import subprocess
import os
import time
import docker
import datetime
import pytz


mount_path = '/Volumes/SunnySD/Security Streams'
folder_name = 'Vector DB'
camera_url = 'rtsp://admin:admin@192.168.0.29:554?tcp'
classes = 'person driveway'
container_name = 'stream_monitor'

pst = pytz.timezone('America/Los_Angeles')

client = docker.from_env()


def start_container_in_background():
    container = client.containers.run(
        image='stream-embed2',
        command='/bin/bash -c "tail -f /dev/null"',
        name=container_name,
        detach=True,
        environment={
            'DB_PATH': '/DB',
            'URL': camera_url,
            'CLASSES': classes
        },
        volumes={f'{mount_path}/{folder_name}': {'bind': '/DB', 'mode': 'rw'}},
        platform='linux/arm64'
    )
    return container

# handle the case where the container is already running
try:
    container = client.containers.get(container_name)
    
    if container.status == 'running':
        container.stop()
    
    container.remove()
except docker.errors.NotFound:
    print(f'Container {container_name} not found, creating new container')

# start off the container
container = start_container_in_background()


prev_log = None
# monitor the container and restart it if it stops
try:
    while True:
        container = client.containers.get(container_name)
        
        # Fetch and process logs
        line = container.logs(stream=False, tail=1).decode().strip()
        if line == prev_log:
            prev_log = line
            continue
        prev_log = line
        if line.startswith('sqlite3.OperationalError:'):
            print('Database error, restarting container...')
            container.restart()
            time.sleep(1)
            continue

        print(line)

        date_line = line.split(' :')[0]
        # date printed in the log like datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"). try to parse it and compare to current time
        # if the time difference is greater than 10 seconds, restart the container
    
        pst_date = None
        try:
            # line is pst so lets take that into account when parsing
            # date = datetime.datetime.strptime(line, '%Y-%m-%d %I:%M:%S %p')
            pst_date = pst.localize(datetime.datetime.strptime(date_line, "%Y-%m-%d %I:%M:%S %p"))

        except Exception as e:
            print('error', e)
            pass
        if pst_date:
            print((datetime.datetime.now(pst) - pst_date).seconds)
            if (datetime.datetime.now(pst) - pst_date).seconds > 10:
                print(f"Time since last log: {(datetime.datetime.now(pst) - pst_date).seconds}")
                print("Restarting container")
                container.restart()

        time.sleep(0.3)  # Delay between log fetches

except KeyboardInterrupt:
    # when we command-c this program, we want to stop the container
    print('Interrupted, stopping container...')
    container = client.containers.get(container_name)
    container.stop()
    container.remove()
except Exception as e:
    # Handle other exceptions
    print(f'An error occurred: {e}')
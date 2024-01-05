import subprocess
import os
import time

mount_path = '/Volumes/SunnySD/Security Streams'
seg_time = 10
camera_url = 'rtsp://admin:admin@192.168.0.29:554?tcp'
folder_name = 'cam1'
container_name = 'ffmpeg_recorder'

os.system("docker rm ffmpeg_recorder -f")
time.sleep(0.5)

cmd = f'docker run --name "{container_name}" -v "{mount_path}":"/usr/data/recordings" -e VIDEO_SEGMENT_TIME={seg_time} "mynvr" "{camera_url}" {folder_name}'

print(cmd)

previous_size = 0
subprocess.Popen(cmd, shell=True)

def get_total_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


while True:
    time.sleep(seg_time+1)
    print(previous_size)
    if os.path.exists(f'{mount_path}/{folder_name}'):
        size = get_total_size(f'{mount_path}/{folder_name}')
        if size > previous_size:
            previous_size = size
            continue
        else:
            command = "docker rm ffmpeg_recorder -f"
            # run this command to stop the container, just use os.system
            os.system(command)

            print("Starting new container")
            # run this command to start the container again
            subprocess.Popen(cmd, shell=True)


        previous_size = size
    else:
        print('Folder does not exist')
        break


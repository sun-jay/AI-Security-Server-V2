from PIL import Image
import time
import os
import subprocess
import chromadb
import datetime
import pytz
import numpy as np

from motion_detect import frame_difference_metric

pst = pytz.timezone('America/Los_Angeles')


os.system("chmod 775 /DB")
time.sleep(1)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

db_path = os.getenv('DB_PATH', '/Volumes/SunnySD/Security Streams/Vector DB')
camera_url = os.getenv('CAMERA_URL', 'rtsp://admin:admin@192.168.0.29:554?tcp')
classes = os.getenv('CLASSES', 'person driveway').split()

client = chromadb.PersistentClient(db_path)

from clip_base import CLIPClassifier
classifier = CLIPClassifier()



def get_frame_ffmpeg():
    command = "ffmpeg -rtsp_transport tcp -analyzeduration 2147483647 -probesize 2147483647 -y -i 'rtsp://admin:admin@192.168.0.29:554?tcp' -vframes 1 cur_frame.jpg"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # process = subprocess.Popen(command, shell=True)
    process.wait()
    print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ", "Frame captured")
    ret = None
    try :
        ret = Image.open('cur_frame.jpg')
        return ret
    except Exception as e:
        return None


try:
    collection = client.create_collection(name="images", metadata={"hnsw:space": "cosine"} )
    print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ","Collection created")
except Exception as e:
    collection = client.get_collection(name="images")
    print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ","Collection connected")




try:
    while True:
        frame = get_frame_ffmpeg()

        if os.path.exists('temp.jpg'):
            # frames should be np arrays
            diff = frame_difference_metric(np.array(Image.open('temp.jpg')), np.array(frame))
            if diff < 1:
                print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ", "No motion detected")
                time.sleep(0.1)
                continue

        if frame is not None:
            frame.save('temp.jpg')
            if classes:
                ret, embeddings = classifier.classify('temp.jpg', classes)
            else:  
                ret, embeddings = classifier.classify('temp.jpg', ["driveway or frontdoor", "person", "delivery man"])
            
            # we are in pacific time
            print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ", ret)


            # Store the embeddings and timestamp in the database``

            # print(embeddings.shape) -> (1, 512)


            collection.add(
                embeddings=list([float(n) for n in embeddings[0]]),
                documents=[datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p")],
                metadatas=[ret],
                ids=[str(time.time())]
            )
        else:
            print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ","Frame not captured")


finally:
    print(datetime.datetime.now(pst).strftime("%Y-%m-%d %I:%M:%S %p"),": ","Stopping camera")
  

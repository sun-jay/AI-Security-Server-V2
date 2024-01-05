import chromadb
import os
from clip_base import CLIPClassifier
import datetime
import bisect
import pytz
import cv2
import sys

# get the first arg and default to person
query = sys.argv[1] if len(sys.argv) > 1 else "person"
print("Query: ", query)


# set up timezone, clip classifier, and vector db client
pst = pytz.timezone('America/Los_Angeles')
utc = pytz.utc
video_location = '/Volumes/SunnySD/Security Streams/cam1'

clip = CLIPClassifier()

db_path = os.getenv('DB_PATH', '/Volumes/SunnySD/Security Streams/Vector DB')
client = chromadb.PersistentClient(db_path)

try:
    collection = client.create_collection(name="images")
except Exception as e:
    collection = client.get_collection(name="images")

# methods for parsing results from vector db
def results_to_entries(results):
    entries = []
    for i in range(len(results['ids'][0])):
        entry = {}
        entry['id'] = results['ids'][0][i]
        entry['distance'] = results['distances'][0][i]
        entry['metadata'] = results['metadatas'][0][i]
        entry['document'] = results['documents'][0][i]
        entries.append(entry)
    return entries

def search_for_word(word, list = True, n = 10):
    embedding = clip.generate_text_embedding(word)
    results = collection.query(
        query_embeddings=embedding,
        n_results=n
    )
    if list:
        return results_to_entries(results)

    return results

def print_by_element(entries):
    [print(e) for e in entries]

    
def get_sorted_timestamps(video_location):
    files = os.listdir(video_location)

    sorted_timestamps = []

    # the file timestamp is in utc
    for f in files:
        try:
            timestamp = datetime.datetime.strptime(f[:-4], '%Y-%m-%d_%H-%M-%S')
            timestamp = utc.localize(timestamp).astimezone(pst)+datetime.timedelta(hours=-1)
            sorted_timestamps.append((timestamp, f"{video_location}/{f}"))
        except ValueError:
            print(f"Skipping file {f} because it does not match the expected format")
            continue

    sorted_timestamps.sort(key = lambda x: x[0])

    return sorted_timestamps

sorted_timestamps = get_sorted_timestamps(video_location)

def find_video_by_unix_timestamp(unix_timestamp, n = 1, video_location = '/Volumes/SunnySD/Security Streams/cam1'):

    # convert the unix timestamp to a datetime object
    target_timestamp = datetime.datetime.fromtimestamp(unix_timestamp, pst)

    # use bisect to find the closest timestamp
    index = bisect.bisect_left(sorted_timestamps, target_timestamp, key=lambda x: x[0])

    if index > n and index < len(sorted_timestamps) - n:
        return sorted_timestamps[index-n-1:index+n]
    
    return sorted_timestamps[index-1]

def play_video(vid):
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()


events = search_for_word(query, n = collection.count())
# out.sort(key = lambda x: x['metadata']['person'], reverse=True)
num_entries = collection.count()
print("Number of entries in the collection: ", num_entries)

# events  = list(filter(lambda x: x['metadata']['person'] > 0.5, events))
print_by_element(events)

for event in events:

    timestamp = float(event['id'])
    time_from_timestamp = datetime.datetime.fromtimestamp(timestamp, pst).strftime("%Y-%m-%d %I:%M:%S %p")
    date_and_time = event['document']

    print("date_and_time: ", date_and_time)
    print("Unix Timestamp: ", timestamp)

    vids = find_video_by_unix_timestamp(timestamp)

    vid = cv2.VideoCapture(vids[1][1])

    print("Playing video: ", vids[1][1])
    play_video(vid)


    input("Play next event?")






# mock_embeddings = [1] * 512






# # results = collection.query(
# #     query_embeddings=mock_embeddings,
# #     n_results=1000000
# # )
# num_entries = collection.count()
# print("Number of entries in the collection: ", num_entries)




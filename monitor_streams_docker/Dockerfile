# Use an official Ubuntu base image with Python and OpenCV
FROM linuxserver/ffmpeg

# Set a working directory
WORKDIR /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    python3-opencv 

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip3 install -r requirements.txt
RUN pip3 install torch
RUN pip3 install Pillow
RUN pip3 install chromadb
RUN pip3 install pytz
RUN pip3 install numpy

# Copy files from your host to your container
COPY clip_base.py /app/clip_base.py
COPY download_model.py /app/download_model.py
COPY motion_detect.py /app/motion_detect.py
RUN python3 download_model.py
COPY embed_frames.py /app/embed_frames.py

RUN mkdir /DB

# Run a command when the container starts
ENTRYPOINT ["python3","-u", "embed_frames.py"]
# CMD [ "bash" ]

# docker build -t stream-embed .
# docker run -it -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' stream-embed class1 class2 class3
# docker run -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' -e CLASSES="person driveway" stream-embed 

# docker run -it --rm --entrypoint bash --network=host --platform linux/arm64 stream-embed1

# docker run -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' -e CLASSES="person driveway" --rm --platform linux/arm64 stream-embed1


# docker run -e DB_PATH="/DB" -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' -e CLASSES="person driveway" -v "/Volumes/SunnySD/Security Streams/Vector DB":"/DB" --rm --platform linux/arm64 stream-embed2


# docker run -it --entrypoint bash -e DB_PATH="/DB" -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' -e CLASSES="person driveway" -v "/Volumes/SunnySD/Security Streams/Vector DB":"/DB" --rm --platform linux/arm64 stream-embed2


# docker run -e DB_PATH="/DB" -e URL='rtsp://admin:admin@192.168.0.29:554?tcp' -e CLASSES="person driveway" -v "/Volumes/SunnySD/Security Streams/Vector DB":"/DB" --rm --platform linux/arm64 stream-embed2

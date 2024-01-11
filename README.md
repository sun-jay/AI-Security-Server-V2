# AI Securty Server V2
## Demo

https://github.com/sun-jay/AI-Security-Server-V2/assets/80140457/a63305c2-9e35-405f-ba81-16033e0b1b62



## Run Locally
The project consists of 4 concurrent processes: record_streams.py, monitor_streams.py, Nextjs frontend, main.py (serves frontend). You will need to update the RTSP URL and file save paths for your setup. 

In `/backend` run:

`python3 record streams.py`

 `python3 monitor_streams.py`
 
 `uvicorn main:app --reload`

In `/frontend` run:

`yarn install`

`yarn dev`
## Tech Stack

**Docker & FFMPEG**: containerized Security Camera NVR (Network Video Recorder)

**PyTorch and Azure ML Studio Cloud GPUs**: fine tuning OpenAI’s CLIP model on a custom doorbell camera dataset

**ChromaDB**: vector database for local embedding storage and vector similarity search

**Python FastAPI**: backend server

**NextJS, React, and TailWindCSS**: frontend interface


## About
**Problem Statement**: Modern consumer security platforms such as Ring only offer rudimentary AI person detection, leaving anomaly filtering a mostly manual and time consuming task.

**Vision Statement**: The current state of computer vision allows for advanced natural language queries and highly efficient searching, which is not yet utilized on many platforms. I sought out to build an app that could leverage and build on new AI technologies to embark on the next step of AI powered security.

  
  

This is actually my second time attempting this project. My first attempt was a good POC, but nowhere near an MVP. These are lessons I learned from from the first attempt:

  

-   Many security cameras steam over WiFi using RTSP (Real Time Streaming Protocol). You can use Python to view and save these streams, but the streams can lose packets, disconnect, or time out with poor error handling. Readily available Python libraries that let you stream over RTSP simply do not provide the level of fault tolerance we need to record indefinitely.
    
-   This is a project that requires multiple concurrent processes (recording streams, AI monitoring, API serving video clips) each with different dependencies and some having to be restarted occasionally and some being free to run indefinitely. I learned the hard way that Dockerizing the different processes and mounting a volume is simply the best way to conduct this orchestra, giving each section a nice environment to perform in, and a way to restart processes that go out of tune.
    
-   On my first attempt, I used OpenPose by Google to monitor the streams. I chose this because it can run at 60 FPS on a CPU and provide accurate person detection. While reliable, this ultimately failed to produce an outcome that hasn't already been perfected by larger platforms like Ring. However, once I started dabbling with OpenAI’s CLIP (Contrastive Language–Image Pre-training) model, I realized this technology had much more powerful applications in the security space than OpenPose.
    

  

With these powerful lessons learned, I set out to build AI Security Cam Server V2.


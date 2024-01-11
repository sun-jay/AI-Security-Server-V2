from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from search_streams import query_and_return_path 

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Query(BaseModel):
    start_time: float
    end_time: float
    query: str

@app.post("/query")
def get_video(query: Query):
    start_time = query.start_time
    end_time = query.end_time
    query = query.query


    path = query_and_return_path(query)
    

    # Path to your video file
    # video_path = "/Volumes/SunnySD/Security Streams/cam1/2024-01-03_19-39-00.mp4"
    return FileResponse(path)

"""
if we had to hit this using js fetch we would do

const response = await fetch('http://localhost:8000/get_video', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({start_time: 0, end_time: 10, query: "person"}) // body data type must match "Content-Type" header
    });


"""

# run using uvicorn main:app --reload

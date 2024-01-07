import React, { useState } from 'react';

function VideoComponent( props ) {
    const fetchVideo = async () => {
        try {
            const response = await fetch('http://localhost:8000/get_video');
            const videoBlob = await response.blob();
            const url = URL.createObjectURL(videoBlob);
            setVideoUrl(url);
        } catch (error) {
            console.error('Error fetching the video', error);
        }
    };

    return (
        <div className="flex items-center justify-center">
            {props.videoUrl && <video className="w-8/12 h-8/12" src={props.videoUrl} controls autoPlay />}
        </div>
    );
}

export default VideoComponent;

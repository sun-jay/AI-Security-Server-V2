import React from 'react'
import { useEffect, useState } from 'react'

const RandomButton = () => {
    const [color, setColor] = useState("white");
    useEffect(() => {
        const interval = setInterval(() => {
            setColor(generateRandomPastelColor()); // Generate a random color
        }, 1000); // Change color every 100 milliseconds

        return () => clearInterval(interval);
    }, []);

    function generateRandomPastelColor() {
        const hue = Math.floor(Math.random() * 360); // Random hue value between 0 and 360
        const saturation = Math.floor(Math.random() * 30) + 70; // Random saturation value between 70 and 100
        const lightness = Math.floor(Math.random() * 30) + 70; // Random lightness value between 70 and 100

        return `hsl(${hue}, ${saturation}%, ${lightness}%)`; // Return the HSL color string
    }
    return (
        <button className="transition duration-1000 m-4 p-4 w-1/12 text-center border border-black rounded-xl"
        style={{ backgroundColor: color }}>Random!</button>
    )
}

export default RandomButton
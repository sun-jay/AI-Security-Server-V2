import { useState } from "react";
import { useEffect } from "react";
import BG from "../components/BG";
import VideoComponent from "../components/VideoComponent";

export default function ExampleComponent() {
  const [isVisible, setIsVisible] = useState(false);

  const handleButtonClick = () => {
    setIsVisible(true);
  };
  const [color, setColor] = useState("#000");

  useEffect(() => {
    const interval = setInterval(() => {
      setColor(generateRandomPastelColor()); // Generate a random color
    }, 100); // Change color every 100 milliseconds

    return () => clearInterval(interval);
  }, []);

  function generateRandomPastelColor() {
    const hue = Math.floor(Math.random() * 360); // Random hue value between 0 and 360
    const saturation = Math.floor(Math.random() * 30) + 70; // Random saturation value between 70 and 100
    const lightness = Math.floor(Math.random() * 30) + 70; // Random lightness value between 70 and 100

    return `hsl(${hue}, ${saturation}%, ${lightness}%)`; // Return the HSL color string
  }

  return (
    <div>
      <VideoComponent />
    </div>
  )}





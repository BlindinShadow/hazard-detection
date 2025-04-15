import { useState, useRef, useEffect } from 'react';

export default function Home() {
  const [imageURL, setImageURL] = useState(null);
  const [videoURL, setVideoURL] = useState('');
  const [videoDetections, setVideoDetections] = useState([]);
  const imgCanvas = useRef();
  const vidCanvas = useRef();
  const videoEl = useRef();

  // Draw image + boxes
  const drawImage = (url, det) => { /* ... */ };

  // Handle image file upload
  const onImageChange = async e => { /* POST to /api/detect, draw on canvas */ };

  // Handle video URL submit
  const onVideoSubmit = async () => { /* POST to /api/detect_video, play video */ };

  // Overlay detections per frame as video plays
  useEffect(() => { /* sync canvas with <video> frames */ }, [videoDetections]);

  return (
    <div style={{ padding: 20 }}>
      <h1>Hazard Detection</h1>

      {/* Image Upload Section */}
      <section>…</section>

      {/* Video URL Section */}
      <section>…</section>
    </div>
  );
}

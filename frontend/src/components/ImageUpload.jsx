import React, { useState } from 'react';
import { predictGesture } from '../api';

export default function ImageUpload({ onResult }) {
  const [imageFile, setImageFile] = useState(null);

  const handleChange = (e) => setImageFile(e.target.files[0]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (imageFile) {
      const prediction = await predictGesture(imageFile);
      onResult(prediction);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={handleChange} required />
      <button type="submit">Predict</button>
    </form>
  );
}

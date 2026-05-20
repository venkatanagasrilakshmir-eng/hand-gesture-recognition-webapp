import React, { useState } from 'react';
import ImageUpload from './components/ImageUpload';
import './styles/style.css';

function App() {
  const [result, setResult] = useState('');

  return (
    <div className="container">
      <h1>Hand Gesture Recognition</h1>
      <ImageUpload onResult={setResult} />
      {result && <h2>Prediction: {result}</h2>}
    </div>
  );
}

export default App;

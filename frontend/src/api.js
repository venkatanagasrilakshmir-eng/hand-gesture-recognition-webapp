export async function predictGesture(file) {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('http://localhost:5000/api/predict', {
    method: 'POST',
    body: formData,
  });
  const data = await response.json();
  return data.prediction;
}

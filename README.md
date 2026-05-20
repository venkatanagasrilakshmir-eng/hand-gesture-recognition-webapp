# ✋🤚 Hand Gesture Recognition Web App

A professional, modular web platform to recognize hand gestures from images using deep learning with an easy-to-use web UI.

---

## 📌 Project Overview

The project enables users to upload images of hand gestures and get instant classification results, powered by a trained Convolutional Neural Network (CNN).

---

## 📊 System Architecture

**High-level Data Flow:**

```
+-----------+      upload      +------------+   REST API  +--------+    predict   +----------------------+
|  Browser  |---------------->|  Frontend  |<===========>| Backend |<===========>| hand_gesture_model.h5 |
+-----------+   (image file)   +------------+   (JSON)    +--------+             +----------------------+
                                                        Flask API       Trained ML Model
```

### **More Detailed Diagram**

![Project Architecture Diagram](docs/architecture.png)

*Above: Replace `architecture.png` with your own custom image in `docs/` if you have one.*

---

## 🚀 Quickstart

### 1️⃣ Clone and Prepare
```bash
git clone https://github.com/yourusername/hand-gesture-recognition-webapp.git
cd hand-gesture-recognition-webapp
```

### 2️⃣ Train Model (once per dataset)
```
# Organize your dataset as:
# data/ClassName/image1.png
# data/ClassName/image2.jpg  etc.
python train_hand_gesture_model.py
```
This saves the model as `models/hand_gesture_model.h5`

### 3️⃣ Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env   # update config if needed
python run.py
```

### 4️⃣ Frontend Setup
```bash
cd frontend
npm install
npm start
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

---


## 👩‍💻 API Workflow

```
[User Image Upload] => [Frontend React] --POST /api/predict--> [Flask API] --> [Model Prediction] --> [Response to UI]
```

- **Endpoint:** `POST /api/predict`  
  Form-data: `file` (image)
- **Response:**
  ```json
  { "prediction": "Peace" }
  ```

---

## 📂 Dataset Example

```
data/
  Fist/
    img1.png
    ...
  Open/
    img2.jpg
    ...
```

---

## 📸 Example UI

![UI Example](docs/ui_example.png)

*Give users a friendly upload prompt and display result instantly!*

---

## 📝 Documentation

Additional docs for devs and deployers in [`docs/`](docs/):

- [System Diagram](docs/architecture.png)
- [API Guide](docs/api.md) *(create this)*
- [Model Details](docs/model.md) *(create this)*

---

## 🛡️ License

[MIT License](LICENSE)

---

_Created by [Venkatanagasrilakshmir](https://github.com/your-github)_  
*For questions or collaborations, open an Issue or Pull Request!*

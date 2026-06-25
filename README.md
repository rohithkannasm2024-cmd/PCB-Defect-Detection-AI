# 🤖 AI PCB Defect Detection using YOLOv8

## 📌 Project Overview

AI PCB Defect Detection is a deep learning-based web application that automatically identifies defects in Printed Circuit Boards (PCBs) using the YOLOv8 object detection model.

The system allows users to:

* Upload PCB images for inspection
* Detect defects automatically using AI
* View confidence scores and defect types
* Perform snapshot-based detection using a webcam
* Visualize results through an interactive dashboard

---

## 🎯 Objectives

* Automate PCB quality inspection
* Reduce manual inspection time
* Improve manufacturing accuracy
* Demonstrate real-world industrial AI applications

---

## 🚀 Features

### Image Upload Detection

Upload any PCB image and instantly detect defects.

### AI-Powered Detection

Uses YOLOv8 object detection for defect localization and classification.

### Dashboard Results

Displays:

* Original PCB Image
* Detected Output Image
* Defect Type
* Confidence Score
* Number of Defects Detected

### Snapshot Detection

Capture an image from a webcam and perform instant PCB inspection.

### Modern Web Interface

Professional Flask-based dashboard with responsive design.

---

## 🛠 Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Artificial Intelligence

* YOLOv8
* Ultralytics
* OpenCV

### Development Tools

* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
PCB-Defect-Detection-AI
│
├── app.py
├── predict.py
├── live_detection.py
├── requirements.txt
│
├── templates
│   ├── index.html
│   ├── dashboard.html
│   └── webcam.html
│
├── static
│   ├── css
│   ├── uploads
│   ├── results
│   └── images
│
├── dataset_yolo
│
├── runs
│   └── detect
│
└── README.md
```

---

## 📊 Dataset

The model was trained using a PCB defect dataset containing multiple defect classes such as:

* Missing Hole
* Mouse Bite
* Open Circuit
* Short Circuit
* Spur
* Spurious Copper

The dataset was converted into YOLO format for training.

---

## 🧠 Model Training

### Model

YOLOv8 Nano (YOLOv8n)

### Training Parameters

* Epochs: 50
* Image Size: 640
* Framework: Ultralytics YOLOv8

### Training Command

```bash
python train.py
```

---

## 📈 Evaluation Metrics

The model performance was evaluated using:

* Precision
* Recall
* mAP@50
* mAP@50-95
* F1 Score

Training visualizations include:

* Confusion Matrix
* Precision Curve
* Recall Curve
* PR Curve
* F1 Curve

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/PCB-Defect-Detection-AI.git
cd PCB-Defect-Detection-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 📷 Workflow

1. Open the application.
2. Upload a PCB image.
3. AI model detects defects.
4. Results are displayed on the dashboard.
5. Users can also use Snapshot Detection through webcam capture.

---

## 🌟 Future Enhancements

* Real-time factory conveyor inspection
* Mobile application integration
* Cloud deployment
* PDF inspection report generation
* Multi-camera industrial monitoring
* Defect severity analysis
* Production analytics dashboard

---


## 👨‍💻 Author

Rohith Kanna S.M.

---

## 📄 License

This project is developed for educational and research purposes.


## Author

**Rohith Kanna S.M**

from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import shutil

app = Flask(__name__)

# -----------------------------
# Load Trained YOLOv8 Model
# -----------------------------
model = YOLO("runs/detect/pcb_defect/weights/best.pt")

# -----------------------------
# Create Required Folders
# -----------------------------
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Prediction Route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded!"

    file = request.files["image"]

    if file.filename == "":
        return "No file selected!"

    # Save uploaded image
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    # Run prediction
    results = model.predict(
        source=image_path,
        save=True,
        exist_ok=True
    )

    result = results[0]

    # --------------------------------
    # Get Prediction Details
    # --------------------------------
    count = len(result.boxes)

    if count > 0:
        class_id = int(result.boxes.cls[0])
        defect = result.names[class_id]
        confidence = f"{float(result.boxes.conf[0]) * 100:.2f}%"
    else:
        defect = "No Defect Detected"
        confidence = "0%"

    # --------------------------------
    # Find YOLO Output Image
    # --------------------------------
    predicted_folder = str(result.save_dir)

    predicted_image = os.path.join(
        predicted_folder,
        file.filename
    )

    destination = os.path.join(
        RESULT_FOLDER,
        file.filename
    )

    if os.path.exists(predicted_image):
        shutil.copy(predicted_image, destination)

    # --------------------------------
    # Open Dashboard
    # --------------------------------
    return render_template(
    "dashboard.html",
    filename=file.filename,
    image="results/" + file.filename,
    defect=defect,
    confidence=confidence,
    count=count
)
# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
   
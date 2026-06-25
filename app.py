from flask import Flask, render_template, request, Response
from ultralytics import YOLO
import cv2
import os
import shutil
import base64
from flask import Response

app = Flask(__name__)

# ==========================================
# Load Trained YOLOv8 Model
# ==========================================
model = YOLO("runs/detect/pcb_defect/weights/best.pt")
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()

# ==========================================
# Create Required Folders
# ==========================================
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# ==========================================
# Home Page
# ==========================================
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()
@app.route("/")
def home():
    return render_template("index.html")
# ==========================================
# Webcam Page
# ==========================================
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()
@app.route("/webcam")
def webcam():
    return render_template("webcam.html")
@app.route("/capture", methods=["POST"])
@app.route("/snapshot")
def snapshot():
    return render_template("webcam.html")


def capture():

    image_data = request.form["imageData"]

    image_data = image_data.split(",")[1]

    image_bytes = base64.b64decode(image_data)

    filename = "snapshot.jpg"

    image_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(image_path,"wb") as f:
        f.write(image_bytes)

    results = model.predict(
        source=image_path,
        save=True,
        exist_ok=True
    )

    result = results[0]

    count = len(result.boxes)

    if count > 0:

        class_id = int(result.boxes.cls[0])

        defect = result.names[class_id]

        confidence = f"{float(result.boxes.conf[0])*100:.2f}%"

    else:

        defect = "No Defect Detected"

        confidence = "0%"

    predicted_folder = str(result.save_dir)

    predicted_image = os.path.join(
        predicted_folder,
        filename
    )

    destination = os.path.join(
        RESULT_FOLDER,
        filename
    )

    if os.path.exists(predicted_image):
        shutil.copy(
            predicted_image,
            destination
        )

    return render_template(
        "dashboard.html",
        filename=filename,
        image="results/" + filename,
        defect=defect,
        confidence=confidence,
        count=count
    )



# ==========================================
# Image Prediction
# ==========================================
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded!"

    file = request.files["image"]

    if file.filename == "":
        return "No file selected!"

    # Save uploaded image
    image_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(image_path)

    # Run YOLO Prediction
    results = model.predict(
        source=image_path,
        save=True,
        exist_ok=True,
        conf=0.25
    )

    result = results[0]

    # ==========================================
    # Extract Detection Details
    # ==========================================
    count = len(result.boxes)

    if count > 0:

        class_id = int(result.boxes.cls[0])

        defect = result.names[class_id]

        confidence = (
            f"{float(result.boxes.conf[0]) * 100:.2f}%"
        )

    else:

        defect = "No Defect Detected"

        confidence = "0%"

    # ==========================================
    # Copy YOLO Output To Static Folder
    # ==========================================
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

        shutil.copy(
            predicted_image,
            destination
        )

    # ==========================================
    # Open Dashboard
    # ==========================================
    return render_template(
        "dashboard.html",
        filename=file.filename,
        image="results/" + file.filename,
        defect=defect,
        confidence=confidence,
        count=count
    )




# ==========================================
# Live Video Generator
# ==========================================
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model.predict(
            source=frame,
            conf=0.25,
            verbose=False
        )

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(
            '.jpg',
            annotated_frame
        )

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()


# ==========================================
# Video Feed Route
# ==========================================
def generate_frames():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )

    cap.release()
@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


# ==========================================
# Run Flask
# ==========================================
@app.route("/live")
def live():
    return render_template("live.html")

if __name__ == "__main__":
    app.run(debug=True)


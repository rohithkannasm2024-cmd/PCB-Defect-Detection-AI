from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/pcb_defect/weights/best.pt")

# Predict
results = model.predict(
    source="test_images/pcb1.jpg",
    save=True,
    conf=0.25
)

print("Prediction Completed!")
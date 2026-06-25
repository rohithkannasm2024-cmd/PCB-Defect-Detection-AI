from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/detect/pcb_defect/weights/best.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Could not read webcam")
        break

    # Run prediction
    results = model.predict(
        source=frame,
        conf=0.25,
        verbose=False
    )

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("Live PCB Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
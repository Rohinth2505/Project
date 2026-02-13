import cv2
from ultralytics import YOLO

# --- 1. Load Higher Accuracy Model ---
# yolov8n = nano (fast, less accurate)
# yolov8s = small
# yolov8m = medium
# yolov8l = large
# yolov8x = extra large (best accuracy)

model = YOLO("yolov8m.pt")   #  Better accuracy than yolov8n

# --- 2. Open Webcam ---
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# --- 3. Processing Loop ---
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Improved Detection Settings
    results = model.track(
        frame,
        conf=0.5,        
        imgsz=960,      
        persist=True,   
        tracker="bytetrack.yaml" 
    )

    annotated_frame = results[0].plot()

    cv2.imshow("High Accuracy Object Detection & Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

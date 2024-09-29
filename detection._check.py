import cv2
from ultralytics import YOLO

# Load the custom YOLOv8 model
model = YOLO('best.pt')  # Replace 'best.pt' with your model file
classes=['ESP32', 'Raspberry Pi', 'Raspberry Pi Pico','Led','Arduino']

def process_image(image):
    # Run inference
    results = model.predict(image, conf=0.5)  # Adjust confidence threshold as needed

    # Process results and draw bounding boxes
    for result in results:
        for box in result.boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # (x1, y1, x2, y2)
            conf = box.conf[0]*100  # Confidence score
            cls = box.cls[0]  # Class index

            if conf > 50:
                 # Draw bounding box and label on the image
                label = f'Class {classes[int(cls)]}: {conf:.2f}'
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return image

def detect_tool(video_source=0):  # Use 0 for webcam or provide a video file path
    # Open video capture
    cap = cv2.VideoCapture(video_source)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame for object detection
        processed_frame = process_image(frame)

        # Display the frame
        cv2.imshow('Object Detection', processed_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_tool()  # Run the main function

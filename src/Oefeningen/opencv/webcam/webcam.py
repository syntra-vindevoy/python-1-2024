import time

import cv2


# Load YOLO
def load_yolo_model():
    # Paths to YOLO config and weights (download YOLOv3/YOLOv4 from official sources or pre-trained COCO)
    yolo_weights = 'yolov3.weights'  # Replace with your YOLO weights file path
    yolo_config = 'yolov3.cfg'  # Replace with your YOLO config file path
    coco_names = 'coco.names'  # Replace with your COCO labels file path

    # Read class names
    with open(coco_names, 'r') as f:
        classes = f.read().strip().split('\n')

    # Load YOLO network
    net = cv2.dnn.readNetFromDarknet(yolo_config, yolo_weights)
    # Use OpenCV's DNN backend and target
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    return net, classes


# Process detections
def process_detections(outputs, frame, classes, target_classes):
    height, width = frame.shape[:2]
    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]  # Class scores
            class_id = scores.argmax()  # Index of highest class score
            confidence = scores[class_id]  # Confidence score
            if confidence > 0.5 and classes[class_id] in target_classes:
                # Scale box coordinates to image size
                center_x, center_y, w, h = (
                        detection[0:4] * [width, height, width, height]
                ).astype(int)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-maximum suppression to refine overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    return [(boxes[i], class_ids[i], confidences[i]) for i in indices.flatten()]


def main():
    # Load YOLO model
    net, classes = load_yolo_model()
    target_classes = {"person", "bicycle", "cat"}  # Classes to detect

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    last_saved_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Prepare the frame for YOLO
        blob = cv2.dnn.blobFromImage(
            frame, scalefactor=1 / 255.0, size=(416, 416), swapRB=True, crop=False
        )
        net.setInput(blob)

        # Get model output layer names
        ln = net.getUnconnectedOutLayersNames()

        # Perform forward pass
        outputs = net.forward(ln)

        # Process detections
        detections = process_detections(outputs, frame, classes, target_classes)

        for (box, class_id, confidence) in detections:
            x, y, w, h = box
            label = f"{classes[class_id]}: {confidence:.2f}"
            color = (0, 255, 0) if classes[class_id] == "cat" else (255, 0, 0)
            if classes[class_id] == "bicycle":
                color = (0, 255, 255)  # Yellow color for bicycles

            # Draw bounding box and label
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(
                frame,
                label,
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                1,
                lineType=cv2.LINE_AA,
            )
            print(f"{label} detected!")

            # Save frame every 10 seconds
            current_time = time.time()
            if current_time - last_saved_time >= 10:
                filename = f"{classes[class_id]}_detected_{int(current_time)}.jpg"
                cv2.imwrite(filename, frame)
                last_saved_time = current_time

        # Show updated frame
        cv2.imshow("Webcam Stream", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

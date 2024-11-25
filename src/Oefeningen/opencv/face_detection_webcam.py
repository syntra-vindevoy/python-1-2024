import os

import cv2
import numpy as np

# Paths to the DNN models
PROTOTXT_PATH = "deploy.prototxt.txt"
MODEL_PATH = "res10_300x300_ssd_iter_140000.caffemodel"

# Minimum confidence threshold for detection
CONFIDENCE_THRESHOLD = 0.5


def main():
    # Check if the model files exist
    if not os.path.exists(PROTOTXT_PATH) or not os.path.exists(MODEL_PATH):
        print("DNN model files not found. Please check the paths.")
        return

    # Load the DNN model
    net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, MODEL_PATH)

    # Verify that the network has been loaded correctly
    if net.empty():
        print("Failed to load the DNN model. Please check the paths and model files.")
        return

    # Print the layer names
    layer_names = net.getLayerNames()
    print("Loaded Layers:")
    for name in layer_names:
        print(name)

    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam!")
        return

    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot read frame!")
            break
        try:
            # Prepare the frame for detection
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

            # Perform the model on the frame
            net.setInput(blob)
            detections = net.forward()

            # Process the detections
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                # Check if the detection satisfies the threshold
                if confidence > CONFIDENCE_THRESHOLD:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # Draw the bounding box and confidence score
                    text = f"{confidence:.2f}"
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

            # Display the frame
            cv2.imshow("Face Detection with DNN", frame)

        except cv2.error as e:
            print(f"Error during processing frame: {e}")

        # Quit if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
import time

import cv2


def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    last_saved_time = time.time()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        if len(faces) > 0:
            cv2.rectangle(frame, (faces[0][0], faces[0][1]), (faces[0][0] + faces[0][2], faces[0][1] + faces[0][3]),
                          (255, 0, 0), 2)
            print("Face detected!")

            # Save frame only every 10 seconds
            current_time = time.time()
            if current_time - last_saved_time >= 10:
                face_filename = f'face_detected_{int(current_time)}.jpg'
                cv2.imwrite(face_filename, frame)
                last_saved_time = current_time

        # Save the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Webcam Stream', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

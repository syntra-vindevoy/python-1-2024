import cv2

def main():
    # Gebruik het voorgetrainde Haarcascade-model voor gezichtsdetectie
    haarcascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(haarcascade_path)

    # Open de video-stream (0 = standaard webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kan de webcam niet openen!")
        return

    print("Druk op 'q' om te stoppen.")

    while True:
        # Lees een frame van de video
        ret, frame = cap.read()

        if not ret:
            print("Kan het frame niet lezen!")
            break

        # Converteer het frame naar grijswaarden (vereist door Haarcascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecteer gezichten in het frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Teken rechthoeken rond de gedetecteerde gezichten
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Toon het frame in een venster
        cv2.imshow("Face Detection", frame)

        # Stop het programma als de gebruiker op 'q' drukt
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Vrijgeven van bronnen
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2

def main():
    # Laad het voorgetrainde Haarcascade-model voor kattengezichten
    haarcascade_path = cv2.data.haarcascades + "haarcascade_frontalcatface.xml"
    cat_cascade = cv2.CascadeClassifier(haarcascade_path)

    # Controleer of het model correct is geladen
    if cat_cascade.empty():
        print("Kan het Haarcascade-model voor katten niet laden!")
        return

    # Open de webcam
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

        # Detecteer kattengezichten in het frame
        cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Teken rechthoeken rond de gedetecteerde kattengezichten
        for (x, y, w, h) in cats:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Cat", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Toon het frame in een venster
        cv2.imshow("Cat Detection", frame)

        # Stop het programma als de gebruiker op 'q' drukt
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Vrijgeven van bronnen
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

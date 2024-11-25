import cv2 as cv


def get_webcam():
    """
    Captures live video from the default camera and displays it in a
    window.

    This function reads frames from the default video capture device
    (usually the built-in or an attached camera). It continuously
    displays the frames in a window. The video feed can be stopped by
    pressing the 'q' key.

    :return: None
    """
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def get_video():
    """
    Display a video in a window. The function captures video from the specified
    file path, resizes each frame, and displays it. The video display loop
    continues until the user presses the 'q' key.

    :return: None
    """
    cap = cv.VideoCapture("video/dog.mp4")
    while True:
        ret, frame = cap.read()
        cv.imshow("Video", rescale_frame(frame, scale=0.25))
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def read_image():
    """
    Reads an image from a predefined path and displays it in a window.

    Summary:
        This function uses OpenCV to read an image from a specified path, display it in
        a window with a given title, and waits for a key press to close the window and
        clean up resources.

    :return: None
    """
    img = cv.imread("images/ben.jpg")

    img = blur_image(change_brightness(img, 100))
    # img = cv.resize(img, (500, 500))
    cv.imshow("Cat", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def resize_image():
    img = cv.imread("images/ben.jpg")
    resized_img = cv.resize(img, (100, 100), interpolation=cv.INTER_CUBIC)
    cv.imshow("Resized Cat", resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def show_canny():
    img = cv.imread("images/ben.jpg")
    canny = cv.Canny(img, 100, 200)
    cv.imshow("Canny", canny)
    cv.waitKey(0)
    cv.destroyAllWindows()


def show_gray():
    img = cv.imread("images/ben.jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()


def rotate_image():
    img = cv.imread("images/ben.jpg")
    rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    cv.imshow("Rotated", rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_brightness(frame, value=30):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv.merge((h, s, v))
    return cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)


def change_color(frame, color=(0, 0, 255)):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


def change_resolution(frame, width=640, height=480):
    return cv.resize(frame, (width, height))


def change_format(frame, format="BGR"):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


def blur_image(frame, kernel_size=(5, 5)):
    return cv.GaussianBlur(frame, kernel_size, 0)


if __name__ == '__main__':
    # show_canny()
    rotate_image()
    # read_image()
    # get_video()
    # get_webcam()
    # resize_image()

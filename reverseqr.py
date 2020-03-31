from pyzbar import pyzbar
import cv2


def without_camera():
    img = cv2.imread("qr-id.png")

    decodedObjects = pyzbar.decode(img)

    for obj in decodedObjects:
        print("Data:", obj.data)
        cv2.imshow("Image", img)
    cv2.waitKey(0)


def with_camera():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)

        for obj in decodedObjects:
            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            QRData = obj.data.decode("utf-8")
            QRType = obj.type
            text = "{} ({})".format(QRData, QRType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (191, 95, 0), 2)
            print('Data : ', obj.data)

        cv2.imshow("QR-scanner", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break


without_camera()


with_camera()



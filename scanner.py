import cv2

cv2.namedWindow("Preview")
vc = cv2.VideoCapture(0)
det = cv2.QRCodeDetector()

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Preview", frame)
    rval, frame = vc.read()
    data, bbox, straight_qrcode = det.detectAndDecode(frame)
    if bbox is not None:
        cv2.rectangle(
            img=frame,
            pt1=[int(bbox[0][0][0]), int(bbox[0][0][1])],
            pt2=[int(bbox[0][2][0]), int(bbox[0][2][1])],
            color=(0, 0, 0),
            thickness=2
        )
        cv2.putText(
            img=frame,
            text=data,
            org=([50, 50]),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(0, 0, 0),
            thickness=2
        )

    if cv2.waitKey(20) == 27:  # When ESC is pressed the window closes
        break

cv2.destroyWindow("Preview")
vc.release()

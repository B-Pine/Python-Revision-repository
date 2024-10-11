import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit(0)

while True:
    success, frame = cap.read()
    try:
        gray = cv.cvtColor(frame, cv.COLOR_BGR5552GRAY)
        cv.imshow("VideoCapture", gray)
    except cv.error:
        frame = cv.flip(frame, 1)
        cv.imshow("Video Capture", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

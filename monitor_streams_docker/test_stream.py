url = 'rtsp://admin:admin@192.168.0.29:554?tcp'

import cv2

cap = cv2.VideoCapture(url)

failed_reads = 0
threshold = 10  # Set your own threshold

while True:
    ret, frame = cap.read()
    print(ret)
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        failed_reads = 0  # Reset counter if frame read is successful
    else:
        failed_reads += 1
        if failed_reads >= threshold:
            print("Stream interrupted.")
            break
cap.release()
cv2.destroyAllWindows()
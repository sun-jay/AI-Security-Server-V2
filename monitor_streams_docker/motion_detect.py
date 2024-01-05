import cv2
import numpy as np

def compute_frame_difference(frame1, frame2):
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    return cv2.absdiff(gray2, gray1)


def frame_difference_metric(frame1, frame2, threshold=25):

    # the input should be of t

    # Compute the frame difference
    diff = compute_frame_difference(frame1, frame2)

    # Apply a threshold
    _, thresh_diff = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Sum the differences above the threshold and normalize by the number of pixels
    avg_change_per_pixel = np.sum(thresh_diff) / 255 / (diff.shape[0] * diff.shape[1])

    return avg_change_per_pixel *100





# def get_motion_mask(frame_difference, kernel_size=9):
#     blur = cv2.medianBlur(frame_difference, 3)
#     _, mask = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
#     kernel = np.ones((kernel_size, kernel_size), np.uint8)
#     return cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# def get_contour_detections(mask):
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     detections = []
#     for cnt in contours:
#         x, y, w, h = cv2.boundingRect(cnt)
#         area = w * h
#         if area > 400:
#             detections.append([x, y, x + w, y + h, area])
#     return np.array(detections)

# def non_max_suppression(boxes, threshold=0.1):
#     if len(boxes) == 0:
#         return []

#     boxes = boxes[np.argsort(-boxes[:, 4])]
#     keep = []
#     while boxes.shape[0] > 0:
#         i = boxes[0]
#         keep.append(i[:4])
#         rest = boxes[1:]
#         rest_area = (rest[:, 2] - rest[:, 0]) * (rest[:, 3] - rest[:, 1])
#         i_area = (i[2] - i[0]) * (i[3] - i[1])
#         union = rest_area + i_area
#         xx1 = np.maximum(i[0], rest[:, 0])
#         yy1 = np.maximum(i[1], rest[:, 1])
#         xx2 = np.minimum(i[2], rest[:, 2])
#         yy2 = np.minimum(i[3], rest[:, 3])
#         w = np.maximum(0, xx2 - xx1)
#         h = np.maximum(0, yy2 - yy1)
#         intersection = w * h
#         iou = intersection / (union - intersection)
#         boxes = rest[iou <= threshold]

#     return np.array(keep)


# # video with motion
# # video_path ="/Volumes/SunnySD/Security Streams/cam1/2023-12-31_09-26-40.mp4"

# # video without motion
# video_path ="/Volumes/SunnySD/Security Streams/cam1/2023-12-31_08-55-00.mp4"

# cap = cv2.VideoCapture(video_path)

# frames = []

# for i in range(int(10*1000/300-5)):
#     cap.set(cv2.CAP_PROP_POS_MSEC, i*300) 
#     frames.append(cap.read()[1])


# for i in range(100):
#     frame1 = frames[i]
#     frame2 = frames[i+1]

#     # Motion Detection Pipeline
#     frame_difference = compute_frame_difference(frame1, frame2)

#     dif = frame_difference_metric(frame_difference)

#     print(dif)
    
#     mask = get_motion_mask(frame_difference)

#     # show the mask
#     cv2.imshow("Motion Mask", mask)

#     if cv2.waitKey(0) == ord('q'):
#         continue




# detections = get_contour_detections(mask)
# nms_detections = non_max_suppression(detections)

# # Draw detections on the frame
# for det in nms_detections:
#     x1, y1, x2, y2 = det
#     cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)

# # cv2.imshow("Motion Detection", frame2)
# cv2.destroyAllWindows()

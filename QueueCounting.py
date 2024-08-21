import os
import cv2
from ultralytics import YOLO, solutions
import numpy as np

os.chdir(r"F:\YOLO Projects\QueueCounting")

model = YOLO("yolov8m.pt")

Classes = model.model.names

lst = ["car", "bus", "truck"]
TargetClasses = {}

for key in Classes:
    for i in lst:
        if Classes[key] == i:
            TargetClasses[key] = i
            
ClsInx = list(TargetClasses.keys()) 
      
queue_region = np.array([[521, 197],[1017, 226],[1058, 676],[8, 593]])

cap = cv2.VideoCapture("istockphoto-1293558487-640_adpp_is.mp4")


def draw_text_with_background(frame, text, position, font, scale, text_color, background_color, border_color, thickness=2, padding=5):
    """Draw text with background and border on the frame."""
    (text_width, text_height), baseline = cv2.getTextSize(text, font, scale, thickness)
    x, y = position
    # Background rectangle
    cv2.rectangle(frame, 
                  (x - padding, y - text_height - padding), 
                  (x + text_width + padding, y + baseline + padding), 
                  background_color, 
                  cv2.FILLED)
    # Border rectangle
    cv2.rectangle(frame, 
                  (x - padding, y - text_height - padding), 
                  (x + text_width + padding, y + baseline + padding), 
                  border_color, 
                  thickness)
    # Text
    cv2.putText(frame, text, (x, y), font, scale, text_color, thickness, lineType=cv2.LINE_AA)


while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    else:
        frame = cv2.resize(frame, (1100, 700))
        cv2.polylines(frame, [queue_region], True, [255, 0, 0], 2)
        results = model.track(frame, persist=True, classes=ClsInx, show=False, conf=0.1)
        Counter = set()
        for result in results:
            boxes = result.boxes.xyxy
            ids = result.boxes.id
            classes = result.boxes.cls
            for box, id, cls in zip(boxes, ids, classes):
                x, y, w, h = box
                x, y, w, h = int(x), int(y), int(w), int(h)
                cx, cy = int((x+w)/2), int((y+h)/2)
                if cv2.pointPolygonTest(queue_region, (cx, cy), False) >= 0:
                    Counter.add(int(id))
                    cv2.rectangle(frame, (x, y), (w, h), [0, 255, 0], 2)
                    cv2.circle(frame, (cx, cy), 5, [0, 0, 255], 2)
                    draw_text_with_background(frame, 
                                      f"{TargetClasses[int(cls)].capitalize()}, ID {int(id)}", 
                                      (x, y - 10), 
                                      cv2.FONT_HERSHEY_COMPLEX, 
                                      0.6, 
                                      (255, 255, 255),  # White text
                                      (0, 0, 0),  # Black background
                                      (0, 0, 255))  # Red border
                    
                
            
        Counting = len(Counter)
        draw_text_with_background(frame, 
                                      f"Queue Counts:{Counting}", 
                                      (10, 30), 
                                      cv2.FONT_HERSHEY_COMPLEX, 
                                      0.6, 
                                      (255, 255, 255),  # White text
                                      (0, 0, 0),  # Black background
                                      (0, 0, 255))  # Red border
        
        cv2.imshow("QueueCounting", frame)
        if cv2.waitKey(1) == 27:
            break
        
cap.release()
cv2.destroyAllWindows()
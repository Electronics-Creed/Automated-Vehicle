import cv2
import lane
import car_detection

video = 'project_video.mp4'
cap = cv2.VideoCapture(video)

while cap.isOpened():
    ret, frame = cap.read()
    frame = lane.process(frame)
    frame = car_detection.car_detect(frame)
    cv2.imshow('Detected', frame)
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

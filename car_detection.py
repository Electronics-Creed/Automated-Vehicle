import cv2


def car_detect(frame):
    car_cascade = cv2.CascadeClassifier('cars.xml')
    ncars = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # Draw border
    for (x, y, w, h) in cars:
        if w > 100 and h > 100:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            ncars = ncars + 1
    return frame



import cv2
import numpy as np


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def process(img):
    region_of_interest_vertices = [(220, 670), (550, 440), (740, 430), (1200, 480), (1200, 640)]
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 255, 255)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image, 6, np.pi / 60, 100, lines=np.array([]), minLineLength=40, maxLineGap=25)
    image_with_lines = draw_the_lines(img, lines)
    return image_with_lines


def nothing():
    pass

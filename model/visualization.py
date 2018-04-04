import cv2
import numpy as np


def draw_box(image, box, color, thickness=2):
    # disegno un box in una immagine, con un certo colore ed un certo spessore
    b = np.array(box).astype(int)
    cv2.rectangle(image, (b[0], b[1]), (b[2], b[3]), color, thickness, cv2.LINE_AA)


def draw_caption(image, box, caption):
    # disegno un testo su una immagine
    b = np.array(box).astype(int)
    cv2.putText(image, caption, (b[0], b[1] - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    cv2.putText(image, caption, (b[0], b[1] - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)


def draw_boxes(image, boxes, color, thickness=2):
    # disegno un elenco di box su una immagine, con un certo colore ed un certo spessore
    for b in boxes:
        draw_box(image, b, color, thickness=thickness)


def draw_detections(image, detections, color=(255, 0, 0), generator=None):
    # disegna i box predetti su una immagine
    draw_boxes(image, detections, color=color)

    # disegna le label corrispondenti
    for d in detections:
        label = np.argmax(d[4:])
        score = d[4 + label]
        caption = (generator.label_to_name(label) if generator else label) + ': {0:.2f}'.format(score)
        draw_caption(image, d, caption)


def draw_annotations(image, annotations, color=(0, 255, 0), generator=None):
    # disegna i ground truth su una immagine
    draw_boxes(image, annotations, color)

    # disegna le label corrispondenti
    for b in annotations:
        label = b[4]
        caption = '{}'.format(generator.label_to_name(label) if generator else label)
        draw_caption(image, b, caption)

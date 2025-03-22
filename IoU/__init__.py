# Calculate IoU between two bounding boxes


def calculate_iou(box1, box2):
    # Get the coordinates of the intersection rectangle
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # Calculate the area of the intersection rectangle
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # Calculate the area of the two bounding boxes
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # Calculate the area of the union of the two bounding boxes
    union_area = box1_area + box2_area - intersection_area

    # Calculate the Intersection over Union (IoU)
    iou = intersection_area / union_area

    return iou


box1 = [2, 1, 5, 5]
box2 = [3, 2, 6, 6]
iou = calculate_iou(box1, box2)
print(f"The Intersection over Union (IoU) between {box1} and {box2} is {iou}.")

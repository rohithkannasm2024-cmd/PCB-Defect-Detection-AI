import os
import shutil
import random
import xml.etree.ElementTree as ET

# -------------------------------
# CHANGE THIS PATH IF REQUIRED
# -------------------------------
dataset_root = "dataset/PCB_DATASET"

image_root = os.path.join(dataset_root, "images")
annotation_root = os.path.join(dataset_root, "Annotations")

output_root = "dataset_yolo"

classes = [
    "missing_hole",
    "mouse_bite",
    "open_circuit",
    "short",
    "spur",
    "spurious_copper"
]

# Create folders
for split in ["train", "valid", "test"]:
    os.makedirs(os.path.join(output_root, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_root, split, "labels"), exist_ok=True)


def convert_box(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]

    xmin, ymin, xmax, ymax = box

    x = ((xmin + xmax) / 2.0) * dw
    y = ((ymin + ymax) / 2.0) * dh
    w = (xmax - xmin) * dw
    h = (ymax - ymin) * dh

    return x, y, w, h


image_files = []

for defect in os.listdir(image_root):

    img_folder = os.path.join(image_root, defect)
    ann_folder = os.path.join(annotation_root, defect)

    for img in os.listdir(img_folder):

        if not img.endswith(".jpg"):
            continue

        image_files.append((defect, img))

random.shuffle(image_files)

total = len(image_files)

train_end = int(0.7 * total)
valid_end = int(0.85 * total)

splits = {
    "train": image_files[:train_end],
    "valid": image_files[train_end:valid_end],
    "test": image_files[valid_end:]
}

for split in splits:

    for defect, img in splits[split]:

        img_path = os.path.join(image_root, defect, img)

        xml_path = os.path.join(
            annotation_root,
            defect,
            img.replace(".jpg", ".xml")
        )

        tree = ET.parse(xml_path)
        root = tree.getroot()

        size = root.find("size")
        w = int(size.find("width").text)
        h = int(size.find("height").text)

        label_lines = []

        for obj in root.iter("object"):

            cls = obj.find("name").text.lower()

            cls_id = classes.index(cls)

            xmlbox = obj.find("bndbox")

            xmin = float(xmlbox.find("xmin").text)
            ymin = float(xmlbox.find("ymin").text)
            xmax = float(xmlbox.find("xmax").text)
            ymax = float(xmlbox.find("ymax").text)

            bb = convert_box((w, h), (xmin, ymin, xmax, ymax))

            label_lines.append(
                f"{cls_id} {' '.join(str(round(a,6)) for a in bb)}"
            )

        shutil.copy(
            img_path,
            os.path.join(output_root, split, "images", img)
        )

        with open(
            os.path.join(
                output_root,
                split,
                "labels",
                img.replace(".jpg", ".txt")
            ),
            "w"
        ) as f:

            f.write("\n".join(label_lines))

print("Dataset Converted Successfully!")
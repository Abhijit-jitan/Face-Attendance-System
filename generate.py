## generate.py

"""NOTE:
    - Collect images with labels in it
    - store them to Input_images folder
    - Run generate.py to create known faces-encoding & label for further process
"""

import cv2
import numpy as np
import os
import face_recognition as fr


def generate(path):
    """ Takes images-path(with names) & makes known-face database(extracts labels from image , extract faces encodings) & Also stores labels & face-encodings to '.npy' file """
    labels, encodings = [], []

    if len(os.listdir(path)) != 0:
        # print("Found {} images ")
        for image in os.listdir(path):
            if image.endswith(".jpg") or image.endswith(".png"):
                img = cv2.imread(os.path.join(path, image))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR to RGB channel format
                encode = fr.face_encodings(img)[0]  # extract face encodings from image
                encodings.append(encode)
                labels.append(os.path.splitext(image)[0])  # list of known-labels

        ## convert & store, names & face encodings to ".npy"
        np.save(r"Backend\known_faces_database\known_face_encodings.npy", encodings)
        np.save(r"Backend\known_faces_database\known_face_labels.npy", labels)
        print("'known_face_labels.npy' & 'known_face_encodings.npy' generated successfully .....")

    elif len(os.listdir(path)) == 0:
        print("Please Ensure that, you have some images to Process !!!!")


path = r"Input_images"
generate(path)

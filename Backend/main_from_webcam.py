## Backend\\main_from_webcam.py

import numpy as np
import cv2, datetime
import face_recognition as fr
import utils

# Load Known face-encodings & labels
known_encodings = np.load(r"known_faces_database\known_face_encodings.npy")  # load stored face-encodings
known_labels = np.load(r"known_faces_database\known_face_labels.npy")        # load stored labels
threshold_in_time = datetime.datetime.strptime("23:30:00", '%H:%M:%S')  # threshold In-time

## live
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    resized_img = cv2.resize(img, (0, 0), None, 0.5, 0.5)  # resized images
    resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)  # BGR to RGB

    # Extract face-encoding from test-image
    face_loc = fr.face_locations(resized_img)  # detect all faces-location in frame
    test_face_encode = fr.face_encodings(resized_img, face_loc)  # face encodings on frame

    # Compare test-face-encoding with known-face-encoding
    for encode_face, face_location in zip(test_face_encode, face_loc):
        matches = fr.compare_faces(known_encodings,encode_face)  # compares new-face-encodeing with known-faces-encodings(returns Boolean value for each [label])
        face_distance = fr.face_distance(known_encodings,encode_face)  # compares frame face-distance to known-faces-distance
        match_id = np.argmin(face_distance)  # index of best matching label_index

        if matches[match_id]:  # If known-face matches to face in frame
            name = known_labels[match_id].title()
            print("Matched With '{}'".format(name))
            utils.csv_writer(name, threshold_in_time)
        else:
            print("No Match Found")

    cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
#cv2.destroyAllWindows()



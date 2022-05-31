# Backend\\main_from_img_dir.py
"""Note:
    - Uses image path to Append in Attendance-Sheet
"""

import numpy as np
import cv2, datetime
import face_recognition as fr
import utils

def get_attendance_from_image(path, threshold_in_time):
    """ Takes Image path => Preprocess => extract-face-encoding => compare with known face encodings => retun match & Append to csv """

    # Load Known face-encodings & labels
    known_encodings = np.load(r"known_faces_database\known_face_encodings.npy")  # load stored face-encodings
    known_labels = np.load(r"known_faces_database\known_face_labels.npy")  # load stored labels

    # Preprocess test-image
    img = cv2.imread(path)
    resized_img = cv2.resize(img, (0, 0), None, 0.5, 0.5)  # resized images
    resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)  # BGR to RGB

    # Extract face-encoding from test-image
    face_loc = fr.face_locations(resized_img)  # detect all faces-location in frame
    test_face_encode = fr.face_encodings(resized_img, face_loc)  # face encodings on frame

    # Compare test-face-encoding with known-face-encoding
    for encode_face, face_location in zip(test_face_encode, face_loc):
        matches = fr.compare_faces(known_encodings,
                                   encode_face)  # compares new-face-encodeing with known-faces-encodings(returns Boolean value for each [label])
        face_distance = fr.face_distance(known_encodings,
                                         encode_face)  # compares frame face-distance to known-faces-distance
        match_id = np.argmin(face_distance)  # index of best matching label_index

        if matches[match_id]:  # If known-face matches to face in frame
            name = known_labels[match_id].title()
            print("Matched With '{}'".format(name))
            utils.csv_writer(name, threshold_in_time)
        else:
            print("No Match Found")


##
test_img_path = r"..\test data\t1.jpg"
threshold_in_time = datetime.datetime.strptime("23:30:00", '%H:%M:%S')  # threshold In-time

get_attendance_from_image(test_img_path, threshold_in_time)
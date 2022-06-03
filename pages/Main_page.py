import numpy as np
import streamlit as st
import face_recognition,datetime,cv2
from Backend import utils

def app():
    threshold_in_time = datetime.datetime.strptime("21:30:00", '%H:%M:%S')  ### UI Part

    ## head
    head = st.container()

    with head:
        st.title("Face Attendance System")
        ## Show date in UI

    ## Load trained encodings & labels(known face-encoding & labels)
    known_encodings = np.load(r"Backend\known_faces_database\known_face_encodings.npy")  # load stored face-encodings
    known_labels = np.load(r"Backend\known_faces_database\known_face_labels.npy")  # load stored labels

    ##########################################
    ######## live(webcam feed)
    st.subheader("Open Webcam")
    live = st.container()
    with live:
        run = st.checkbox("Run")
        if run:
            st.success("Webcam On")
        FRAME_WINDOW = st.image([])
        cap = cv2.VideoCapture(0)
        while run:
            success, img = cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR to RGB
            FRAME_WINDOW.image(img)

            video_frame = face_recognition.face_locations(img)  # detect all faces on frame
            encode_frame = face_recognition.face_encodings(img, video_frame)  # face encodings on frame
            for encode_face, face_location in zip(encode_frame, video_frame):
                matches = face_recognition.compare_faces(known_encodings,encode_face)  # compares frame face-encodeing to known-faces-encodings
                face_distance = face_recognition.face_distance(known_encodings,encode_face)  # compares frame face-distance to known-faces-distance
                match_id = np.argmin(face_distance)  # index of best matching label_index

                if matches[match_id]:  # If known-face matches to face in frame
                    name = known_labels[match_id]  # .title()
                    attendance = utils.csv_writer(name,threshold_in_time)  # append,returns [Id_names,entry_time,attendance_status] of known-faces
                    st.write("{} Added Successfully !!!".format(name))
                else:
                    st.write("Not sure about your face, Try Again Later !!!!")

        else:
            st.warning("Webcam Stopped")



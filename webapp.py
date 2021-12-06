import numpy as np
import streamlit as st
import face_recognition
import cv2
import utils
import os
import datetime

### UI Part

## head
head=st.container()
with head:
    st.title("Face Attendance System")
    dt=datetime.datetime.now()
    st.write("Date : {}--{}".format(dt.strftime("%d %B %Y"),dt.strftime('%I:%M:%S %p')))

## Load trained encodings & labels(known face-encoding & labels)
known_encodings=np.load("known_face_encodings.npy")   # load stored face-encodings
known_labels=np.load("known_face_labels.npy")         # load stored labels

## live(webcam feed)
st.subheader("Open Webcam")
live=st.container()
with live:
    run=st.checkbox("Run")
    FRAME_WINDOW=st.image([])
    cap=cv2.VideoCapture(0)
    while run:
        success,img=cap.read()
        #resized_img=cv2.resize(img,(0,0),None,0.5,0.5)   # resized images
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # BGR to RGB
        FRAME_WINDOW.image(img)

        video_frame=face_recognition.face_locations(img)  # detect all faces on frame
        encode_frame=face_recognition.face_encodings(img,video_frame)  # face encodings on frame
        for encodeface,face_location in zip(encode_frame, video_frame):
            matches=face_recognition.compare_faces(known_encodings,encodeface)        # compares frame face-encodeing to known-faces-encodings
            face_distance=face_recognition.face_distance(known_encodings,encodeface)  # compares frame face-distance to known-faces-distance
            match_id=np.argmin(face_distance)  # index of best matching label_index

            if matches[match_id]:  # If known-face matches to face in frame
                name=known_labels[match_id].title()
                # date = date.today();date.strftime("%d/%m/%y")
                attendance_sheet=utils.attendance_writer(name)
            else:
                st.write("Not sure about your face !!!!")
    else:
        st.write("stopped")


## Attendance generate
st.subheader("Generate Attendance-Sheet DataFrame")
generate=st.container()
with generate:
    to_df=st.button('Generate')    # write to dataframe
    if to_df:
        #df=utils.write_dataframe(attendance_sheet)
        st.write("Written Successfully...")

    show_df=st.button('Show')  # Show generated df
    if show_df:
        st.write("Generated Attendance Sheet")
        #st.write(df)
    ## code for generate dataframe to other format

import numpy as np
import face_recognition as fr
import cv2
import utils
import os

known_encodings=np.load(r"D:\Projects\face attendance system\known_face_encodings.npy") # load stored face-encodings
known_labels=np.load(r"D:\Projects\face attendance system\known_face_labels.npy") # load stored labels

## live
cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    resized_img=cv2.resize(img,(0,0),None,0.5,0.5)  # resized images
    resized_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # BGR to RGB

    video_frame=fr.face_locations(resized_img)  # detect all faces on frame
    encode_frame=fr.face_encodings(resized_img,video_frame)  # face encodings on frame

    for encodeface,face_location in zip(encode_frame,video_frame):
        matches=fr.compare_faces(known_encodings,encodeface)  # compares frame face-encodeing to known-faces-encodings
        face_distance=fr.face_distance(known_encodings,encodeface)  # compares frame face-distance to known-faces-distance
        match_id=np.argmin(face_distance)  # index of best matching label_index

        if matches[match_id]:  # If known-face matches to face in frame
            name=known_labels[match_id].title()
            #date = date.today();date.strftime("%d/%m/%y")
            attendance_sheet=utils.attendance_writer(name)
        else:
            print("Not sure about your face !!!!")

    cv2.imshow('Output',img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



df=utils.write_dataframe(attendance_sheet)
print(df)


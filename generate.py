## import libraries
import cv2
import os
import face_recognition as fr
import numpy as np

# keep all known images to 'known_faces' file to generate 'labels' & 'face-encodings'
path=r'D:\Projects\face attendance system\known_faces'
def generate(path):
    """ Takes directory-path & extracts labels form image , extract faces encodings, Also stores labels & face-encodings to '.npy' file  """
    labels,encodings=[],[]
    image_list=os.listdir(path)     ## list of all images to be trained
    print("please, wait a moment.....")

    for image in image_list:
        img=cv2.imread(os.path.join(path,image))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)     # BGR to RGB channel format
        encode = fr.face_encodings(img)[0]
        encodings.append(encode)
        labels.append(os.path.splitext(image)[0])   # list of known-labels


    ## write & store to .npy file
    np.save(os.path.join(os.getcwd(),"known_face_encodings.npy"),encodings)
    np.save(os.path.join(os.getcwd(),"known_face_labels.npy"),labels)
    print("'known_face_labels.npy' & 'known_face_encodings.npy' generated successfully .....")


generate(path)
import cv2
import numpy as np
import os 
import face_recognition as fr
#import tqdm

# keep all known images to 'known_faces' file to generate 'labels' & 'face-encodings'

def generate(path):
    """ Takes images-path(with names) & makes known-face database(extracts labels from image , extract faces encodings) & Also stores labels & face-encodings to '.npy' file """
    labels,encodings=[],[]
    for image in os.listdir(path):
        img=cv2.imread(os.path.join(path,image))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                 # BGR to RGB channel format
        encode = fr.face_encodings(img)[0]                      # extract face encodings from image
        encodings.append(encode)
        labels.append(os.path.splitext(image)[0])               # list of known-labels

    ## convert & store, names & face encodings to ".npy"
    np.save(r"known_face_encodings.npy",encodings)
    np.save(r"known_face_labels.npy",labels)
    print("'known_face_labels.npy' & 'known_face_encodings.npy' generated successfully .....")

path=r"images"
generate(path)

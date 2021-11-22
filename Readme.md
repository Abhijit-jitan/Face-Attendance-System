## Goal:


## Working:
``Mainly it compares trained-face-encodings to new detected face-encodings & if it matched(similar distance between face-landmarks), then attendance & in-time recored`` 

## Steps:
 * Download repository to local machine 
 * Place training-images to ``face attendance system\Known_faces`` directory
 * Run ``generate.py``, it will generate ``known_face_encodings.npy(face-encoding array)`` & ``known_face_label.npy(labels)``
 * Run ``main.py`` to switch-on webcam,then newly detected face-encodings compared with trained-face-encoding 
 * If face-matched,then attendance & in-time added to attendance-sheet(pandas DataFrame) 

## Use-cases:
 * Better & Automated approach for Attendence System(In any sector)
 * Better Product recommendations to known-persons in stores
 *   

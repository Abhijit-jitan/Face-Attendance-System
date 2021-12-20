## Goal:
  **I ve tried ``Contactless`` & ``Automated`` approach  to replace ``biometric Attendance System``**

## Use-cases:
 * Better & Automated approach for Attendence System(In any sector)
 * Better Product recommendations to known-persons in stores
 *   


## Working:
``Mainly it compares trained-face-encodings to new detected face-encodings & if it matched(similar distance between face-landmarks), then attendance & in-time recored`` 

## Steps:
 * Download repository to local machine 
 * Place training-images to ``face attendance system\Known_faces`` directory
 * Run ``generate.py``, it will generate ``known_face_encodings.npy(face-encoding array)`` & ``known_face_label.npy(labels)``
 * Run ``main.py`` to switch-on webcam,then newly detected face-encodings compared with trained-face-encoding 
 * If face-matched,then attendance & in-time added to attendance-sheet(pandas DataFrame) 


## Evolution:
 * **Version_1:** Explicitly training known faces & directly test them
 * **Version_2:** Used "Streamlit" to develop "GUI" & used ".npy" file for train model(replacement of explicitly training) 
 * **Version_3:** Used "Streamlit" to develop "GUI" & used "generate.py" script to generate "(known_face & known_label files).npy"
 * **Version_4:** Used "threshold-time" to check is the entry-time is late|in-time & write attendance to ".CSV" file   


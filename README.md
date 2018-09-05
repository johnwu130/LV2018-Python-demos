# LV2018-Python-demos
These are some demos for the LV2018 Python Node.

Needed Software:

LabVIEW 2018, 64-bit recommended

Python 3.5 or 3.6, 64-bit recommended (32-bit or 64-bit needs to match LabVIEW)
Python packages:
-Numpy
-OpenCV
-speech_recognition

1. Basic Math
Adds 2 floats in Python, return output to LabVIEW.
2. Calling a cloud service
Call the google speech recognition API, and recognizes speech from wav file.
3. Face tracking with OpenCV
Save webcam images to jpg, use OpenCV to detect faces, and return face coordinates to LabVIEW

*Note: Demo 2 and 3 uses LabVIEW to save temporary audio and image files to disk.  The default temp dir is D:\, because C:\ may be write-protected.  If the demo doesn't work, be sure to change the temp dir to a directory that has access permission. 

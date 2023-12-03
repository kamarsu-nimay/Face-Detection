# Face-Detection
This project can be used to detect the faces present in a picture or on a live webcam

## Getting Started
1. Clone the repo to you system:
   ```
   git clone https://github.com/nimay-kamarsu/Face-Detection.git
   ```
2. Install the required libraries:
   ```
   pip install opencv-python
   ```

## Run the Program
* After cloning and installing the required libraries, run the program in an IDE of you choice. If there's any error while running the program check whether the installed libraries is the latest verion. If not update the library.
  ```
  python main.py
  ```

## System Design
1. This program is designed using OpenCV api which comes with pre-trained models for face detection.
2. It is designed that the program takes input from the user to detect the face either from the live webcam or an image available in the device.
3. While the webcam is turned on immediately after input command, the path of the image in the device should be given to detect the face.

import cv2

def detect_faces(image_path=None):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if image_path is None:
        # Using a live webcam for detection
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            # Convert the frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecting faces in the frame
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the result
            cv2.imshow('Detected Faces', frame)

            # Press 'ESC' key to break the loop
            if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for 'ESC' key
                break

        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()

    else:
        # Using a provided image for detection
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the result
        cv2.imshow('Detected Faces', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# User choice: Enter '1' for live webcam and '2' for image file
user_choice = input("Choose an option:\n1. Live Webcam\n2. Image from Device\nEnter choice (1/2): ")

if user_choice == '1':
    detect_faces()
elif user_choice == '2':
    image_path = input("Enter the path of the image file: ")
    detect_faces(image_path)
else:
    print("Invalid choice. Please choose either '1' or '2'.")

import cv2
import easyocr

# Initialize cascade classifier
numberPlate_cascade = "numberplate_haarcade.xml"
detector = cv2.CascadeClassifier(numberPlate_cascade)

# Initialize the easyocr Reader object
reader = easyocr.Reader(['en'])

# Open video capture
video_path = r'F:\Traffic violation.mp4'
cap = cv2.VideoCapture(video_path)

# Create video writer
output_path = 'output.avi'
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while cap.isOpened():
    # Read frame from video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect number plates
    plates = detector.detectMultiScale(frame_gray, scaleFactor=1.05, minNeighbors=7,
                                       minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Iterate through each detected number plate
    for (x, y, w, h) in plates:
        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the number plate
        plateROI = frame_gray[y:y + h, x:x + w]
        cv2.imwrite("numberplate.jpg", plateROI)

        # Detect text
        text = reader.readtext(plateROI)

        if len(text) == 0:
            continue
        print(text)
        print(text[0][1])

        # Draw text on the frame
        cv2.putText(frame, text[0][1], (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    # Write frame to output video
    out.write(frame)

# Release video capture and writer
cap.release()
out.release()

print("Video processing complete.")

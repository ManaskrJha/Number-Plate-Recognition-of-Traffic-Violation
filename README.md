# Number Plate Recognition of Traffic Violation from a Video

This project implements number plate recognition in a video using OpenCV and EasyOCR. It detects and extracts number plates from each frame of the video, performs optical character recognition (OCR) on the extracted plates and displays the recognized text on the frames.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction
Number plate recognition is an important task in various applications such as traffic monitoring, parking management, and law enforcement. This project utilizes computer vision techniques to detect and recognize number plates in a video. It makes use of the Haar cascade classifier from OpenCV for number plate detection and EasyOCR for text recognition.

The process involves the following steps:
1. Initialize the cascade classifier using the pre-trained XML file for number plate detection.
2. Initialize the EasyOCR reader object for text recognition.
3. Open the video capture and create a video writer to save the processed frames.
4. Read each frame from the video.
5. Convert the frame to grayscale for better processing.
6. Detect number plates using the cascade classifier.
7. Iterate through each detected number plate.
8. Draw a bounding box around the number plate on the frame.
9. Crop the number plate region from the frame.
10. Perform OCR on the cropped number plate image using EasyOCR.
11. Retrieve the recognized text from the OCR result.
12. Display the recognized text on the frame.
13. Write the processed frame to the output video.
14. Release the video capture and video writer.
15. Print a message indicating the completion of video processing.

## Installation
To run this project, you need to have the following dependencies installed:
- OpenCV: Install OpenCV using the command `pip install opencv-python`.
- EasyOCR: Install EasyOCR using the command `pip install easyocr`.

## Usage
1. Clone the repository: `git clone https://github.com/example/repo.git`.
2. Navigate to the project directory: `cd repo`.
3. Place the `numberplate_haarcade.xml` file in the same directory as the script.
4. Set the `video_path` variable in the script to the path of the input video file.
5. Set the `output_path` variable in the script to the desired path for the output video file.
6. Run the script: `python number_plate_recognition.py`.
7. After the script finishes, the output video with the recognized number plates will be saved to the specified `output_path`.

## Contributing
Contributions to this project are welcome. You can contribute by adding new features, improving the existing code, or fixing any issues. To contribute, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push the changes to your fork: `git push origin feature-name`.
5. Submit a pull request.



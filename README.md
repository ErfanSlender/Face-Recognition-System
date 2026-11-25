# Face Recognition & Attendance System

A python-based face recognition system using:

- Python
- OpenCV
- Face Recognition
- NumPy
- SQLite

## Features

- Real-time face recognition
- Multiple known faces
- Face Matching
- SQLite database intergration
- Automatic attendance logging
- 30-second logging interval per person

## Project Structure

FaceRecognitionSystem/
│
├─ known/
├─ database.py
├─ recognizer.py
├─ config.py
├─ main.py
├─ requirements.txt
├─ test_dlib_image.py
└─ README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run

python main.py

## Privacy

Face images and biometric data are stored locally.
Do not upload personal face images or database to GitHub.
Only use images with tthe subject' consent.
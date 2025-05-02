# OCR Text Detection Application

This Streamlit application allows you to detect text from both live video feed and uploaded images using OCR (Optical Character Recognition) powered by Tesseract and OpenCV.

## Features

- Live video feed text detection
- Image upload and text detection
- Real-time OCR processing
- Clean and intuitive user interface

## Prerequisites

1. Python 3.7 or higher
2. Tesseract OCR installed on your system:
   - Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - Mac: `brew install tesseract`

## Installation

1. Clone this repository
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Choose between Live Video or Image Upload mode using the sidebar
3. For Live Video:
   - Click 'Start/Stop Video' to begin/end video capture
   - Text will be detected in real-time
4. For Image Upload:
   - Upload an image file (jpg, jpeg, png)
   - Text will be detected automatically

## Dependencies

- streamlit==1.32.0
- opencv-python==4.9.0.80
- pytesseract==0.3.10
- numpy==1.26.4
- Pillow==10.2.0

## Notes

- The application uses Tesseract OCR for text detection
- Image preprocessing is applied to improve OCR accuracy
- The live video mode requires a webcam
- For best results, ensure good lighting and clear text in the images/video 
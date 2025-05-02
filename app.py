import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
import tempfile
import os

# Configure Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set page config
st.set_page_config(
    page_title="OCR Text Detection",
    page_icon="📝",
    layout="wide"
)

# Title and description
st.title("📝 OCR Text Detection")
st.write("""
This application can detect text from:
1. Live video feed from your webcam
2. Uploaded images
""")

# Sidebar for mode selection
mode = st.sidebar.radio(
    "Select Input Mode:",
    ["Live Video", "Image Upload"]
)

# Function to perform OCR on an image
def perform_ocr(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # Perform OCR
    text = pytesseract.image_to_string(thresh)
    return text

# Live Video Mode
if mode == "Live Video":
    st.header("Live Video OCR")
    st.write("Click the button below to start/stop mbg the video feeding")
    
    # Initialize session state for video capture
    if 'run' not in st.session_state:
        st.session_state.run = False
    
    # Button to start/stop video
    if st.button('Start/Stop Video'):
        st.session_state.run = not st.session_state.run
    
    # Video capture
    if st.session_state.run:
        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        
        while st.session_state.run:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access webcaming")
                break
            
            # Convert frame to RGB for display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Perform OCR on the frame
            text = perform_ocr(frame)
            
            # Display the frame and detected text
            frame_placeholder.image(frame_rgb, channels="RGB")
            st.text_area("Detected Text:", text, height=100)
            
            # Add a small delay to prevent high CPU usage
            cv2.waitKey(1)
        
        cap.release()

# Image Upload Mode
else:
    st.header("Image Upload OCR")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        
        # Convert to BGR for OpenCV
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Perform OCR
        text = perform_ocr(image_bgr)
        
        # Display the detected text
        st.text_area("Detected Text:", text, height=200)

# Add some instructions in the sidebar
st.sidebar.markdown("""
### Instructions:
1. For Live Video:
   - Click 'Start/Stop Video' to begin/end video capture
   - Text will be detected in real-time
   
2. For Image Upload:
   - Upload an image file (jpg, jpeg, png)
   - Text will be detected automatically
""")

# Note about Tesseract installation
st.sidebar.markdown("""
### Note:
Make sure Tesseract OCR is installed on your system:
- Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux: `sudo apt-get install tesseract-ocr`
- Mac: `brew install tesseract`
""") 
import streamlit as st
from PIL import Image
import torch
import torch.nn as nn
from torchvision import transforms
import joblib
import torchvision.models as models




############################################################################################################
############################################################################################################

# Inject custom CSS to resize the file uploader
st.markdown(
    """
    <style>
    h1 {
        font-size: 40px; /* Adjust the font size */
        text-align: left; /* Align text in the uploader to the center */
        
    }
    /* Uploader container */
    .stFileUploader {
        
        max-width: 370px; /* Set the desired width */
        text-align: center; /* Align text in the uploader to the center */
        font-size: 20px; /* Set the desired font size */
    }
    /* Input element */
    .stFileUploader > div {
        max-width: 300px; /* Restrict the width of the upload area */
        font-size: 10px;  /* Adjust font size if necessary */
        text-align: center; /* Align text in the uploader to the center */
    }
    /* Button */
    .stFileUploader button {
        padding: 5px 10px; /* Smaller padding for the button */
        font-size: 12px;   /* Smaller font size */
        text-align: center; /* Align text in the uploader to the center */

    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Upload your image")

# File uploader with custom size
uploaded_file = st.file_uploader(" ", type=["jpg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=" ", width=300)
    st.markdown("""
    <style>
    .custom-text {
        position: absolute;
        top: -700px; /* Adjust as needed */
        left: 500px; /* Adjust as needed */
        font-size: 40px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    <div class="custom-text">
        Image Attributes:
    </div>
    """, unsafe_allow_html=True)


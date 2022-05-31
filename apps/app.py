import streamlit as st
#from webcam import webcam
#import cv2
#from streamlit_webrtc import webrtc_streamer
import cv2
#import av #strealing video library
import numpy as np
import torch

st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 

def igen_frames():
    cap = cv2.VideoCapture(cv2.CAP_V4L2) #resolved, correct position

for i in range(0, 50):
    ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#img_file = st.camera_input()
#if img_file is not None:
#    st.image(img_file)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

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

run = st.checkbox('모니터링 시작')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(-1)

frames = []
if camera.isOpened():
    for i in range(0, 50):
        ret, frame = camera.read()
        if frame is not None: 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
            frames.append(frame)

#img_file = st.camera_input()
#if img_file is not None:
#    st.image(img_file)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

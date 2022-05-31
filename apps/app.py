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

@st.cache(allow_output_mutation=True)
def get_cap():
        return cv2.VideoCapture(0)

cap = get_cap()

frameST = st.empty()

if captured_image is None:
    st.write("Waiting for capture...")

while True:
    ret, frame = cap.read()
        
    if not ret:
        cv2.waitKey(3000)
        cap.release()
        break
    frameST.image(frame, channels="BGR")

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

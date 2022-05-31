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

@st.cache(allow_output_mutation=True)
def get_cap():
    return cv2.VideoCapture(0)

cap = get_cap()

FRAME_WINDOW = st.empty()

while run:
    ret, frame = cap.read()      
    if ret:
        cap.release()
        break
        
    FRAME_WINDOW.image(frame)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

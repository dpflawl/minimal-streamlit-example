import streamlit as st
import cv2
import torch

st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 
run = st.checkbox('모니터링 시작')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(CAP_V4L2)

count = 0
while run:
    _, frame = camera.read()
    if frame is not None: 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        break
    count += 1
    if count == 91:
        break
else:
    st.write(' ') #st.write('모니터링 중지')
        
#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

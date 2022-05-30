import streamlit as st
import cv2
import joblib

st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 
run = st.checkbox('모니터링 시작')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write(' ') #st.write('모니터링 중지')

#머신러닝으로 저장된 모델을 호출하고 st로 부터 받은 값으로 예측한다.
loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")

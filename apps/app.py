import cv2
import streamlit as st

st.title("얼굴 영상을 이용하여 심박수 측정 🙌👩‍💻👏")
run = st.checkbox('심박 모니터링 시작')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

#머신러닝으로 저장된 모델을 호출하고 st로 부터 받은 값으로 예측한다.
#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/regression_model.pkl")

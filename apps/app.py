import streamlit as st
from threading import Thread
import cv2 as cv
import time

st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 

@st.cache(allow_output_mutation=True)
def get_cap():
    return cv.VideoCapture(0)

cap = get_cap()

frameST = st.empty()
param=st.sidebar.slider('chose your value')

while True:
    ret, frame = cap.read()
    # Stop the program if reached end of video
    if not ret:
        print("Done processing !!!")
        cv.waitKey(3000)
        # Release device
        cap.release()
        break

    frameST.image(frame, channels="BGR")

#img_file = st.camera_input()
#if img_file is not None:
#    st.image(img_file)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
#loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

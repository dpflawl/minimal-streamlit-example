st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 

import streamlit as st
from threading import Thread
import cv2
import time

cap = cv2.VideoCapture(0)
frameST = st.empty()
param = st.sidebar.slider('choose your value')

stopper_started = False
while True:
    success, frame = cap.read()
    if not success: break

    frameST.image(frame, channels="BGR")
    updated_time = time.time()

    if not stopper_started:
        #this block executes for once with every
        #streamlit re-run command
        def stopper(self):
            while True:
                try:
                    #if time difference increases this thread will be terminated
                    time_diff = round(time.time() - updated_time)
                    if time_diff >1: #1 second
                        print("Done processing !!!")
                        print("Releasing VideoCapture")
                        #if streamlit ui is stopped
                        #time gap will increase
                        #hence releasing camera resource
                        cap.release()
                        break
                except: pass
        th = Thread(target=stopper, args=(0,))
        th.daemon = True
        th.start()
        stopper_started = True

#img_file = st.camera_input()
#if img_file is not None:
#    st.image(img_file)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

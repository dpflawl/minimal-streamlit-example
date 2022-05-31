import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("얼굴로부터 심박수를 추정하는 심박 모니터링 서비스 Demo 📷💓")
st.write("👩‍💻 Developed by 지예림") 

webrtc_streamer(key="example")

#img_file = st.camera_input()
#if img_file is not None:
#    st.image(img_file)

#loaded_model = joblib.load("/app/minimal-streamlit-example/apps/PhysNet_v5.pkl")
#loaded_model = torch.load('/app/minimal-streamlit-example/apps/model_90.pt', encoding='ascii')

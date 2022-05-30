
#streamlit 라이브러리를 불러오기
import streamlit as st
#AI모델을 불러오기 위한 joblib 불러오기
import joblib
import pandas as pd

# st를 이용하여 타이틀과 입력 방법을 명시한다.

st.title('차량 속도에 따른 납부보험료 예측서비스')
st.subheader('(1) 아래에 당신 차의 평균 속도를 입력해주세요!!!')

values = st.slider('평균속도 입력하세요', 0, 200)  # st.number_input("평균속도")
st.write('평균속도:', values)

#머신러닝으로 저장된 모델을 호출하고 st로 부터 받은 값으로 예측한다.
loaded_model = joblib.load("regression_model.pkl")
new_x = [values]
df_new_x = pd.DataFrame(new_x)
new_y = loaded_model.predict(df_new_x )

#예측결과를 화면에 뿌려준다. 
st.subheader('(2) 속도에 따른 당신이 납부해야할 보험료는 다음과 같습니다.')
st.write('예상되는 납부보험료:', new_y[0])

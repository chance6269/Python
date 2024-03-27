# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:20:25 2024

@author: jcp
"""

# 기본 버튼 입력 예제

import streamlit as st

# session 처리
if st.session_state:
    cnt_session = st.session_state['cnt']
    cnt_session += 1
    st.session_state['cnt'] = cnt_session
    print('기본 버튼 입력 예제: cnt =',cnt_session)    
else:
    st.session_state['cnt'] = 0
    cnt_session = st.session_state['cnt']

#
st.title("스트림릿의 버튼 입력 사용 예")
st.header("버튼 클릭 회수: {0}".format(cnt_session))

clicked = st.button('버튼 1')
st.write('버튼 1 클릭 상태:', clicked)

if clicked:
     st.write('버튼 1을 클릭했습니다.' )
else:
     st.write('버튼 1을 클릭하지 않았습니다.' )
        
clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태:', clicked)

if clicked:
     st.write('버튼 2를 클릭했습니다.' )
else:
     st.write('버튼 2를 클릭하지 않았습니다.' )

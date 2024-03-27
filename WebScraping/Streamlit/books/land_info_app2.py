# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:05:37 2024

@author: jcp
"""

import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 원본 DataFrame의 제목 열에 있는 문자열을 분리해 
# 전국, 서울, 수도권의 매매가 변화율 열이 있는 DataFrame 반환하는 함수
def split_title_to_rates(df_org):
    df_new = df_org.copy()

    df_temp = df_new['제목'].str.replace('%', '') # 제목 문자열에서 % 제거
    df_temp = df_temp.str.replace('보합', '0')    # 제목 문자열에서 보합을 0으로 바꿈
    df_temp = df_temp.str.replace('보합세', '0')  # 제목 문자열에서 보합세를 0으로 바꿈
    
    regions = ['전국', '서울', '수도권']    
    for region in regions:
        df_temp = df_temp.str.replace(region, '') # 문자열에서 전국, 서울, 수도권 제거

    df_temp = df_temp.str.split(']', expand=True) # ]를 기준으로 열 분리
    df_temp = df_temp[1].str.split(',', expand=True) # ,를 기준으로 열 분리
    
    df_temp = df_temp.astype(float)
    
    df_new[regions] = df_temp # 전국, 서울, 수도권 순서대로 DataFrame 데이터에 할당

    return df_new[['등록일'] + regions + ['번호']] # DataFrame에서 필요한 열만 반환

# %%

# df_rate = split_title_to_rates(df) # split_title_to_rates() 함수 호출
# %%
checked_1 = st.sidebar.checkbox('전국')
checked_2 = st.sidebar.checkbox('서울')
checked_3 = st.sidebar.checkbox('수도권')

clicked = st.sidebar.button('부동산 데이터 가져오기')

if(clicked==True):
    st.subheader("아파트의 매매가 변화율 데이터")
    
    base_url = "https://land.naver.com/news/trendReport.naver"

    df_rates = pd.DataFrame() # 전체 데이터가 담길 DataFrame 데이터
    last_page_num = 8 # 가져올 데이터의 마지막 페이지 

    for page_num in range(1, last_page_num+1):

        url = f"{base_url}?page={page_num}"
        dfs = pd.read_html(url)

        df_page = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음
        df_rate = split_title_to_rates(df_page)
        
        # 세로 방향으로 연결 (기존 index를 무시)
        df_rates = pd.concat([df_rates, df_rate], ignore_index=True) 

    # 최신 데이터와 과거 데이터의 순서를 바꿈. index도 초기화함  
    df_rates_for_chart = df_rates[::-1].reset_index(drop=True)
    
    selected_regions = []
    
    if(checked_1):
        selected_regions.append('전국')
    if(checked_2):
        selected_regions.append('서울')
    if(checked_3):
        selected_regions.append('수도권')
        
    if(selected_regions == []):
        st.subheader("지역을 선택하세요.")
    else:
        st.dataframe(df_rates[['등록일']+selected_regions].head())
        
        
        mpl.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 폰트 설정 
        mpl.rcParams['axes.unicode_minus'] = False # 마이너스(-) 폰트 깨짐 방지
        
        ax = df_rates_for_chart.plot(x='등록일', y=selected_regions, figsize=(15, 6),
                                     style = '-o', grid=True)
        
        ax.set_title("아파트 매매가 변화율", fontsize=30)
        ax.set_xlabel("날짜", fontsize=20)
        ax.set_ylabel("변화율", fontsize=20)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        fig = ax.get_figure()
        st.pyplot(fig)
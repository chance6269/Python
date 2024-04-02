# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:54:45 2024

@author: pjc62
"""

# 05 데이터 시각화하기

# 학습목표 : 
    # 맷플롯립 사용법 배우기
    # 선 그래프, 막대 그래프 그려보기
    
# 05-1 맷플롯립 기본 요소 알아보기

# 그래프 크기를 좀더 키우고, 산점도를 동그라미 대신 별 모양으로 그려라

# 피겨, rcParams, 서브플롯

# Figure 객체 :
    # 모든 그래프 구성 요소를 담고 있는 최상위 객체
    
# %%
import gdown
gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

# %%

import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()

# %%
# 산점도 그리기
import matplotlib.pyplot as plt

plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()

# %%
# 그래프 크기 바꾸기 : 
# figure() :
    # figsize=( , )
    # 단위는 inch
plt.figure(figsize=(9, 6)) # 너비 9인치, 높이 6인치인 figure 객체 생성
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
# plt.show() 호출시,  figure()로 만들어진 객체는 자동으로 소멸됨.

# %%
# 설치된 맷플롯립 기본 그래프 크기 확인
print(plt.rcParams['figure.figsize'])

# %%
# 그래프 실제 크기 확인하기

# 기본 DPI값 확인
print(plt.rcParams['figure.dpi']) # 72.0

# %%
# 픽셀 크기로 다루려면?
# px / DPI = inch

plt.figure(figsize=(900/72, 600/72)) # 너비 900px, 높이 600px인 figure 객체 생성
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()

# 결과 : 744x484 (1 / 1.2096)배
# 이유는? tight 레이아웃
# %%
# 그래프 크기 바꾸기 : dpi=
plt.figure(dpi=144)
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
# inch당 pixel수가 2배로 늘어나기 때문에 그래프가 2배로 커짐.
# 그래프 안 구성요소들도 함께 커짐.
# 숫자, 마커 크기

# %%
# rcParams 객체 :
    # 맷플롯립 그래픜의 기본값을 관리하는 객체
    
# DPI 기본값 바꾸기
plt.rcParams['figure.dpi'] = 100

# %%
# 산점도 마커 모양 바꾸기

# 마커 기본값 변경하기
# 마커 기본값 확인
plt.rcParams['scatter.marker'] # 'o'
plt.rcParams['scatter.marker'] = '*'

# %%
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()

# %%
# 기본값 변경 없이 마커 바꾸기
# marker=마커모양
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1, marker='+')
plt.show()

# %%
# 여러 개의 서브플롯 출력하기
# 서브플롯 : 
    # Axes 클래스의 객체.
    # 하나의 서브폴롯은 두 개 이상의 Axis(축)을 포함함.
    # 각 축에는 눈금 또는 tick이 표시.
    # label : 축의 이름
    
# %%
# 서브플롯 그리기:
    # subplots(서브플롯 갯수)
    
fig, axs = plt.subplots(2)
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)

axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_yscale('log')

fig.show()
# Figure 객체인 fig에 Axis 객체인 axs[0], axs[1]을 서브플롯으로 추가
# %%
# 크기 조절, 제목 넣기
fig, axs = plt.subplots(2, figsize=(6, 8))

axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
axs[0].set_title('scatter plot')

axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_title('histogram')
axs[1].set_yscale('log')

fig.show()

# %%
# 서브플롯을 가로로 나란히 출력하기
# subplot(행, 열, ...)
# 축 이름 지정 :
    # set_xlabel=
    # set_ylabel=
    
fig, axs = plt.subplots(1,2, figsize=(10,4))

axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
axs[0].set_title('scatter plot')
axs[0].set_xlabel('number of books')
axs[0].set_ylabel('borrow count')

axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_title('histogram')
axs[1].set_yscale('log')
axs[1].set_xlabel('borrow count')
axs[1].set_ylabel('frequency')

fig.show()


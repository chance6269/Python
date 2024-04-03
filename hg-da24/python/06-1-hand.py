# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:26:03 2024

@author: jcp
"""

# 06 복잡한 데이터 표현하기

# 학습 목표:
    # 그래프에 한글을 출력하고 맷플롯립의 객체지향 API를 사용해 그래프를 꾸미는 방법 알아보기
    # 스택 영역 그래프, 스택 막대 그래프, 원 그래프 그리는 방법 배우기
    
# 06-1 객체지향 API로 그래프 꾸미기

# pyplot 방식과 객체지향 API 방식 :
    # pyplot 방식 : matplotlib.pyplot의 함수를 사용하여 그리는 방식
    # 객체지향 API 방식 : Figure 객체와 Subplot 객체를 만들고 그 객체의 메서드를 사용하는 방식
    
# %%
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100

# %%
# pyplot 방식으로 그래프 그리기
# - matplotlib.pyplot 함수들이 하나의 피겨 객체에 대한 상태를 공유
plt.plot([1, 4, 9, 16])
plt.title('simple line graph')
plt.show()

# %%
# 객체지향 API 방식으로 그래프 그리기
fig, ax = plt.subplots() # 하나의 Axes 객체를 가지는 Figure 생성
ax.plot([1,4,9,16])
ax.set_title('simple line graph')
fig.show()
# 간단한 경우 pyplot방식, 복잡한 그래프를 그리는 경우 객체지향 방식을 사용하는 것이 좋다.

# %%
# 그래프에 한글 출력하기
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100
# %%
import matplotlib.font_manager as fm


# font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
font_files = fm.findSystemFonts(fontpaths=['C:/Users/jcp/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
    print(fpath)
    fm.fontManager.addfont(fpath)

# %%
# 폰트 지정하기(1): font.family 속성
plt.rcParams['font.family'] # ['sans-serif']

# 나눔고딕 폰트 사용
plt.rcParams['font.family'] = 'NanumGothic'

# %%
# 폰트 지정하기(2): rc() 함수
plt.rc('font', family='NanumBarunGothic')

# %%
# 폰트크기도 같이 조절
plt.rc('font', family='NanumBarunGothic', size=11)

# rcParams 객체로 확인
print(plt.rcParams['font.family'], plt.rcParams['font.size']) # ['NanumBarunGothic'] 11.0

# %%
# 그래프 제목 한글로 출력
plt.plot([1,4,9,16])
plt.title('간단한 선 그래프')
plt.show()

# %%
plt.rc('font', size=10)

# %%
# 출판사별 발행 도서 개수 산점도 그리기
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)
# %%
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()

# %%
# x축 : 발행년도, y축 : 출판사
# 출판사 수가 20000개가 넘기 때문에 모두 표현하기 어려움.
# 발행 도서가 많은 상위 30개 출판사의 데이터 중 일부 사용.
# 고유한 출판사 목록 만들기
top30_pubs = ns_book7['출판사'].value_counts()[:30]
top30_pubs

# %%
# 상위 30개 출판사에 해당하는 행을 표시하는 불리언 인덱스 생성
# isin() :
    
top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)
top30_pubs_idx

# %%
# 상위 30개 출판사의 발행도서 개수는?
top30_pubs_idx.sum() # 51886

# %%
# 무작위로 1000개 선택하기
# sample() :
    # random_state= : seed()와 유사한 역할
ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=42)
ns_book8.head()

# %%
# 산점도 그리기
# x축 : 발행년도, y축 : 출판사
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'])
ax.set_title('출판사별 발행 도서')
fig.show()

# %%
# 값에 따라 마커 크기를 다르게 나타내기
# scatter(..., s= )
# 입력 데이터와 동일한 길이의 배열을 지정하면 각 데이터마다 마커 크기가 다르게 표현.
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], s=ns_book8['대출건수'])
ax.set_title('출판사별 발행 도서')
fig.show()

# %%
# 마커 꾸미기
# 1. 투명도 조절하기 : alpha=
# 2. 마커 테두리 색 바꾸기 : edgecolor=
# 3. 마커 테두리 선 두께 바꾸기 : linewidths= 
# 4. 산점도 색 바꾸기 : c=
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(ns_book8['발행년도'], ns_book8['출판사'], linewidths=0.5, edgecolors='k', alpha=0.3, 
           s=ns_book8['대출건수']*2, c=ns_book8['대출건수'])
ax.set_title('출판사별 발행 도서')
fig.show()

# %%
# 값에 따라 색상 표현하기: 컬러맵
# scatter()의 기본값 : viridis 컬러맵

# jet 컬러맵으로 그리기
# 컬러 막대 : 컬러맵 색깔이 어떤 대출건수 값에 대응하는지 참조 정보 제공
# fig.colorbar(객체)
fig, ax = plt.subplots(figsize=(10,8))
sc = ax.scatter(ns_book8['발행년도'], ns_book8['출판사'],
                linewidths=0.5, edgecolors='k', alpha=0.3,
                s=ns_book8['대출건수']**1.3, c=ns_book8['대출건수'], cmap='jet')
ax.set_title('출판사별 발행 도서')
fig.colorbar(sc)
fig.show()
# 
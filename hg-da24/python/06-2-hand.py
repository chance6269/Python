# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:31:33 2024

@author: jcp
"""

# 06-2 맷플롯립의 고급 기능 배우기

# 그래프에 범례 추가
# 선 그래프, 막대 그래프 동시에 여러 개 그리는 법
# 데이터프레임의 피벗 테이블 기능

# %%
import matplotlib.font_manager as fm


# font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
font_files = fm.findSystemFonts(fontpaths=['C:/Users/jcp/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
    print(fpath)
    fm.fontManager.addfont(fpath)
    
# %%
import matplotlib.pyplot as plt

plt.rc('font', family='NaNumBarunGothic')

plt.rcParams['figure.dpi'] = 100
# %%
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

# %%
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()

# %%
# 하나의 피겨에 여러 개의 선 그래프 그리기
# plot() 함수 여러 번 호출

# 출판사에 대한 '발행년도'별 '대출건수' 그래프 그리기
# %%
# 상위 30위 정도의 고유한 출판사 목록
top30_pubs = ns_book7['출판사'].value_counts()[:30]
top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)

# %%
# '출판사','발행년도','대출건수'열만 추출
ns_book9 = ns_book7[top30_pubs_idx][['출판사','발행년도','대출건수']]

# %%
# 출판사, 발행년도 기준 대출건수 열의 합 구하기
# groupby() + sum()
ns_book9 = ns_book9.groupby(by=['출판사','발행년도']).sum()

# %%
# 인덱스 초기화
ns_book9 = ns_book9.reset_index()
# '황금가지' 출판사 데이터 확인
ns_book9[ns_book9['출판사'] == '황금가지'].head()

# %%
# 선 그래프 2개 그리기
# 출판사 별로 각각 데이터프레임 생성
line1 = ns_book9[ns_book9['출판사'] == '황금가지']
line2 = ns_book9[ns_book9['출판사'] == '비룡소']

# %%
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(line1['발행년도'],line1['대출건수'])
ax.plot(line2['발행년도'],line2['대출건수'])
ax.set_title('연도별 대출건수')
fig.show()

# %%
# 범례 추가 : legend()
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(line1['발행년도'],line1['대출건수'], label='황금가지')
ax.plot(line2['발행년도'],line2['대출건수'], label='비룡소')
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()

# %%
# 선 그래프 5개 그리기
# x축 좌표 범위 지정 : set_xlim(min, max)
fig, ax = plt.subplots(figsize=(8,6))
for pub in top30_pubs.index[:5]:
    line = ns_book9[ns_book9['출판사'] == pub]
    ax.plot(line['발행년도'],line['대출건수'], label=pub)
ax.set_title('연도별 대출건수')
ax.legend()
ax.set_xlim(1985, 2025)
fig.show()

# %%
# 스택 영역 그래프 : 
    # 하나의 선 그래프 위에 다른 선 그래프를 차례대로 쌓는 것
    # 그래프 사이의 간격이 y축의 값이 됨.
# stackplot(xval, yval) :
    # y축 값을 2차원 배열로 전달해야 함.
    
# 1. pivot_table() 메서드로 각 '발행년도'열의 값을 열로 바꾸기 - y축에 넣을 2차원 배열 만들기
# 2. '발행년도'열을 리스트 형태로 바꾸기 - x축에 넣을 리스트 만들기
# 3. stackplot() 메서드로 그래프 그리기

# %%
# pivot_table() 메서드로 각 '발행년도'열의 값을 열로 바꾸기
# 엑셀의 피벗 테이블과 유사한 기능
# pivot_table(index=, columns=)
ns_book10 = ns_book9.pivot_table(index='출판사', columns='발행년도')
ns_book10.head()
# 열이 다단으로 구성되어 있음.
# ('대출건수', 1947)
ns_book10.columns[:10]
# %%
# '발행년도' 열을 리스트 형태로 바꾸기
# get_level_values() : 
    # 인덱스 객체에서 호출
    # 다단으로 구성된 열 이름엥서 선택한 항목만 추출 가능
top10_pubs = top30_pubs.index[:10]
year_cols = ns_book10.columns.get_level_values(1)

# %%
# stackplot() :
    # x축 값 : year_cols
    # y축 값 : 상위 10개 출판사 행
    # 범례 : 출판사 이름
# legend(loc= ) : 범례 위치 지정
fig, ax = plt.subplots(figsize=(8, 6))
ax.stackplot(year_cols, ns_book10.loc[top10_pubs].fillna(0), labels=top10_pubs)
ax.set_title('연도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985, 2025)
fig.show()

# %%
# 하나의 피겨에 여러 개의 막대 그래프 그리기
# 
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(line1['발행년도'],line1['대출건수'], label='황금가지')
ax.bar(line2['발행년도'],line2['대출건수'], label='비룡소')
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()
# 먼저 그린 막대를 덮어쓰게 되는 문제 발생.
# 나란히 옆으로 그리려면?
# %%
# 기본너비 0.8의 절반인 0.4 너비로 그린 다음, 0.4의 절반 0.2씩 떨어지도록 그리기
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(line1['발행년도']-0.2,line1['대출건수'], label='황금가지', width=0.4)
ax.bar(line2['발행년도']+0.2,line2['대출건수'], label='비룡소', width=0.4)
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()

# %%
# 스택 막대 그래프 :
    # 위로 쌓은 그래프
# bar(bottom=막대가 시작할 y좌표)

height1 = [5,4,7,9,8]
height2 = [3,2,4,1,2]

plt.bar(range(5), height1, width=0.5)
plt.bar(range(5), height2, bottom=height1, width=0.5) #height1 막대가 끝나는 위치에서 시작
plt.show()
# 막대 시작 위치를 계속 누적 보관해야 하기때문에 불편함

# %%
# 막대의 길이를 누적해 놓고 그리는 방법
height3 = [a + b for a, b in zip(height1, height2)]

plt.bar(range(5), height3, width=0.5)
plt.bar(range(5), height1, width=0.5)
plt.show()

# %%
# 데이터값 누적하여 그리기
# cumsum()
ns_book10.loc[top10_pubs[:5], ('대출건수', 2013):('대출건수',2020)]

# %%
ns_book10.loc[top10_pubs[:5], ('대출건수', 2013):('대출건수',2020)].cumsum()

# %%
ns_book12 = ns_book10.loc[top10_pubs].cumsum()

# %%
# 주의 : 가장 큰 막대를 먼저 그려야함.
# - 큰 막대가 이전에 그린 막대를 모두 덮어버리는 문제 예방.
fig, ax = plt.subplots(figsize=(8, 6))
for i in reversed(range(len(ns_book12))): # 누적 합계가 가장 큰 마지막 출판사부터 그리기
    bar = ns_book12.iloc[i]
    label = ns_book12.index[i]
    ax.bar(year_cols, bar, label=label)
ax.set_title('연도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985, 2025)
fig.show()

# %%
# 원 그래프 그리기
# 원그래프 : 
    # 전체 데이터에 대한 비율을 원의 부채꼴로 나타낸 그래프
    # pie chart
    
# %%
# 상위 출판사의 발행 도서 비율
data = top30_pubs[:10]
labels = top30_pubs.index[:10]

# %%
# pie(data, labels= )
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels)
ax.set_title('출판사 도서 비율')
fig.show()
# 3시 방향부터 반시계 방향
# %%
# 원 그래프의 단점 :
    # 시각적으로 어떤 데이터가 더 큰지 구분하기 어려움.
    
# %%
# startangle=
plt.pie([10,9], labels=['A제품', 'B제품'], startangle=90)
plt.title('제품의 매출 비율')
plt.show()

# %%
# 비율 표시하고 부채꼴 강조하기
# pie(..., autopct= ) :
    # % 연산자에 적용할 포맷팅 문자열 전달.
# %d : 정수로 표시
# pie(..., explode= ) :
    # 조각을 조금 떨어뜨려 시각적으로 부각
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels, autopct='%.1f%%', explode=[0.1]+[0]*9, startangle=90)
ax.set_title('출판사 도서 비율')
fig.show()

# %%
# 여러 종류의 그래프가 있는 서브플롯 그리기
fig, axes = plt.subplots(2,2, figsize=(20,16))

# 산점도
ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=42)
sc = axes[0, 0].scatter(ns_book8['발행년도'], ns_book8['출판사'], linewidths=0.5, edgecolors='k', alpha=0.3,
                        s=ns_book8['대출건수'], c=ns_book8['대출건수'], cmap='jet')
axes[0,0].set_title('출판사별 발행 도서')
fig.colorbar(sc, ax=axes[0,0])

# 스택 영역 그래프
axes[0,1].stackplot(year_cols,ns_book10.loc[top10_pubs].fillna(0), labels=top10_pubs)
axes[0,1].set_title('연도별 대출건수')
axes[0,1].legend(loc='upper left')
axes[0,1].set_xlim(1985, 2025)

# 스택 막대 그래프
for i in reversed(range(len(ns_book12))):
    bar = ns_book12.iloc[i] # 행추출
    label = ns_book12.index[i] # 출판사 이름 추출
    axes[1,0].bar(year_cols, bar, label=label)
axes[1,0].set_title('연도별 대출 건수')
axes[1,0].legend(loc='upper left')
axes[1, 0].set_xlim(1985, 2025)

# 원 그래프
axes[1,1].pie(data, labels=labels, startangle=90, autopct='%.1f%%', explode=[0.1]+[0]*9)
axes[1,1].set_title('출판사 도서 비율')

fig.savefig('all_in_one.png')
fig.show()

# %%
# 판다스로 여러 개의 그래프 그리기

# 스택 영역 그래프 그리기
ns_book11 = ns_book9.pivot_table(index='발행년도', columns='출판사', values='대출건수')
ns_book11.loc[2000:2005]
# 이전과 다르게 values에 집계할 열을 지정
# -> 열 이름이 다단으로 구성되지 않아 get_level_values() 사용 안해도 됨.
# %%
# pivot_table()의 aggfunc 파라미터를 사용하는 방식.
# 기본 집계 방식이 평균이므로, 값을 모두 더하기 위해 np.sum() 지정
import numpy as np

ns_book11 = ns_book7[top30_pubs_idx].pivot_table(index='발행년도', columns='출판사', values='대출건수', aggfunc=np.sum)
ns_book11.loc[2000:2005]
# %%
# plot.area()
fig, ax = plt.subplots(figsize=(8, 6))
ns_book11[top10_pubs].plot.area(ax=ax, title='연도별 대출건수', xlim=(1985, 2025))
ax.legend(loc='upper left')
fig.show()

# %%
# 스택 막대 그래프 그리기
# plot.bar() :
    # 기본적으로 막대를 나란히 출력
    # stacked=True : 스택 막대 그래프 그리기
    # cumsum() 호출 안해도 됨.

fig, ax = plt.subplots(figsize=(8, 6))    
ns_book11.loc[1985:2025, top10_pubs].plot.bar(
    ax=ax, title='연도별 대출건수', stacked=True, width=0.8)
ax.legend(loc='upper left')
fig.show()

# %%
fig, ax = plt.subplots(figsize=(8, 6))    
ns_book11[top10_pubs].plot.bar(ax=ax, title='연도별 대출건수', stacked=True, width=0.8)
ax.legend(loc='upper left')
# ax.set_xlim(1985, 2025) # 버그가 있어 작동하지 않음.
fig.show()
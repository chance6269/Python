# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:04:31 2024

@author: pjc62
"""

# 05-2 선 그래프와 막대 그래프 그리기

# 선 그래프, 막대 그래프 그리기
# 선 모양, 그래프 색상 바꾸기
# 이미지 출력, 그래프를 이미지로 저장하기

# 선 그래프 : 데이터 포인트 사이를 선으로 이은 그래프

# 막대 그래프 : 데이터 포인트의 크기를 막대 높이로 나타낸 그래프

# 산점도 - 전체 데이터의 형태를 가늠하는데 용이.

# 선, 막대 그래프 - 한 축을 따라 어떤 데이터의 변화를 살펴보는데 용이하다.
# ex) 연도별로 몇권의 도서가 발행되었는가

# 연도별 발행 도서 개수 구하기

import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

# %%
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()

# %%
# value_counts() :
    # 한 열에서 고유한 값의 등장 횟수 계산
count_by_year = ns_book7['발행년도'].value_counts()
count_by_year 
# 발행년도
# 2012    18601
# 2014    17797
# 2009    17611
# 2011    17523
# 2010    17503
 
# 2650        1
# 2108        1
# 2104        1
# 2560        1
# 1947        1
# Name: count, Length: 87, dtype: int64

# %%
# numpy의 unique()와 비슷한 결과
import numpy as np
np.unique(ns_book7['발행년도'], return_counts=True)

# %%
# 데이터 정렬하기
count_by_year = count_by_year.sort_index()
count_by_year
# 발행년도
# 1947     1
# 1948     1
# 1949     1
# 1952    11
# 1954     1
#         ..
# 2551     1
# 2552     2
# 2559     1
# 2560     1
# 2650     1
# Name: count, Length: 87, dtype: int64

# %%
# 발행년도가 2030년 이상인 데이터 제거
count_by_year = count_by_year[count_by_year.index <= 2030]
count_by_year

# %%
# 주제별 도서 개수 구하기
# 주제분류열의 첫번째 문자를 기준으로 도서를 카운트

# NaN이라면 -1을 반환하는 함수를 만들어 걸러내야 함.
import numpy as np # np.nan을 사용하기 위해 임포트

def kdc_1st_char(no):
    if no is np.nan:
        return '-1'
    else:
        return no[0]
    
count_by_subject = ns_book7['주제분류번호'].apply(kdc_1st_char).value_counts()
count_by_subject
# 주제분류번호
# 8     108643
# 3      80767
# 5      40916
# 9      26375
# 6      25070
# 1      22647
# -1     16978
# 7      15836
# 4      13688
# 2      13474
# 0      12376
# Name: count, dtype: int64

# 문학에 해당하는 8로 시작하는 도서가 가장 많음.

# %%
# 선 그래프 그리기
# plot(x축, y축)

# 서브플롯 없이 figure 객체로 선그래프 그리기
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 100

# %%
plt.plot(count_by_year.index, count_by_year.values)
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()

# %%
# 선 모양과 색상 바꾸기
# plot(.., linestyle= , color=, marker= )
# 선 모양
# solid line : '-'
# dotted line : ':'
# dash dot line :'-.'
# dashed line : '--'

plt.plot(count_by_year, linestyle=':',marker='.', color='red')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()

# %%
# 하나의 문자열로 합쳐서 지정하면?
plt.plot(count_by_year, '.:r')

# %%
# 별 모양 마커와 실선을 사용한 선그래프를 녹색으로 그리기
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()

# %%
# 선 그래프 눈금 개수 조절 및 마커에 텍스트 표시하기
# xticks() : x축 눈금 지정
# annotate(문자열, (x, y)) : 그래프에 값 표시
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val))
plt.show()

# %%
# 텍스트를 마커에서 조금 떼어 놓으려면?
# xytext= : 텍스트 위치 조절
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(idx+1,val+10))
plt.show()
# y축의 스케일이 x축보다 훨씬 커서 거의 차이가 없음. 
# 상대적인 위치를 포인트나 픽셀 단위로 지정해야함. -> textcoords=

# %%
# textcoords='offset points' : 상대적 위치로 조절

plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
    plt.annotate(val, (idx, val), xytext=(2,2), textcoords='offset points')
plt.show()

# %%
# 막대 그래프 그리기
# bar(x, y)
plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0,2), textcoords='offset points')
plt.show()

# %%
# 텍스트 정렬, 막대 조절 및 색상 바꾸기
# annotate(ha='center') : 텍스트 위치 막대 중앙 정렬
# annotate(fontsize= ) : 폰트 크기 조절
# annotate(color= ) : 색상 지정
# bar(width= ) : 막대 두께 지정
# bar(color= ) : 막대 색상 지정

plt.bar(count_by_subject.index, count_by_subject.values, width=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (idx, val), xytext=(0,2), textcoords='offset points', ha='center', fontsize=8, color='green')
plt.show()

# %%
# 가로 막대 그래프 그리기
# barh()
# x축, y축 제목 반대로 쓰기
# 막대 두께 : width 대신 height=
# annotate() 좌표도 반대로
# ha=대신 va=
plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.ylabel('subject')
plt.xlabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (val, idx), xytext=(2,0), textcoords='offset points', va='center', fontsize=8, color='green')
plt.show()

# %%
# 좀 더 알아보기1 :
    # 이미지 출력하고 저장하기

# 이미지 읽기
# imread() : 이미지를 읽어 넘파이 배열로 반환
import matplotlib.pyplot as plt
img = plt.imread('jupiter.png')
img.shape # (1561, 1646, 3)

# %%
# 이미지 화면에 출력하기
# imshow()
plt.imshow(img)
plt.show()
# 피겨 큐기에 상관없이 기본적으로 원본의 가로세로 비율을 유지함.

# %%
# 축과 눈금 출력 끄기 : axis('off')
plt.figure(figsize=(8,6))
plt.imshow(img)
plt.axis('off')
plt.show()

# %%
# 이미지 저장하기
# imsave(파일이름, 넘파이 배열)
plt.imsave('jupiter.jpg', img)

# %%
# 좀 더 알아보기2 :
    # 그래프를 이미지로 저장하기
# savefig(저장할 파일 이름, dpi= )
# rcParams['savefig.dpi'] 로 기본 dpi 지정 가능

plt.rcParams['savefig.dpi'] # 'figure'

# %%
# show()로 figure 객체가 소멸하기 이전에 savefig()를 호출해야 함.
plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.ylabel('subject')
plt.xlabel('number of books')
for idx, val in count_by_subject.items():
    plt.annotate(val, (val, idx), xytext=(2,0), textcoords='offset points', va='center', fontsize=8, color='green')
plt.savefig('books_by_subject.png')
plt.show()

# %%
plt.imshow(plt.imread('books_by_subject.png'))
plt.axis('off')
plt.show()
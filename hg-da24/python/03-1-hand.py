# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:14:50 2024

@author: jcp
"""

import pandas as pd

ns_df = pd.read_csv('ns_202104.csv', low_memory=False)
ns_df.head()

# %%
# Unnamed: 13 열 삭제

ns_book = ns_df.loc[:,'번호':'등록일자']
ns_book.head()

# %%
# 불리언 배열을 사용하여 원하는 열 선택.

print(ns_df.columns)

# 
print(type(ns_df.columns))
# 판다스의 Index 클래스 객체
# 파이썬 리스트처럼 숫자 인덱스로 참조 가능.
print(ns_df.columns[0]) # 번호
# %%
# 원소별 비교 :
    # 판다스 배열 성격의 객체는 어떤 값과 '비교'할 때 자동으로 배열에 있는 모든 원소와 하나씩 비교.
    
ns_df.columns != 'Unnamed: 13'
# array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#         True,  True,  True,  True, False])

# %%
selected_columns = ns_df.columns != 'Unnamed: 13'
ns_book = ns_df.loc[:, selected_columns]
ns_book.head()

# %%
# 중간에 있는 '부가기호'열 제외

selected_columns = ns_df.columns != '부가기호'
ns_book = ns_df.loc[:, selected_columns]
ns_book.head()

# %%
# drop() : 데이터프레임 행, 열 삭제.
# drop(행 or 열 이름, axis=0 or 1)

ns_book = ns_df.drop('Unnamed: 13', axis=1)
ns_book.head()

# %%

ns_book = ns_df.drop(['부가기호','Unnamed: 13'], axis=1)
ns_book.head()

# %%
# inplace 매개변수로 '주제분류번호'열 삭제
# 연결된 객체가 수정되는 것이 아님.
# 내부적으로 수정된 새로운 객체를 만든 후, ns_book 변수에 연결.
# 성능상 이득은 없다.
ns_book.drop('주제분류번호', axis=1, inplace=True)
ns_book.head()

# %%
# dropna() : NaN이 하나 이상 포함된 행이나 열을 삭제

ns_book = ns_df.dropna(axis=1)
ns_book.head()

# %%
# 모든 값이 NaN인 열 삭제.
ns_book = ns_df.dropna(axis=1, how='all')
ns_book.head()

# %%
# # 행 삭제.

# ns_book2 = ns_book.drop([0,1])
# ns_book2.head()

# # %%
# # 행 선택 방법 : 슬라이싱, 불리언 배열
# # 슬라이싱
# ns_book2 = ns_book[2:]
# ns_book2.head()

# # %%
# # 불리언 배열
# selected_rows = ns_df['출판사' ]=='한빛미디어'
# ns_book2 = ns_book[selected_rows]
# ns_book2.head()
# # %%
# # loc()에 불리언 배열 사용
# ns_book2 = ns_book.loc[selected_rows]
# ns_book2.head()

# # %%
# ns_book2 = ns_book[ns_book['대출건수'] > 1000]
# ns_book2.head()

# %%
#  중복된 행 찾기
# duplicated() :
    # 첫번째 이후 중복된 행은 True, 첫번째의 중복되지 않은 행은 False의 불리언 배열을 반환

# sum()과 함께 사용하여 중복된 행 개수 카운트 가능.
sum(ns_book.duplicated()) # 0

# %%
# 도서명, 저자, ISBN 기준으로 중복된 행 찾기.
# duplicated(subset=['도서명','저자','ISBN])
sum(ns_book.duplicated(subset=['도서명','저자','ISBN'])) # 22096

# %%
# 어떤 데이터가 중복되었는지 확인
# duplicated(keep=False) : 중복된 모든 행을 True로 표시.
dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=False)
ns_book3 = ns_book[dup_rows]
ns_book3.head()

# %%
# 그룹별로 모으기
# 같은 도서의 대출건수를 하나로 합치기.
# groupby()

count_df = ns_book[['도서명','저자','ISBN','권','대출건수']]
# %%
# 정수 타입인 대출건수열은?
# sum()
# groupby()는 기본적으로 by에 지정된 열에 NaN이 포함되어 있으면 해당 행을 삭제함.
# NaN이 포함되어 있는 행을 삭제하고 계산하면 대출건수 합계에서 빠지기 때문에
# dropna=False 지정.

group_df = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False)
loan_count = group_df.sum()

# %%
loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
loan_count.head()
# 인덱스 : 도서명, 저자, ISBN, 권
# '대출건수'열 : 각 책의 대출건수를 더한 결과

# %%
# 원본 데이터 업데이트하기

# 1. duplicated()로 중복된 행을 True로 표시한 불리언 배열 만들기
# 2. 반전시켜서 중복되지 않은 고유한 행을 True로 표시
# 3. 2번의 불리언 배열을 사용해 원본 배열에서 고유한 행만 선택.

# 판다스의 ~연산자 : 불리언 배열 반전.

# %%
dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
unique_rows = ~dup_rows
ns_book3 = ns_book[unique_rows].copy()

sum(ns_book3.duplicated(subset=['도서명','저자','ISBN','권'])) # 0

# %%
# 원본 데이터프레임 인덱스 설정하기
# set_index(...,inplace=True)
ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
ns_book3.head()

# %%
# 업데이트하기
# update()
ns_book3.update(loan_count)
ns_book3.head()

# %%
# 인덱스열 해제
# reset_index()

ns_book4 = ns_book3.reset_index()
ns_book4.head()

# %% 
# 대출건수가 잘합쳐졌는지 확인하기
sum(ns_book['대출건수']>100) # 2311

# %%
sum(ns_book4['대출건수']>100) # 2550
# 대출건수 100회이상인 책이 훨씬 늘어남
# -> 중복된 도서의 대출건수를 합쳤기 때문에

# 그러나 여러 개의 열을 사용해 데이터프레임의 인덱스를 만들었다가 다시 해제했기 때문에
# 초기 데이터프레임과 ns_book4의 열 순서가 달라졌다.
# %%
# 원래 열 순서대로 맞추기
# : []연산자에 원하는 열 이름을 순서대로 전달
ns_book4 = ns_book4[ns_book.columns]
ns_book4.head()

# %%
# 저장
ns_book4.to_csv('ns_book4.csv', index=False)

# %%
# 일괄 처리 함수 만들기

def data_cleaning(filename):
    
    ns_df = pd.read_csv(filename, low_memory=False)
    
    ns_book = ns_df.dropna(axis=1, how='all')
    
    count_df = ns_book[['도서명','저자','ISBN','권','대출건수']]
    
    loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
    
    dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
    unique_rows = ~dup_rows
    ns_book3 = ns_book[unique_rows].copy()
    
    ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
    
    ns_book3.update(loan_count)
    
    ns_book4 = ns_book3.reset_index()
    
    ns_book4 = ns_book4[ns_book.columns]
    return ns_book4

# %%
new_ns_book4 = data_cleaning('ns_202104.csv')
ns_book4.equals(new_ns_book4)
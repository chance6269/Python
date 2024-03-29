# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:17:35 2024

@author: jcp
"""

# 3-2 잘못된 데이터 수정하기


# import gdown

# gdown.download('https://bit.ly/3GisL6J', 'ns_book4.csv', quiet=False)

# %%
# 데이터프레임 정보 요약 확인하기

import pandas as pd
ns_book4 = pd.read_csv('ns_book4.csv', low_memory=False)
ns_book4.head()

# %%
# df.info() :
    # 전체 행 갯수, 열 개수, 열 이름, 누락된 값이 없는 행 개수, 열 데이터 타입
ns_book4.info()

# %%
# ns_book4.info(memory_usage='deep')

# %%
#  누락된 값 처리하기
# 각 열의 누락된 값이 몇 개 있는지 확인하고, 누락된 값을 표시하는 방법

# 누락된 값 개수 확인 : isna()
# NaN 직접 카운트. 각 행이 비어 있는지 나타네는 불리언 배열 반환.
# isna() + sum() 으로 비어 있는 행 개수 확인
ns_book4.isna().sum()

# %%

# 누락된 값으로 표시하기 None과 np.nan
# 정수를 저장하는 열에 None을 입력하면 누락된 값으로 인식.

ns_book4.loc[0,'도서권수'] = None
ns_book4['도서권수'].isna().sum()

# %%
ns_book4.head(2)
# : NaN으로 표시
# '도서권수'값이 1 -> 1.0으로 바뀐 이유
# 판다스가 NaN을 특별한 실수 값으로 저장하기 때문.

# %%
# 열 데이터 타입 지정하기
# astype({열이름:데이터 타입})
ns_book4.loc[0, '도서권수'] = 1
ns_book4 = ns_book4.astype({'도서권수': 'int32', '대출건수': 'int32'})
ns_book4.head(2)

# %%
# 문자열을 저장할 수 있는 열에 None을 입력한다면?
ns_book4.loc[0, '부가기호'] = None
ns_book4.head(2)
# : 그대로 None으로 표시
# %%
# NaN 입력하기
import numpy as np
ns_book4.loc[0,'부가기호'] = np.nan
ns_book4.head(2)

# %%
# 누락된 값 바꾸기(1)
# loc, fillna()
# '세트 ISBN'열의 누락된 값을 NaN이 아니라 빈 문자열''로 바꾸기
# loc + isna()
set_isbn_na_rows = ns_book4['세트 ISBN'].isna() # 누락된 값을 찾아 불리언 배열로 반환
ns_book4.loc[set_isbn_na_rows,'세트 ISBN'] = ''
ns_book4['세트 ISBN'].isna().sum() # 누락된 열 확인 : 0
# %%
# 좀더 편하게 바꾸는 방법
# fillna()
# NaN -> '없음'으로 바꾸기
# 기본적으로 새로운 데이터프레임을 반환하므로 isna()를 연결하면 NaN의 개수를 셀 수 있음.
ns_book4.fillna('없음').isna().sum()
# %%
# 특정 열만 선택해서 바꾸기
ns_book4['부가기호'].fillna('없음').isna().sum() # 0
# 문제 : 특정 열 선택후 fillna() 적용시, 열 이름 없이 개수만 있는 Series객체로 반환함.
# %%
type(ns_book4['부가기호']) # Series
# %%
# NaN을 바꾸면서 전체 데이터프레임을 반환하기
# fillna({열이름:바꾸려는 값})
ns_book4.fillna({'부가기호':'없음'}).isna().sum()

# %%
# 누락된 값 바꾸기(2)
# df.replace()
# 첫째, 바꾸려는 값이 하나 일때
# df.replace(old, new)
ns_book4.replace(np.nan, '없음').isna().sum()

# %%
# 둘째, 바꾸려는 값이 여러 개일 때
# replace([old1, old2],[new1, new2])
ns_book4.replace([np.nan, '2021'], ['없음', '21']).head(2)
# %%
# replace({old1:new1,old2:new2}).head(2)
ns_book4.replace({np.nan:'없음','2021':'21'}).head(2)

# %%
# 셋째, 열마다 다른 값으로 바꿀 때
# replace({열 이름: old}, new)
ns_book4.replace({'부가기호': np.nan}, '없음').head(2)
# %%
ns_book4.replace({'부가기호':{np.nan:'없음'},'발행년도':{'2021':'21'}}).head(2)

# %%
# 정규 표현식
#  - 문자열 패턴을 찾아서 대체하기 위한 규칙의 모음.

# 100번과 101번 행의 네 자리 연도를 두자리로 바꿀때,
ns_book4.replace({'발행년도':{'2021':'21'}})[100:102]
# 연도가 2018이라면 적용이 안되는 문제 발생.

# %%
# 숫자 찾기: \d
# 4자리연도를 뒤에 두자리만 묶을 때 : \d\d(\d\d)
# A21을 만나면? : 영문자가 있고 3글자로 이루어져 있기에 Pass.
# regex 매개변수 : 정규 표현식을 사용한다는 의미.
# \1, \2으로 패턴 안의 그룹을 나타냄
# r : 파이썬에서 정규 표현식을 다른 문자열과 구분하기 위해 접두사처럼 붙임.
ns_book4.replace({'발행년도':{r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102]

# %%

# 정규 표현식이 반복될 때
# 중괄호를 사용하여 개수 지정.
reg_ns_book4 = ns_book4.replace({'발행년도':{r'\d{2}(\d{2})':r'\1'}}, regex=True)[100:102]

# %%
# 문자 찾기: 마침표(.)
# 저자
# 로런스 인그래시아 (지은이), 안기순 (옮긴이) -> 로런스 인그래시아, 안기순
reg_ns_book4 = ns_book4.replace({'저자':{r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]

# %%
# 잘못된 값 바꾸기

# ns_book4.astype({'발행년도':'int32'})
# ValueError: invalid literal for int() with base 10: '1988.': Error while type casting for column '발행년도'
# '1988.' 을 변환할 수 없어 에러 발생
# %%
# 정규 표현식으로 다른 문자가 있는 연도를 찾아보기
# pd.str.contains() : 시리즈나 인덱스에서 문자열 패턴을 포함하고 있는지 검사

# 발행년도 열에 '1988'이 포함된 행의 개수는?
ns_book4['발행년도'].str.contains('1988').sum() # 407

# %%
# ns_book4['발행년도']=='1988'처럼 쓰면 안되는 이유 :
    # 정확히 '1988'만 검색. '1988.'같은 것은 제외 됨.
    # contains()는 주어진 문자열이 포함된 모든 행을 찾음.
    # 정규 표현식을 인식함.
    
# %%
# contains()의 na 매개변수.
# na=True 
# : 연도가 누락된 행을 True, 연도가 들어간 행을 False로 지정.
invalid_number = ns_book4['발행년도'].str.contains('\D', na=True) # 숫자 이외 문자를 포함한 것들 + 누락된 행,
print(invalid_number.sum()) # 숫자 이외의 문자가 들어간 행의 개수 출력 : 1777
ns_book4[invalid_number].head()

# %%
# 연도 앞과 뒤에 있는 문자 제외
ns_book5 = ns_book4.replace({'발행년도': r'.*(\d{4}).*'}, r'\1', regex=True)
ns_book5[invalid_number].head()

# %%
unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
print(unkown_year.sum()) # 67
ns_book5[unkown_year].head()
#
# %%
# NaN이거나 네 자리 숫자가 아닌 값 처리
# 임의로 -1 값으로 바꾼다음 astype()메서드로 '발행년도'열을 정수형으로 변환
ns_book5.loc[unkown_year, '발행년도'] = '-1'
ns_book5 = ns_book5.astype({'발행년도':'int32'})

# %%
# 연도 중 이상하게 큰 값이나 작은 값이 들어 있는 경우.
# gt(): 전달된 값보다 큰 값 찾기.
ns_book5['발행년도'].gt(4000).sum() # 131

# %%
(ns_book5['발행년도'] > 4000).sum() # 131

# %%
# -=2333 으로 서기로 바꾼다음 4000년이 넘는 도서가 있는지 확인
dangun_yy_rows = ns_book5['발행년도'].gt(4000) # 4000보다 큰 값을 찾아 불리언 배열로
ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333
# ns_book5.loc[dangun_yy_rows, '발행년도'] -= 2333
# %%
dangun_year = ns_book5['발행년도'].gt(4000) # 다시 4000 이상 값 찾기
print(dangun_year.sum()) # 13
ns_book5[dangun_year].head(2)
# %%
ns_book5.loc[dangun_year, '발행년도'] = -1

# %%
# 연도 작은 값 확인하기
# 0보다 크고 1900년 이전 도서
old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900) # 0보다 크고 1900보다 작은값 찾기
ns_book5[old_books]

# %%
ns_book5.loc[old_books, '발행년도'] = -1
ns_book5['발행년도'].eq(-1).sum() # 86

# %%
# 누락된 정보 채우기
# '도서명','저자','출판사','발행년도'열이 분석에 중요하다고 판단.
# 위 4개 열에 누락된 값이 있으면 안됨
# 누락된 값이 있거나 '발행년도'열이 -1인 행의 개수 확인
na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
    | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
print(na_rows.sum()) # 5268
ns_book5[na_rows].head(2)

# %% 
# BeautifulSoup로 채우기

import requests
from bs4 import BeautifulSoup
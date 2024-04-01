# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:25:26 2024

@author: jcp
"""

# 01-3

# gdown 웹에서 대용량 파일을 다운로드할 수 있는 패키지
import gdown
gdown.download('https://bit.ly/3eecMKZ','남산도서관 장서 대출목록 (2021년 04월).csv', quiet=False)

# %%
# 파이썬으로 csv 파일 출력하기
# open(), readline()

with open('남산도서관 장서 대출목록 (2021년 04월).csv') as f:
    print(f.readline())
    
# %%
# 파일 인코딩 형식 확인하기 
# chardet.detect()
# open()
# mode='rb' : 바이너리 읽기 모드. 문자 인코딩 형식에 상관없이 파일 열기 가능.
import chardet
with open('남산도서관 장서 대출목록 (2021년 04월).csv', mode='rb') as f:
    d = f.readline()
print(chardet.detect(d))
{'encoding': 'EUC-KR', 'confidence': 0.99, 'language': 'Korean'}

# %%
# 인코딩 형식 지정하기
# open() :
    # encoding= : 인코딩 형식 지정 파라미터
with open('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='EUC-KR') as f:
    print(f.readline())
    print(f.readline())
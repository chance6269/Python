#!/usr/bin/env python
# coding: utf-8

# # 01-3 이 도서가 얼마나 인기가 좋을까요?

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 도서 데이터 찾기

# [공공데이터포털](https://www.data.go.kr/)
# 
# 도서관 정보나루의 [남산도서관 장서/대출 목록](https://www.data4library.kr/openDataV?libcode=4707)

# ## 코랩에서 데이터 확인하기

# In[4]:


import gdown

gdown.download('https://bit.ly/3eecMKZ', 
               './data/남산도서관 장서 대출목록 (2021년 04월).csv', quiet=False)

# %%
import gdown

gdown.download('https://data4library.kr/openDataV?libcode=4707', 
               './data/서울특별시교육청남산도서관 장서 대출목록 (2024년 02월).csv', quiet=False)


# %%
# ## 파이썬으로 CSV 파일 출력하기

# In[5]:


with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv') as f:
    print(f.readline())


# In[11]:


"""
fp = open('남산도서관 장서 대출목록 (2021년 04월).csv')
for rd in fp.readline():
    print(rd)
fp.close()
"""


# In[ ]:


# 파일 인코딩 형식 확인
import chardet

with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv', mode='rb') as f:
    d = f.readline()

print(chardet.detect(d)) # 읽은 내용의 인코딩 확인
# {'encoding': 'EUC-KR', 'confidence': 0.99, 'language': 'Korean'}

# In[ ]:


with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr') as f:
    print(f.readline()) # 번호,도서명,저자,출판사,발행년도,ISBN,세트 ISBN,부가기호,권,주제분류번호,도서권수,대출건수,등록일자,
    print(f.readline()) # "1","인공지능과 흙","김동훈 지음","민음사","2021","9788937444319","","","","","1","0","2021-03-19",


# In[ ]:


# 파일명 처리 방식
# MacOS : NFD
# Windows, Linux : NFC
# NFC : 한글
# NFD : ㅎㅏㄴㄱㅡㄹ
#
import os
import glob
import unicodedata

for filename in glob.glob('./data/*.csv'):
  nfc_filename = unicodedata.normalize('NFC', filename)
  os.rename(filename, nfc_filename)
  print("filename:", filename)
  print("nfc_filename:", nfc_filename)


# ## 데이터프레임 다루기: 판다스

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr')
# DtypeWarning: Columns (5,6,9) have mixed types. Specify dtype option on import or set low_memory=False.

# 컬럼5 : ISBN
# 컬럼6 : 세트ISBN
# 컬럼9 : 주제분류번호

# 판다스에서 csv파일을 읽을 때 분할해서 읽음
# 데이터타입을 자동으로 인식.
# 그 때 분할해서 읽은 데이터들의 자료형이 일치하지 않으면 발생되는 경고.


# In[ ]:


df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 low_memory=False)


# In[ ]:


df.head()


# In[ ]:


df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 dtype={'ISBN': str, '세트 ISBN': str, '주제분류번호': str})
df.head()


# In[ ]:


df.to_csv('./data/ns_202104.csv')


# In[ ]:


with open('./data/ns_202104.csv', encoding="utf-8") as f:
    for i in range(3):
        print(f.readline(), end='')


# In[ ]:


ns_df = pd.read_csv('./data/ns_202104.csv', low_memory=False)
ns_df.head()


# In[ ]:

    # index_col=0 : 첫 번째(0) 컬럼을 인덱스로 지정

ns_df = pd.read_csv('./data/ns_202104.csv', index_col=0, low_memory=False)
ns_df.head()


# In[ ]:

# index=False: 저장할 때 인덱스를 제외
df.to_csv('./data/ns_202104_noindex.csv', index=False)


# In[ ]:


# 코랩을 사용하는 경우 xlsxwriter 패키지를 설치해 주세요.
# get_ipython().system('pip install xlsxwriter')


# In[ ]:


ns_df.to_excel('./data/ns_202104.xlsx', index=False, engine='xlsxwriter')

print("엑셀 파일 생성 종료")
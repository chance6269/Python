# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:48:16 2024

@author: jcp
"""

# ### 5.2.2 표 형식의 데이터 파일 읽고 쓰기

# #### CSV 파일 읽고 쓰기

# [5장: 168페이지]

# In[ ]:


# get_ipython().run_cell_magic('writefile', 'E:/Workspace/Python/Pandas/books/data/A_product_sales.csv', '연도,1분기,2분기,3분기,4분기\n2016,2412,4032,5183,1139\n2017,2725,4986,6015,1242\n2018,2925,5286,6497,1596\n2019,2691,5813,7202,1358\n2020,2523,6137,7497,1512\n')


# [5장: 169페이지]

# In[ ]:


import pandas as pd

#  CSV 파일 경로
folder = 'E:/Workspace/Python/Pandas/books/data/' # 폴더 지정
csv_file = folder + 'A_product_sales.csv' # 파일 경로 지정

# CSV 파일을 읽어와서 DataFrame 데이터 생성
df = pd.read_csv(csv_file, encoding = "utf-8") 
df


# In[ ]:


df = pd.read_csv(csv_file, index_col="연도")
df


# [5장: 171페이지]

# In[ ]:


df = pd.DataFrame({ '고객ID': ['C5001', 'C5002', 'C5003', 'C5004'],
                     '국가':['한국', '미국', '영국', '독일'],
                      '주문금액':[1152000, 2507000, 3698000, 4504100] })
df


# In[ ]:


# CSV 파일 경로
folder = 'E:/Workspace/Python/Pandas/books/data/'    # 폴더 지정
csv_file = folder + 'sales_info_w.csv'     # 파일 경로 지정

df.to_csv(csv_file)                      # DataFrame 데이터를 CSV 파일로 쓰기
print("생성한 CSV 파일:", csv_file)      # 생성한 파일 이름 출력


# [5장: 172페이지]

# In[ ]:


# CSV 파일 경로
folder = 'E:/Workspace/Python/Pandas/books/data/'
csv_file = folder + 'sales_info_cp949_encoding.csv'

# DataFrame 데이터를 CSV 파일로 쓰기(인코딩은 'cp949', index 포함 안 함)
# encoding : cp949(euc-kr 호환, 더 많은 한글 문자 지원)
# index : False, 인덱스를 제외
df.to_csv(csv_file, encoding="cp949", index=False)
print("생성한 CSV 파일:", csv_file) # 생성한 파일 이름 출력



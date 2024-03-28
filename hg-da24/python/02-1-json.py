#!/usr/bin/env python
# coding: utf-8

# # 02-1 API 사용하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 파이썬에서 JSON 데이터 다루기

# JSON :
    # 파이썬의 dictionary와 list를 중첩해 놓은 것과 비슷함.


# In[1]:


# dict
d = {"name": "혼자 공부하는 데이터 분석"}

print(d['name'])


# In[2]:

    # 웹 기반 API로 데이터를 전달할 때에는 딕셔너리가 아닌, 
    # 텍스트로 전달해야하기 때문에 변환이 필요.
    
import json


# In[3]:

    # json.dumbs()
# 파이썬 객체를 json문자열로 변환
# 기본적으로 아스키 문자 외의 다른 문자를 16진수로 출력하기 때문에 한글이 제대로 안보임.
# ensure_ascii=False : 저장된 문자를 그대로 출력.

d_str = json.dumps(d, ensure_ascii=False)
print(d_str) # {"name": "혼자 공부하는 데이터 분석"}


# In[4]:


print(type(d_str)) # <class 'str'>


# In[5]:

# JSON 문자열을 파이썬 프로그램에 사용하려면 다시 파이썬 dict로 바꾸어야 함.

    # json.loads()
# json문자열을 딕셔너리로 변환
d2 = json.loads(d_str)

print(d2['name'])


# In[6]:


print(type(d2)) # <class 'dict'>


# In[7]:



d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022}')

print(d3['name'])
print(d3['author'])
print(d3['year'])


# In[8]:

# dict 안에 list 중첩
    
# 문자열이 길 경우 \로 연결 가능

d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", \
                "author": ["박해선","홍길동"], \
                  "year": 2022}')

print(d3['author'][1]) # 홍길동

print(type(d3['author'])) # <class 'list'>


# In[9]:

# 멀티라인 문자열 지정
# json : 배열[객체, 객체]
# python : 리스트[딕셔너리, 딕셔너리]
d4_str = """
[
  {"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name": "혼자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""
d4 = json.loads(d4_str)

print(type(d4)) # <class 'list'>
print(d4[0]['name']) # 혼자 공부하는 데이터 분석
print(d4[1]['name']) # 혼자 공부하는 머신러닝+딥러닝


# In[10]:


import pandas as pd

# json 문자열 -> 판다스 데이터프레임으로 생성
pd_d4 = pd.read_json(d4_str)
print(pd_d4)


# In[11]:

# JSON문자열 -> 파이썬 객체 -> 데이터 프레임
# 리스트 -> 데이터프레임
pd_d4_11 = pd.DataFrame(d4)



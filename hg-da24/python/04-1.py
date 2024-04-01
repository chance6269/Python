#!/usr/bin/env python
# coding: utf-8

# # 04-1 통계로 요약하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/04-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# 기술통계 : 자료의 내용을 압축하여 설명하는 방법(=요약 통계)
# 정량적인 수치로 전체 데이터의 특징을 요약하거나 이해하기 쉬운 간단한 그래프를 사용

# 대표적인 통계량 : 평균, 표준편차
# 탐색적 데이터 분석

# ## 기술통계 구하기

# In[1]:


import gdown

gdown.download('https://bit.ly/3736JW1', 'ns_book6.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book6 = pd.read_csv('ns_book6.csv', low_memory=False)
ns_book6.head()


# In[3]:
# describe() : 몇 가지 기술통계를 자동으로 추출

ns_book6.describe()


# In[4]:


sum(ns_book6['도서권수']==0) # 3206


# In[5]:


ns_book7 = ns_book6[ns_book6['도서권수']>0]


# In[6]:

# 30%, 60%, 90% 값 보기
ns_book7.describe(percentiles=[0.3, 0.6, 0.9])


# In[7]:

# 열의 데이터 타입이 수치가 아닌 데이터 타입의 열의 기술 통계
ns_book7_object_describe = ns_book7.describe(include='object')


# ## 평균

# $평균 = \dfrac{a + b + c}{3}$
# 
# $평균 = \dfrac{x_1 + x_2 + x_3}{3}$

# In[8]:


x = [10, 20, 30]
sum = 0
for i in range(3):
    sum += x[i]
print("평균:", sum / len(x))


# $평균 = \dfrac{x_1 + x_2 + x_3}{3} = \dfrac{\sum_{i=1}^{3} x_i}{3}$
# 
# $평균 대출건수 = \dfrac{\sum_{i=1}^{376770} x_i}{376770}$

# In[9]:


ns_book7['대출건수'].mean() # 11.593438968070707


# ## 중앙값

# In[10]:


ns_book7['대출건수'].median() # 6.0


# In[11]:


temp_df = pd.DataFrame([1,2,3,4])
temp_df.median()
# 0    2.5
# dtype: float64


# In[12]:


ns_book7['대출건수'].drop_duplicates().median() # 183.0
ns_book7_unique = ns_book7['대출건수'].drop_duplicates()
ns_book7_unique.median()

# 중복된 값 제거 후 중앙값이 크게 상승함 :
    # 작은 대출건수에 중복된 행이 많다고 생각할 수 있다.


# ## 최솟값, 최댓값

# In[13]:


ns_book7['대출건수'].min() # 0


# In[14]:


ns_book7['대출건수'].max() # 1765


# ## 분위수

# In[15]:

# 분위수(quantile) : 데이터를 순서대로 늘어 놓았을 때 이를 균등한 간격으로 나누는 기준점.

# 하위 25%에 위치한 값 추출
ns_book7['대출건수'].quantile(0.25) # 2.0


# In[16]:


ns_book7['대출건수'].quantile([0.25,0.5,0.75])
# 0.25     2.0
# 0.50     6.0
# 0.75    14.0
# Name: 대출건수, dtype: float64


# In[17]:

# 시리즈 객체를 정의한 후 분위수 구하기
pd.Series([1,2,3,4,5]).quantile(0.9) # 4.6


# In[18]:


4 + (0.9-0.75)*(5-4)/(1.0-0.75) # 4.6


# In[19]:
# 보간(interpolation)

# quantile(..., interpolation=...)
# 'midpoint' = 분위수에 상관없이 무조건 두 수 사이 중앙값 사용
pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='midpoint')


# In[20]:

# 'nearest' = 두 수 중에서 가까운 값을 선택.
pd.Series([1,2,3,4,5]).quantile(0.9, interpolation='nearest') # 5(0.9가 1.0에 더 가까우므로)


# In[21]:

    # 대출건수 10이 위치한 백분위를 찾는 법은?

borrow_10_flag = ns_book7['대출건수'] < 10


# In[22]:


borrow_10_flag.mean() # 0.6402712530190833


# In[23]:


ns_book7['대출건수'].quantile(0.65) # 10


# ## 분산 : 평균으로부터 데이터가 얼마나 퍼져있는지를 나타내는 통계량

# 편차 : 평균을 뺀 값
# 분산 : 편차 제곱의 평균
# 각 값에서 평균을 뺀 다음 제곱한 후 평균처럼 샘플 개수로 나누어 구할 수 있다.
# 수식 기호 s^2

# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}$
# 
# $ \bar{x} = \dfrac{\sum_{i=1}^n x_i}{n}$

# In[24]:

# var() : 분산 계산하는 함수.

ns_book7['대출건수'].var() # 371.69563042906674


# ## 표준 편차 : 분산의 제곱근. 수식 기호 s

# $ s = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}}$

# In[25]:

# std() : 표준편차를 계산하는 함수.

ns_book7['대출건수'].std() # 19.279409493785508

# %%
# var()로 표준편차를 구한다면?
s = ns_book7['대출건수'].var() # 371.69563042906674
s ** 0.5 # 19.279409493785508
# $\sqrt{4}=2$

# In[26]:

# std()를 코드로 구현해보기.

import numpy as np

diff = ns_book7['대출건수'] - ns_book7['대출건수'].mean()

np.sqrt( np.sum(diff**2) / (len(ns_book7)-1) ) # 19.279409493785508


# ## 최빈값 : 데이터에서 가장 많이 등장하는 값

# In[27]:

# mode() : 최빈값 계산하는 함수
ns_book7['도서명'].mode()

# 0    승정원일기
# Name: 도서명, dtype: object


# In[28]:


ns_book7['발행년도'].mode()
# 0    2012.0
# Name: 발행년도, dtype: float64


# ## 데이터프레임에서 기술통계 구하기

# numeric_only=True : 수치형 열만 연산할 수 있기 때문에 해당 열에만 적용되도록 
# 지정하지 않을 경우, 모든 데이터 타입의 열에 대해 수행하기 때문에 시간이 매우 오래 걸리며 경고 발생.

# In[29]:


ns_book7.mean(numeric_only=True)
# 번호      202977.476649
# 발행년도      2008.460076
# 도서권수         1.145540
# 대출건수        11.593439
# dtype: float64

# In[30]:


ns_book7.loc[:, '도서명':].mode()

#      도서명             저자   출판사    발행년도  ... 주제분류번호 도서권수 대출건수        등록일자
# 0  승정원일기  세종대왕기념사업회 [편]  문학동네  2012.0  ...  813.6    1    0  1970-01-01

# [1 rows x 12 columns]

# 이 결괏값만 보고 승정원일기가 문학동네 출판사의 도서라고 오해하면 안됨!
# 출력 결과물 사이에는 서로 연관이 없음!!

# In[31]:


ns_book7.to_csv('ns_book7.csv', index=False)


# ## 넘파이의 기술통계 함수

# ### 평균 구하기

# In[32]:


import numpy as np

np.mean(ns_book7['대출건수']) # 11.593438968070707
# pd.mean()과 동일한 결과.


# $\dfrac{국어점수 \times 2 + 수학점수}{3}$
# 
# $\dfrac{국어점수 \times 국어가중치 + 수학점수 \times 수학가중치}{국어가중치 + 수학가중치}$ 
# 
# $가중평균 = \dfrac{x_1 \times w_1 + x_2 \times w_2}{w_1 + w_2} = \dfrac{\sum_{i=1}^{2} x_i \times w_i}{\sum_{i=1}^{2} w_i}$

# In[33]:

# average() : mean()과 동일하게 평균 계산.
# weights : 가중치 파라미터.
# 

np.average(ns_book7['대출건수'], weights=1/ns_book7['도서권수']) # 10.543612175385386


# In[34]:

# 여러 권을 보유한 도서와 그렇지 않은 도서를 공정하게 다루기 위해
# 대출건수를 도서권수로 나눌 수 있음.
# 모든 도서의 권수가 1일 때 대출건수는?
np.mean(ns_book7['대출건수']/ns_book7['도서권수']) # 9.873029861445774


# In[35]:

# 전체 대출건수의 합 / 전체 도서권수 :
    # 도서에 상관없이 한 권 당 대출건수 구하기.
ns_book7['대출건수'].sum()/ns_book7['도서권수'].sum() # 10.120503701300958


# ### 중앙값 구하기

# In[36]:
# pd.median()과 동일한 값

np.median(ns_book7['대출건수']) # 6.0


# ### 최솟값, 최댓값 구하기

# In[37]:


np.min(ns_book7['대출건수']) # 0


# In[38]:


np.max(ns_book7['대출건수']) # 1765


# ### 분위수 구하기

# In[39]:


# interpolation 매개변수가 numpy 1.22(python >= 3.8) 버전부터 method로 바뀜
np.quantile(ns_book7['대출건수'], [0.25,0.5,0.75]) # array([ 2.,  6., 14.])



# ### 분산 구하기

# In[40]:


np.var(ns_book7['대출건수']) # 371.6946438971496

# pd.var()과의 차이점은?
ns_book7['대출건수'].var() # 371.69563042906674
# 소수점 셋째 자리부터 차이가난다.

# n-1 자유도 :
# 판다스의 계산식의 분모가 n이 아니라 n-1이기 때문에 발생하는 차이.
# 표본집단, 모집단
# 표본집단은 평균과 n-1개의 샘플 데이터를 알고 있다면 마지막 한 개의 샘플 값을 자동으로 알 수 있음.
# => '자유도가 n-1이다'
# 따라서 분산을 계산할때 분모를 n이 아닌 n-1로 나눔.
# https://wscode.tistory.com/74
# 분산의 과소평가 문제

# 넘파이의 var() 함수는 n으로 나눈다.
# 표본집단으로 모집단의 특징을 추정하려한다 -> n-1 (판다스)
# 단순히 일련의 데이터에 대한 분산을 계산하고 싶다 -> n (넘파이)

# $ s^2 = \dfrac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$

# In[41]:

# ddof= : 자유도 차감값 지정.
# pd.var(..., ddof=1)
ns_book7['대출건수'].var(ddof=0) # 371.6946438971496


# In[42]:

# np.var(..., ddof=0)
np.var(ns_book7['대출건수'], ddof=1) # 371.69563042906674


# ### 표준 편차 구하기

# In[43]:

# 분산과 마찬가지로 판다스와 자유도 차감값이 다름.
np.std(ns_book7['대출건수']) # 19.27938390865096


# ### 최빈값 구하기

# In[44]:

# unique() : 배열에서 고유한 값 찾는 함수.
# return_counts= : 고유한 값의 등장 횟수 반환.

values, counts = np.unique(ns_book7['도서명'], return_counts=True)
max_idx = np.argmax(counts) # 가장 큰 값의 인덱스
values[max_idx] # '승정원일기'


# ## 확인문제

# %%
# #### 3.
a = [1, 10, 3, 6, 20]
df = pd.DataFrame(a)

df.var()
df.std()


# #### 4.

# In[45]:

# 평균 대출 건수가 가장 높은 10개의 출판사를 추출하라
ns_book7[['출판사','대출건수']].groupby('출판사').mean().sort_values('대출건수', ascending=False).head(10)


# #### 5.

# In[46]:

# 문제 5. 다음은 25%와 75% 경계에 해당하는 대출건수를 찾아 이 범위에 속한 도서가 전체 도서 중 몇퍼센트인가?

target_range = np.array(ns_book7['대출건수'].quantile(q=[0.25,0.75]))
target_bool_idx = (ns_book7['대출건수'] >= target_range[0]) & (ns_book7['대출건수'] <= target_range[1])
target_bool_idx.sum()/len(ns_book7)*100

# 51.51737134060568

# %%
target_range = list(ns_book7['대출건수'].quantile(q=[0.25,0.75]))
target_bool_idx = (ns_book7['대출건수'] >= target_range[0]) & (ns_book7['대출건수'] <= target_range[1])
target_bool_idx.sum()/len(ns_book7)*100

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:03:38 2024

@author: jcp
"""

# 07 검증하고 예측하기

# 학습목표 :
    # 통계적 추정에 해당하는 가설검정, 순열검정 등을 배운다.
    # 머신러닝 모델을 사용해 미래 샘플에 대한 예측을 만드는 방법을 배운다.
    
# 07-1 통계적으로 추론하기

# 모수검정 : 모집단에 대한 파라미터를 추정하는 방법

    # 파라미터 : 평균, 분산 등
    # 모집단 : 관심 대상이 되는 전체 데이터

    # 표본 : 모집단에서 선택한 일부 샘플

    # 어떤 가정을 전제로 하고 수행되는 경우가 많다.
    # ex) 정규분포를 따른다
    
# %%
# 표준점수 구하기

# 표준점수(z 점수) : 
    
    # 데이터가 정규분포를 따른다고 가정하고, 각 값이 평균에서 얼마나 떨어져 있는지 표준편차를 사용해 변환한 점수
    # z 점수 : 평균까지 거리를 표준편차로 나눈 것.
    # z = (x - 평균) / 표준편차
    # 데이터 분포를 가늠할 수 있다.

# %%    # 
# z 점수 구하기 - 넘파이
import numpy as np

x = [0, 3, 5, 7, 10]

s = np.std(x)
m = np.mean(x)
z = (7 - m) / s
print(z) # 0.5872202195147035

# %%
# z 점수 구하기 - scipy
from scipy import stats

stats.zscore(x) # array([-1.46805055, -0.58722022,  0.        ,  0.58722022,  1.46805055])
# 배열 x에 대한 모든 z 점수를 계산하여 배열로 반환

# %%
# 누적분포 이해하기
# 표준정규분포 : 
    # 평균=0, 표준편차=1인 정규분포
    # z = x  -> z 점수를 사용해 전체 데이터가 어떻게 분포되어 있는지 나타낼 수 있음.

# 누적분포 구하기
# 어떤 z 점수 이내의 샘플 비율 계산
# %%
# stats 모듈의 norm.cdf()
# 표준정규분포에서 평균 0까지의 누적분포는?
stats.norm.cdf(0) # 0.5

# %%
# z=1 이내의 비율을 구하려면?
# (z = 1 까지 누적분포) - (z = -1 까지의 누적분포)
# 표준편차 1까지의 면적 - 표준편차 -1 까지의 면적
stats.norm.cdf(1.0) - stats.norm.cdf(-1.0) # 0.6826894921370859

# %%
stats.norm.cdf(1.0) # 0.8413447460685429
# %%
stats.norm.cdf(-1.0) # 0.15865525393145707
# %%
# 표준편차 2 이내의 비율
stats.norm.cdf(2.0) - stats.norm.cdf(-2.0) # 0.9544997361036416

# %%
# 전체에서 특정 비율에 해당하는 z 점수 구하기
# norm.ppf()
# 90% 누적분포에 해당하는 z 점수는?
stats.norm.ppf(0.9) # 1.2815515655446004

# %%
# 중심극한정리 : 
    # '무작위로 샘플을 뽑아 만든 표본의 평균은 정규분포에 가깝다'는 이론


# %%
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)
# %%
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()

# %%
import matplotlib.pyplot as plt

plt.hist(ns_book7['대출건수'], bins=50)
plt.yscale('log')
plt.show()
# 정규분포와 상당히 거리가 멀다

# %%
# 샘플링하기
# 무작위로 1000개의 표본을 샘플링하여 각 평균을 리스트로 저장
# 샘플링을 위해 sample() 사용
# 이어서 mean() 사용하여 샘플링 결과의 평균 계산
# .sample().mean()

np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(30).mean()
    sample_means.append(m)

# %%
plt.hist(sample_means, bins=30)
plt.show()
#  종모양과 유사한 분포 형성

# %%
# 샘플링 크기와 정확도
# 실제 모집단의 통계량과 얼마나 일치할까?
np.mean(sample_means) # 11.539900000000001

# %%
ns_book7['대출건수'].mean() # 11.593438968070707

# 소수점 첫째 자리까지 같음.
# %%
# 샘플링 크기 20으로 평균 계산
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(20).mean()
    sample_means.append(m)
# %%
np.mean(sample_means) # 11.39945

# %%
# 샘플링 크기 40으로 평균 계산
np.random.seed(42)
sample_means = []
for _ in range(1000):
    m = ns_book7['대출건수'].sample(40).mean()
    sample_means.append(m)
# %%
np.mean(sample_means) # 11.5613
# 더욱 평균 11.59에 가까워짐.

# %%
# 표본 평균의 표준편차가 모집단의 표준편차를 표본 크기의 제곱근으로 나눈 것에 가깝다.
# 표준오차 : 표본 평균의 표준편차.
np.std(sample_means) # 3.0355987564235165

# %%
# 모집단 표준편차 / 표본 크기의 제곱근
np.std(ns_book7['대출건수']) / np.sqrt(40) # 3.048338251806833

# %%
# 모집단의 평균 범위 추정하기 : 신뢰구간
# 신뢰구간 : 
    # 표본의 파라미터가 속할 것이라 믿는 모집단의 파라미터 범위

# 파이썬 도서 대출건수를 사용해 신뢰구간 계산하기:
    # 전체 데이터프레임에서 컴퓨터 관련 도서 중 파이썬 도서만 골라내기
    # 컴퓨터 관련 도서 주제분류번호 : 003, 004, 005
    # 도서명 '파이썬'이 포함됨.

# %%
python_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
        ns_book7['도서명'].str.contains('파이썬')
python_books = ns_book7[python_books_index]
python_books.head()

# %%
# 모두 몇권인가
len(python_books) # 251

# %%
# 대출건수 평균 계산
python_mean = np.mean(python_books['대출건수'])
python_mean # # 14.749003984063744

# 평균 대출건수 14회 이상.
# z 점수 공식과 중심극한정리를 연결하여 예측해본다면?
# 모집단의 평균 = 14.75 - z * 표본오차(=모집단의 표준편차 / 표본크기의 제곱근)
# %%
# 표준오차 계산
python_std = np.std(python_books['대출건수'])
python_se = python_std / np.sqrt(len(python_books))
python_se # 0.8041612072427442

# %%
# 표본의 평균이 모집단 평균을 중심으로 95% 이내 구간에 포함된다고 가정
stats.norm.ppf(0.975) # 1.959963984540054
# %%
stats.norm.ppf(0.025) # -1.9599639845400545
# 정규분포는 대칭이기 때문에 두 점수가 부호만 다르고 같음.

# %%
# 표준오차 * z
print(python_mean - python_se * 1.96, python_mean - python_se * -1.96) 
# 13.172848017867965 16.325159950259522
# -> 모집단 평균이 13.2에서 16.3 사이에 놓여 있을거라 95% 확신
# 95% 신뢰구간에서 파이썬 도서의 모집단 평균이 13.2에서 16.3 사이에 놓여 있다.

# %%
# 통계적 의미 확인하기 : 가설검정
# 가설검정 :
    # 표본에 대한 정보를 사용해 모집단의 파라미터에 대한 가정을 검정하는 것
    # 영가설(null hypothesis) = 귀무가설 : 표본 사이에 통계적으로 의미 없다고 예상되는 가설
    # 대립가설 : 표본 사이에 통계적인 차이가 있다는 가설
    
# 유의수준 : 정규분포의 양쪽 꼬리 면적의 합이 5%가 되는 지점

# %%
# z 점수로 가설 검증하기
# c++ 도서 표본추출
cplus_books_index = ns_book7['주제분류번호'].str.startswith('00') & \
                    ns_book7['도서명'].str.contains('C++', regex=False)
cplus_books = ns_book7[cplus_books_index]
cplus_books.head()
# %%
len(cplus_books) # 89

# %%
# 평균 대출건수 확인
cplus_mean = np.mean(cplus_books['대출건수'])
cplus_mean # 11.595505617977528
# 파이썬 도서의 14.75와 차이가 있다.

# %%
# 표준오차 계산
cplus_se = np.std(cplus_books['대출건수'])/ np.sqrt(len(cplus_books))
cplus_se # 0.9748405650607009

# %%
# 가설검정 공식에 대입
(python_mean - cplus_mean) / np.sqrt(python_se**2 + cplus_se**2) # 2.495408195140708

# %%
# 누적분포 확인
stats.norm.cdf(2.50) # 0.9937903346742238

# 5% 이하로 유의수준 이하로 영가설 기각.
# 대립가설 : 파이썬과 C++ 도서의 평균에 차이가 있다.

# %%
# t-검정으로 가설 검증하기

# ttest_ind() :
    # 두 표본의 평균을 비교하는 함수
    # t-분포인 두 표본을 비교하는 t-검정을 수행
    
# t-분포 : 
    # 정규분포와 비슷하지만, 중앙은 조금 더 낮고 꼬리가 더 두꺼운 분포
    # 표분 크기가 30 이하일때 사용하는 것이 좋음
    # 표본 크기가 30 이상이면 정규분포와 매우 비슷해짐.
    # -> 표본 크기에 상관없이 평균을 비교할 수 있음.
    
# %%

t, pvalue = stats.ttest_ind(python_books['대출건수'], cplus_books['대출건수'])
print(t, pvalue) # 2.1390005694958574 0.03315179520224784

# %%
# 정규분포가 아닐 때 가설 검증하기: 순열검정

# 순열검정 : 
    # 모집단의 분포가 정규분포를 따르지 않거나 모집단의 분포를 알 수 없을 때 사용
    # 비모수검정 방법 : 모집단의 파라미터를 추정하지 않는다.
    # 두 표본의 평균의 차이를 계산한 후 두 표본을 섞어 무작위 2개 그룹(원래 표본 크기와 동일)으로 나눔.
    # 이 두 그룹에서 다시 평균의 차이를 계산
    # 이 과정을 여러 번 반복해서 원래 표본의 평균 차이가 무작위 그룹의 평균 차이보다 크거나 작은 경우를 헤아려 p-값 계싼
    
# %% 
# 도서 대출건수 평균 비교(1) : 파이썬 vs C++

def statistic(x, y):
    return np.mean(x) - np.mean(y)

# %%
def permutation_test(x, y):
    # 표본의 평균 차이를 계산
    obs_diff = statistic(x, y)
    # 두 표본을 합하기
    all = np.append(x, y)
    diffs = []
    np.random.seed(42)
    # 순열검정 1000번 반복
    for _ in range(1000):
        # 전체 인덱스 섞기
        idx = np.random.permutation(len(all))
        # 랜덤하게 두 그룹으로 나눈 후 평균 차이 계산
        x_ = all[idx[:len(x)]]
        y_ = all[idx[len(x):]]
        diffs.append(statistic(x_, y_))
    # 원본 표본보다 작거나 큰 경우의 p-값을 계산
    less_pvalue = np.sum(diffs < obs_diff)/1000
    greater_pvalue = np.sum(diffs > obs_diff)/1000
    # 둘 중 작은 p-값을 선택해 2를 곱하여 최종 p-값 반환
    return obs_diff, np.minimum(less_pvalue, greater_pvalue) * 2
# 일반적으로 영가설을 기각하는 것이 목적이므로 둘 중에 작은 값을 택하고 2를 곱해 양쪽 꼬리에 해당하는 비율 얻기
# = 영가설이 옳다고 가정했을 때 이런 데이터가 관측될 확률
# %%
permutation_test(python_books['대출건수'], cplus_books['대출건수']) # (3.1534983660862164, 0.022)
# 두 도서의 평균 대출건수에는 차이가 있다.

# %%
res = stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']), statistic, random_state=42)
print(res.statistic, res.pvalue) # 3.1534983660862164 0.0258

# %%
res = stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']), lambda x,y: np.mean(x)-np.mean(y), random_state=42)
print(res.statistic, res.pvalue) # 3.1534983660862164 0.0258

# %%
# 도서 대출건수 평균 비교(2) : 파이썬 vs 자바스크립트

java_books_idx = ns_book7['주제분류번호'].str.startswith('00') & \
                ns_book7['도서명'].str.contains('자바스크립트')
java_books = ns_book7[java_books_idx]
java_books.head()

# %%
print(len(java_books), np.mean(java_books['대출건수'])) # 105 15.533333333333333
print(java_books['대출건수'].mean()) # 15.533333333333333

# %%
permutation_test(python_books['대출건수'], java_books['대출건수']) # (-0.7843293492695889, 0.566)
# p-값이 0.05보다 훨씬 큼 
# - 영가설을 기가할 수 없음
# 파이썬과 자바스크립트 도서 사이의 평균 대출건수 차이는 큰 의미가 없다.
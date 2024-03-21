# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:52:03 2024

@author: jcp
"""

# [문제]
# 데이터프레임을 이용하여 총점과 평균을 구하라.
# 1. '이름'을 인덱스로 지정
# 2. 각 학생의 총점과 평균
# 3. 각 과목별 총점과 평균
# 4. 처리 결과를 전체의 새로운 하나의 프레임으로 구성

# 결과예시:
# 이름 수학 영어 음악 체육 총점 평균
# 서준   90   98   80  100  373   93
# 준서   90   98   80  100  373   93
# 인아   90   98   80  100  373   93
# 수성   90   98   80  100  373   93
# 총점  360  392  320  400    0    0
# 평균   90   98   80  100    0    0

# 조건:
    # 1. 반복문을 사용하라
    # 2. 각 행과 열을 하나씩 읽어서 처리
    
# %%
import pandas as pd
# df=pd.read_csv('score.txt')
# print(df)
data = [
        [90, 98, 80, 100],
        [90, 98, 80, 100],
        [90, 98, 80, 100],
        [90, 98, 80, 100],
        ]

df = pd.DataFrame(data)
print(df)

# %%
# 1. 이름을 인덱스로 지정
df.index = ['서준','준서','인아','수성']
# df = df.set_index('이름')
df
# %%
# 2. 각 학생의 총점과 평균
df.columns = ['수학','영어','음악','체육']
df

# df.loc['서준']['수학'] = 11
# 연쇄 할당은 위험합니다! ['서준','수학']
for student in df.index:
    tot = 0    
    
    for i in ['수학', '영어','음악','체육']:
        tot += int(df.loc[student,i])
        
    df.loc[student,['총점','평균']] = [tot, tot//4]
    
df['총점'] = df['총점'].astype(int)    
df['평균'] = df['평균'].astype(int)
print(df)    

# %%
# 3. 각 과목별 총점과 평균
for col in df.columns:
    tot = 0
    
    for student in ['서준','준서','인아','수성']:
        tot += int(df.loc[student, col])
        
    df.loc['총점',col] = tot
    df.loc['평균',col] = tot // 4
    
df['총점'] = df['총점'].astype(int)
df['평균'] = df['평균'].astype(int)
print(df)

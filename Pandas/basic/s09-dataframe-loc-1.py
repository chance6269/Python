# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:18:32 2024

@author: jcp
"""

# df = pd.DataFrame(data[, ])
import pandas as pd

# list
data = [
        [14,'남','한양대'],
        [15,'남','장안중'],
        [16,'여','수성중'],
        [17,'여','수원대']
        ]

df = pd.DataFrame(data, index=['길동','정윤','희애','유라'],
                  columns=['나이','성별','학교'])
print(df)
#     나이 성별   학교
# 길동  14  남  한양대
# 정윤  15  남  장안중
# 희애  16  여  수성중
# 유라  17  여  수원대
# %%

# 단일행 선택
# loc : 인덱스 선택
# 결과 : Series
df1 = df.loc['희애']
print(df1) # Series
# 나이     16
# 성별      여
# 학교    수성중
# Name: 희애, dtype: object

# %%

# 단일행 선택
# 결과 : DataFrame
df2 = df.loc[['희애']]
print(df2) # DataFrame
#     나이 성별   학교
# 희애  16  여  수성중

# %%

# 다중행 선택[범위지정]
# loc : 인덱스, 슬라이싱
# 결과 : DataFrame
df3 = df.loc['정윤':'희애']
print(df3)
#     나이 성별   학교
# 정윤  15  남  장안중
# 희애  16  여  수성중

# %%

# 다중행 선택
# loc : 멀티 인덱스 지정
# 결과 : DataFrame(지정된 순서로)
df4 = df.loc[['정윤','희애','길동']]
print(df4)
#     나이 성별   학교
# 정윤  15  남  장안중
# 희애  16  여  수성중
# 길동  14  남  한양대
# %%

# 순번과 칼럼을 동시에 지정
# 전체행을 선택, 칼럼은 '성별','학교'선택
# 행의 범위와 열의 범위를 동시 지정
df5 = df.loc[:,['성별','학교']]
# df5 = df.iloc[:,1:3]
print(df5)

# %%
df6 = df.loc['정윤':'유라',['성별','학교']]
print(df6)
#    성별   학교
# 정윤  남  장안중
# 희애  여  수성중
# 유라  여  수원대

# %%
df7 = df.loc[:,:]
print(df7)
print(df)
print(df7==df)
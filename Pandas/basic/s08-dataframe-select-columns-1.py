# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:48:06 2024

@author: Solero
"""

# 판다스 : DataFrame

# 데이터프레임 칼럼 참조, 인덱스 참조

#%%


#%%
import pandas as pd

# list
data = [
    # 0   1     2        
    [15, '남', '장안중'], # 0 행
    [16, '여', '수성중'], # 1 행
    [17, '여', '수원대']  # 2 행
]

df = pd.DataFrame(data, index=['정윤', '희애', '유라'], 
                  columns=['나이', '성별', '학교'])
print(df)
"""
    나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
유라  17  여  수원대
"""

#%%

# 시리즈처럼 인덱스 참조를 할 수 없다.
# KeyError: '정윤'
# print(df['정윤'])   

# KeyError: "None of [Index(['정윤'], dtype='object')] are in the [columns]"
# print(df[['정윤']]) 


#%%

# 칼럼 참조 : '나이' 칼럼의 모든 행을 참조
# 결과 : Series
age_sr = df['나이']
print(age_sr) # Series

#%%

# 칼럼 참조 : '나이' 칼럼의 모든 행을 참조
# 결과 : DataFrame
age_df = df[['나이']]
print(age_df) # DataFrame

#%%
 
# 다중 칼럼 참조 : '나이', '성별' 칼럼의 모든 행을 참조
# 결과 : DataFrame
age_sex = df[['나이', '성별']]
print(age_sex) # DataFrame

#%%
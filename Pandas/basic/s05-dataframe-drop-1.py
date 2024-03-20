# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:48:06 2024

@author: Solero
"""

# 판다스 : DataFrame

# 형식:
# df = pd.DataFrame(data[, index=index_data, columns=columns_data])

# 행/열 삭제(drop)

#%%


#%%
import pandas as pd

# list
data = [
    # 0   1     2        
    [15, '남', '장안중'], # 0 행
    [16, '여', '수성중']  # 1 행
]

df = pd.DataFrame(data, index=['정윤', '희애'], 
                  columns=['나이', '성별', '학교'])
print(df)
"""
    나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
"""

#%%

# 행 삭제 : axis = 0
ndf = df.drop('희애') # 기본값 생략
print(ndf)

ndf = df.drop('희애', axis=0)
print(ndf)

#%%

# 열 삭제 : axis = 1
ndf = df.drop('학교', axis=1)
print(ndf)
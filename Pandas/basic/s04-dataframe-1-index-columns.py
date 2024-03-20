# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:18:32 2024

@author: jcp
"""
# 판다스 : DataFrame

# 형식:
# df = pd.DataFrame(data[, index=index_data, columns=columns_data])

#%%
import pandas as pd

# list
data = [
        [15, '남', '장안중'],
        [16, '여', '수성중']
        ]

df = pd.DataFrame(data)
print(df)
#     0  1    2
# 0  15  남  장안중
# 1  16  여  수성중

# %%

# 새로운 인덱스 지정
df.index = ['정윤','희애']

# 새로운 칼럼 지정
df.columns = ['나이', '성별', '학교']
print(df)

#     나이 성별   학교
# 정윤  15  남  장안중
# 희애  16  여  수성중
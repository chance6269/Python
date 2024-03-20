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

# reset_index()
# index가 칼럼으로 이동하여 새로운 칼럼이 생성
# index : 0부터 순번 부여 된다.
ndf = df.reset_index()
print(ndf)


#%%

# set_index() : 칼럼을 index로 이동(변경)하고 기존 인덱스는 삭제
xdf = ndf.set_index('index')

#%%
ydf = xdf.set_index('학교')
print(ydf)
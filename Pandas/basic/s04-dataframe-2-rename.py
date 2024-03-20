# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:18:32 2024

@author: jcp
"""

import pandas as pd

# list
data = [
        [15, '남', '장안중'],
        [16, '여', '수성중']
        ]

df = pd.DataFrame(data, index=['정윤','희애'],
                  columns=['나이','성별','학교'])
print(df)
#     나이 성별   학교
# 정윤  15  남  장안중
# 희애  16  여  수성중

# %%

# 인덱스 변경
# 결과 : 새로운 데이터프레임 생성
ndf = df.rename(index={'희애':'정희'})
print(ndf)

#     나이 성별   학교
# 정윤  15  남  장안중
# 정희  16  여  수성중
# %%
ndf = df.rename(columns={'학교':'중학교'})
print(ndf)

#     나이 성별  중학교
# 정윤  15  남  장안중
# 희애  16  여  수성중
# %%

# 원본 변경 : inplace=True
ndf.rename(index={'정윤':'신정윤', '희애':'신정희'},
           columns={'나이':'연령'}, inplace=True)

print(ndf)
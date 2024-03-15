# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:31:35 2024

@author: jcp
"""

student = {
    'name': '홍길동',
    'age':34,
    '주소':'한양',
    '생존':False
    }

print(student)

#%%

# Value 리스트 만들기 : dict.values()
# 값 목록을 얻기
dv = student.values()
print(dv) # dict_values(['홍길동', 34, '한양', False])

# %%

# dict.values()를 튜플로 전환
tv = tuple(dv)
print(tv) # ('홍길동', 34, '한양', False)

dvc = dv
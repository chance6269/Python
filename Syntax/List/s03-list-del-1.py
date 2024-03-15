# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:37:32 2024

@author: jcp
"""
# 리스트 삭제
# del 명령어
# 함수가 아니다.
# del list[index]
# del list[start:end]


a = [1,2,3,4,5,[70,80,90]]

# 리스트 요소 삭제
# del a[-1]
print(a) # [1, 2, 3, 4, 5]

# %%
# 슬라이싱 기법으로 삭제
del a[2:4]
print(a) # [1, 2, 5]


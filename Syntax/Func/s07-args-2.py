# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:52:05 2024

@author: jcp
"""

# 함수(Function)
# 가변인자
# 인자의 갯수가 가변일 때

# %%
# 가변인자로 전달하면 튜플로 받음
# 가변인자형은 파라미터 변수 앞에 (*)를 붙임
def tots(title,*vals):
    print(f"[{title}] {vals}", end=": ") # tuple
    tot = 0
    for val in vals:
        if isinstance(val, int): # 정수인 경우에만 계산.
            tot += val
    return tot
    
# %%

print(tots(10))
print(tots(10,20))
print(tots(10,20,30))

# %%
tots(99,)
print(tots((99,))) # 0

# %%

# 튜플을 인자로 보내면
# 튜플이 하나의 인자로 전달(3개의 인자가 아닌)
tots((10,20,30))

# %%
print(tots('홍길동',10,20)) # 30
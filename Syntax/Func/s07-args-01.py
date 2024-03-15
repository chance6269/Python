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
# 가변 파라미터 앞에 일반 파라미터 지정 가능
# def tots(*vals, title): # 오류
def tots(title, *vals):
    print(f"[{title}] {vals}", end=": ") # tuple
    tot = 0
    for val in vals:
            tot += val
    return tot
    
# %%

# 가변인자로 호출
print(tots("홀수",1,3,5,7,9))
print(tots("짝수",2,4,6,7,10))

# %%
tots(99,)
print(tots((99,))) # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

# %%

# 튜플을 인자로 보내면
# 튜플이 하나의 인자로 전달(3개의 인자가 아닌)
tots((10,20,30))
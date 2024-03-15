# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:39:14 2024

@author: jcp
"""

# 람다함수 응용

# %%

# 파라미터
# what: 문자열
# func: 함수
# vals: 가변인자(계산할 데이터)

def calc(what, func, *vals):
    print(f"calc({what}): ", func(*vals))
    
# %%

def add(*vals):
    tot = 0
    for val in vals:
        tot += val
    return tot

# 함수를 변수에 할당
fun = add
print("add:", add(1,2,3,4,5))
print("fun:", fun(1,2,3,4,5))

# %%
calc("홀수", add, 1,3,5,7,9)
calc("짝수", add, 2,4,6,8,10)
    
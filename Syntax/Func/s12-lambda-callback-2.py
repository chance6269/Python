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

def calc(what, func, a, b):
    print(f"calc({what}): ", func(a, b))
    
# %%
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

# %%
calc("덧셈", add, 10, 20) # 30
calc("뺄셈", sub, 10, 6) # 4
calc("곱셈", mul, 10, 3) # 30

# %%

# 람다함수 사용
calc("덧셈", lambda a, b: a + b, 10, 20) # 30
calc("뺄셈", lambda a, b: a - b, 10, 6) # 4
calc("곱셈", lambda a, b: a * b, 10, 3) # 30
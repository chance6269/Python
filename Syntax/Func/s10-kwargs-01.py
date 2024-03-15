# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:28:51 2024

@author: jcp
"""

# 함수(Function)

# 키워드 매개변수(kwargs)
# 호출할 때 반드시 인자에 키를 명시해아 한다.
# 인자 : 키=값

# %%

# 파라미터 : dict로 받음
def move(**kwargs):
    print(f"[move] type({type(kwargs)}): {kwargs}")
    for key in kwargs.keys():
        print(f"key={key}, value={kwargs[key]}")
    
# %%
# move(1,2,3) # TypeError: move() takes 0 positional arguments but 3 were given

# %%

move(x=10, y=20, z=30) # [move] type(<class 'dict'>): {'x': 10, 'y': 20, 'z': 30}
move(a=10, b=20, c=30) # [move] type(<class 'dict'>): {'a': 10, 'b': 20, 'c': 30}
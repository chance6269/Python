# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:14:28 2024

@author: jcp
"""

# 함수형 프로그래밍(Functional Programming)

# 자료 처리를 수학적 함수의 계산으로 취급하고
# 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임 중 하나

# %%

def score(name):
    print(f"[score] name({name})")
    
    def minmax(*args):
        min = args[0]
        max = args[0]
        
        for val in args:
            if val < min:
                min = val
            if val > max:
                max = val
                
        return name, min, max
    
    return minmax

# %%

# 전용함수
mfunc = score("[중간고사]")
lfunc = score("[기말고사]")

print(mfunc(70,80,90))
print(mfunc(88,99,100))
print(lfunc(80,99,100))
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:42:20 2024

@author: jcp
"""

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산가능 : 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:42:20 2024

@author: jcp
"""

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산가능 : 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
# -총합누적, 평균
# -히스토리(이력)

# 전역변수
total = 0
count = 0
hists = []

# 더하기
def add(a, b):
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 나누기
def div(a, b):
    return a / b

# 곱하기
def mul(a, b):
    return a * b

# 나머지
def mod(a, b):
    return a % b

# 제곱
def square(a,b):
    return a ** b


# 평균
# def avg(nums):
#     return tot(nums) / len(nums)
def tot():
    return total

def avg():
    return total / count

def comp(a, op, b):
    if op == '+':
        c = add(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op =='%':
        c = mod(a, b)
    elif op == '**':
        c = square(a, b)
    else:
        return None
    
    return c

def recalc():
    t = 0
    for a, op, b in hists:
        c = comp(a, op, b)
        t += c
        print(f"{a} {op} {b} = {c}")
    return t, t / len(hists) # 튜플(총합, 평균)


# 계산기
def calc(a, op, b):

    c = comp(a, op, b)    
    if c == None:
        return 0
    
    # 전역변수
    global total
    global count
        
    # 누적
    count += 1 # 연산횟수 누적
    total += c # 연산결과 누적
    hists.append((a, op, b)) # 계산결과 보관
    return c # 단위연산 결과 리턴

# %%
calc(10, '+', 20)
calc(2, '*', 4)
calc(10, '/', 2)
calc(2, '**', 3)
print('총합:', total)
print('총합:', tot())
print('평균:', avg())
print('검산', recalc())
# calc() 함수에서 지원하지 않는 연산자
calc(2,  '&', 3)       # 0


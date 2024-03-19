# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:22:20 2024

@author: jcp
"""

# 1000이하의 소수를 나열하기

counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n%i == 0:
            break
    else:
        print(n)
        
print(f'나눗셈을 실행한횟수: {counter}')
# 나눗셈을 실행한횟수: 78022

# %%

counter = 0
ptr = 0 # 이미 찾은 소수 개수
prime = [None] * 500

prime[ptr] = 2 
ptr += 1

for n in range(3, 1001, 2): # 홀수만 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나누기
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1
        
for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')
# 나눗셈을 실행한 횟수: 14622

# %%
# 어떤 정수 n이 다음 조건을 만족하면 소수
# : n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다.
# = n 이하의 어떤 소수의 제곱으로도 나누어 떨어지지 않으면 소수.
counter = 0
ptr = 0 # 이미 찾은 소수 개수
prime = [None] * 500

prime[ptr] = 2 
ptr += 1


prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2): # 홀수만 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1
        
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
# 곱셈과 나눗셈을 실행한 횟수: 3774

# %%
# 어떤 정수 n이 다음 조건을 만족하면 소수
# : n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다.
counter = 0
ptr = 0 # 이미 찾은 소수 개수
prime = [None] * 500

prime[ptr] = 2 
ptr += 1


prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2): # 홀수만 대상으로 설정
    i = 1
    while prime[i] <= n ** 0.5:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1
        
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
# 곱셈과 나눗셈을 실행한 횟수: 3774

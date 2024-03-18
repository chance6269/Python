# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:32:16 2024

@author: jcp
"""

# random(), randint()
# 난수: 규칙이 없는 임의의 수

# %%

# random() : 0~1.0 사이의 값

import random

for n in range(10):
    x = random.random()
    print(x)
    
# %%

# 1부터 6까지 숫자를 20번 발생시켜라

for n in range(20):
    x = random.random()
    y = x * 6
    z = int(y) + 1
    print(f"{y:0.5f}, {x:0.5f}, {z}")
    
# %%

import math # 수학 모듈

# 0부터 10까지 숫자를 20번 발생시켜라
# 소숫점 5자리 이하 버리고 발생된 난수를 출력 : trunc()
s = 0
e = 10
m = 20
for n in range(m):
    x = random.random()
    y = x * (e-s+1)
    z = int(y)
    x = math.trunc(x) 
    print(f"{y:0.5f}, {x:.5f}, {z:2d}")
    
# %% 
# [문제]
# 1부터 45까지 난수를 발생시켜 6개의 충돌되지 않는 조합을 만들어라

# 인수로 받은 list의 0~(list length-1) 사이 랜덤한 index의 요소를 pop하여 리턴하는 함수
def random_pop(lst): 
    num = random.random() * len(lst)
    return lst.pop(int(num))
# %%

ball_box = list(range(1, 46)) # 1~45 숫자 공이 담긴 상자

lotto = [] # 로또 번호 넣을 자리
for i in range(6):
    ball_num = random_pop(ball_box) # 숫자 추출
    lotto.append(ball_num) # 로또 번호 리스트에 추가
    
print(lotto) # 로또 번호 출력
# %%

ls = 1 # 시작값
le = 45 # 종료값
lc = 6 # 갯수
lotto = [0,0,0,0,0,0] # 총 6개의 난수를 저장할 리스트

import random

for i in range(lc):
    lotto = random.sample(range(ls, le+1), 1)
    lotto.sort()
    print(f"[{i+1}] {lotto}")
    
# %%
import random
lotto = []
while True :
    x = random.random()  
    y = int((x * 45) + 1)
    if y not in lotto :
        lotto.append(y)
        if len(lotto) == 6 :
            break
    else :
        continue
    
# %%

ls = 1
le = 45
lc = 6
lotto = []

while len(lotto) < lc:
    random_integer = random.randint(ls,le)
    if random_integer not in lotto:
        lotto.append(random_integer)
print("로또 번호:", lotto)
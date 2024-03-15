# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:22:54 2024

@author: jcp
"""

# [문제]
# 문자열 변수(s)에서 't'의 위치를 모두 찾아라
# find()

s = "Python is the best choice"
print("0123456789" * 4)
print(s)

# old = s.find('t') # 2
# print("t의 첫 위치 : ",old)
old = -1
new = old
while True:
    
    new += s[old+1:].find('t')+1
    print('new : ', new)
    if new == old: # 이전 위치와 달라지지 않는다면 종료
        break
    print("t를 찾았습니다. 위치 : ",new)
    old = new
    
# %%
# [해결2]
# str.find(sub[, start[, end]])
# 결과 = 문자열. find(탐색문자열, 시작위치, 종료위치)

t1=s.find('t')
t2=s.find('t',t1+1)
t3=s.find('t',t2+1)
# new = s.find('t',old+1)
print(t1, t2, t3)

# old=s.find('t')
# print("t의 첫 위치 : ",old)
old = -1
while True:
    
    new = s.find('t',old+1)
    if new == -1:
        break
    print('new : ', new)
    print("t를 찾았습니다. 위치 : ",new)
    old = new
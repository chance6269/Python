# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:21:55 2024

@author: jcp
"""

# 튜플(Tuple)
# 불변(immutable)
# 수정(추가, 삭제, 변경) 불가
# 장점 :
    # 리스트에 비해 속도가 빠르다
    # 공간절약
# 특징 : 딕셔너리(dict) 키로 활용
# 함수의 인자로 사용

t1 = ()
t2=(1,) # 요소가 하나일때 반드시(,)를 붙여야함.
n1=(1)
print(type(t2)) #<class 'tuple'>
print(type(n1)) #<class 'int'>

# 소괄호 생략 가능
t3=1,2,3

# 한줄에 여러 변수 선언 가능
# 언패킹
a,b,c = 10, 20, 'END'
d,e,f = (a,b,c)


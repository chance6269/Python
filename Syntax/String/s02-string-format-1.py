# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:38:18 2024

@author: jcp
"""

# 문자열 포맷팅
"""
    %s : 문자열
    %c : character
    %d : 정수
    %f : float
    %o : 8진수
    %x : 16진수
    %% : Literal %(문자 % 자체)
"""
# %%

# 정수

num = 99
print("이 숫자는 정수 %d 입니다."%num)
print("이 숫자는 정수 {0} 입니다.".format(num))
print(f"이 숫자는 정수 {num} 입니다.")

# %%

a = 'a'

av = ord(a) # a의 ASCII코드 값
print(av) # 97
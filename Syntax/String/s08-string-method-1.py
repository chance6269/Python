# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:48:52 2024

@author: jcp
"""

# 문자열 삽입 
# 삽입할 문자열.join('삽입될 문자열')
# 각각 문자 사이에 삽입
",".join('abcd') # 'a,b,c,d'
",".join(['a','b','c','d']) # 'a-b-c-d'



# %%
# 공백 지우기

# 왼쪽 공백 지우기
# lstrip()
a = " hi "
a.lstrip() # 'hi '

# 오른쪽 공백 지우기 
# rstrip()
a = " hi "
a.rstrip() # ' hi'

# 양쪽 공백 지우기
# strip()

a = ' hi hi '
a.strip() # 'hi hi'


# %%

# 문자열 바꾸기
# replace(바뀔 문자열, 바꿀 문자열)
a = "Life is too short"
a.replace("Life", "Your leg") # 'Your leg is too short'



# %%

# 문자열 나누기
# split()
a.split() # ['Life', 'is', 'too', 'short']
# split(sep)
b = "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']

# %%
# [문제]
# 아래 전화번호를 공백() 대신 하이픈(-)으로 대체하라.
# 단, join()함수를 이용해서 완성하라
hp='010 1234 1234'

hp=hp.split()
'-'.join(hp)
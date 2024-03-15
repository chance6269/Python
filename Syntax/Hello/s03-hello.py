# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:38:11 2024

@author: jcp
"""

# 숫자형
x = 10
x
# 정수형
a = 123
b = -123
c = 0
print(a, b, c)

#%% 셀 분리

# 실수형
f = 1.2
p = 3.14
print(f)
print(p)

#%%

# 지수형
e1 = 4.24E10 # 42400000000.0
e2 = 4.24e-10 # 4.24e-10
print(e1)
print(e2)

#%%

e3 = 1.0E3 # 1.0 * 10^3 -> 1000.0
print(e3)

e4 = 1.0E-3 # 1.0 * 10^-3 -> 0.001
print(e4)

#%%

# 8진수(octal) : 0O, 0o
o1 = 0o177
o2 = 0O177
print(o1) # 127
print(o2) # 127

ox = 0o377 # 255
print(ox)

#%%

# 16진수(hexa-demical) : 0x
# 0123456789ABCDEF

# 8비트
h1 = 0xff
print(h1) # 255

# 4비트(nibble)
h2 = 0xf
print(h2) # 15

# 16비트
h3 = 0xffff # 65535
print(h3)
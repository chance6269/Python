# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:01:27 2024

@author: jcp
"""

# 딕셔너리 추가, 삭제
a = {1: 'a'}
a[2] = 'b'
print(a)

a[2] = 3

print(a)


print(a.get('nokey'))
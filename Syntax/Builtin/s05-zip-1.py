# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:14:32 2024

@author: jcp
"""

# zip()
# zip(*iterable)
# 여러개로 구성된 데이터를 인덱스별로 묶어서 리턴
# 최소 인덱스에 맞춰서

# %%

a = [1,2,3]
b = [1,3,5]
c = [2,4,6]

abzip = zip(a, b, c)


print(abzip)
print(list(abzip)) # [(1, 1, 2), (2, 3, 4), (3, 5, 6)]
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:15:40 2024

@author: jcp
"""

# 리스트 복사
# 얕은 복사 : 참조값만 복사

    
x = [[1,2,3], [4,5,6]]
y = x.copy()
x[0][1] = 9
x
y
# %%
# 깊은 복사 :
# 참조하는 객체 자체를 복사
# copy.deepcopy()

import copy
x = [[1,2,3], [4,5,6]]
y = copy.deepcopy(x)
x[0][1] = 9
print(x) # [[1, 9, 3], [4, 5, 6]]
print(y) # [[1, 2, 3], [4, 5, 6]]
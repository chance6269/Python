# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:45:23 2024

@author: jcp
"""

# 리스트에서 요소 꺼내기 : pop()
# 꺼낸 요소는 삭제가 된다.
# pop(0)
# 선입선출 : FIFO(First In First Out), 큐(Queue)

lst = ['삼성','SK','LG','HD']

print("# pop()")
print(lst.pop(0)) # 삼성
print(lst.pop(0)) # SK
print(lst.pop(0)) # LG
print(lst.pop(0)) # HD

print('원본:', lst) # []

# %%
print(lst.pop(0)) # IndexError: pop from empty list

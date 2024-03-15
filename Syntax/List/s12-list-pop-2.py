# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:06:38 2024

@author: jcp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:45:23 2024

@author: jcp
"""

# 리스트에서 요소 꺼내기 : pop()
# 꺼낸 요소는 삭제가 된다.
# pop()
# 후입선출 : LIFO(Last In First Out), 스택(Stack)

lst = ['삼성','SK','LG','HD']

print("# pop()")
print(lst.pop()) # HD
print(lst.pop()) # LG
print(lst.pop()) # SK
print(lst.pop()) # 삼성

print('원본:', lst) # []


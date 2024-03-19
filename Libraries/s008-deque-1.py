# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:28:46 2024

@author: jcp
"""

# - collections.deque()

# 데크(deque) : 양방향 자료형
# 스택이나 큐처럼 쓸 수 있다.

from collections import deque

a = [1,2,3,4,5]
q = deque(a)

# 회전: 시계방향

q.rotate(2)

result = list(q)
print(result) # [4, 5, 1, 2, 3]

# %%
from collections import deque
d = deque([1,2,3,4,5])
d.append(6)
d # deque([1, 2, 3, 4, 5, 6])

d.appendleft(0)
d # deque([0, 1, 2, 3, 4, 5, 6])

d.pop() # 6

d # deque([0, 1, 2, 3, 4, 5])

d.popleft() # 0

d # deque([1, 2, 3, 4, 5])
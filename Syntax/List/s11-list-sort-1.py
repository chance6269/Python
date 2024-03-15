# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:32:16 2024

@author: jcp
"""

# sort()
# 리턴 : None
# 원본이 변경. 요소의 위치가 바뀐다.
# 정렬순서 : 대문자, 소문자, 한글

score = [99, 67, 100, 56, 90, 70]

# %%
# 오름차순
score.sort()
print(score) # [56, 67, 70, 90, 99, 100]

# %%
# 내림차순 :
#  먼저 sort()로 정렬후 reverse()

score.sort()
score.reverse()
print(score) # [100, 99, 90, 70, 67, 56]
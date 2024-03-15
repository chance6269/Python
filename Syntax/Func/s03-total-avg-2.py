# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:31:05 2024

@author: jcp
"""

# 함수

# %%

# 총점
def totavg(k, e, m):
    tot = k + e + m
    avg = tot / 3
    return tot, avg

# %%

tot, avg = totavg(70, 80, 90)

print("총점 : ", tot)
print("평균 : ", avg)

# %%

# 다중 리턴을 튜플로 받음
score = totavg(70, 80, 90)
print("점수:", score)
print("총점:", score[0])
print("평균:", score[1])
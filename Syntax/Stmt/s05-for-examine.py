# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:51:35 2024

@author: jcp
"""

# [문제]
# 구구단 프로그램을 작성하라

start = int(input("시작단을 입력하시오: "))
end = int(input("종료단을 입력하시오: "))


for n in range(start, end+1):
    print(f"[{n}단]")
    for i in range(1, 10):
        print(f"{n} X {i} = {n*i:>2}")
        
    print()
    
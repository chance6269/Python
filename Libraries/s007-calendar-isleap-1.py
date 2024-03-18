# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:26:54 2024

@author: jcp
"""

# 윤년 구하기
# 윤년의 기준 : 2월 달이 29일
# 1. 서력 기원 연수가 4로 나누어 떨어지는 해는 우선 윤년
# 2. 그중에 100으로 나누어 떨어지는 해는 평년이다.
# 3. 400으로 나누어 떨어지는 해는 다시 윤년으로 정한다.

# 2024년은 윤년

import calendar

year = 2024

# 윤년이면 True, 평년이면 False
isleap = calendar.isleap(year)
print(f"{year}년은 {isleap}이다")
print("{0}년은 {1}이다.".format(year, "윤년" if isleap else "평년"))

# %%

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

isleap2 = is_leap_year(year)
print(f"{year}년은 {isleap2}이다")
print("{0}년은 {1}이다.".format(year, "윤년" if isleap2 else "평년"))

# %%
def is_leap_year3(year):
    if year % 4 ==0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    else:
        return False
    
isleap3 = is_leap_year3(year)
print(f"{year}년은 {isleap3}이다")
print("{0}년은 {1}이다.".format(year, "윤년" if isleap2 else "평년"))
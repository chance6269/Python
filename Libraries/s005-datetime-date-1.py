# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:27:07 2024

@author: jcp
"""

# 날짜를 계산하고 요일을 알려면?
# datetime.date :
    # 년, 월, 일로 날짜를 표현할 때 사용하는 모듈
    
# 2019년 12월 14일부터 만나기 시작했다면 2021년 6월 5일 사귄 지 며칠째 되는 날일까?
# 아울러 사귀기 시작한 2019년 12월 14일은 무슨 요일이었을까? 파이썬 프로그램으로 풀어보자.

import datetime
day1 = datetime.date(2019, 12, 14)
day1
day2 = datetime.date(2021, 6, 5)
day2


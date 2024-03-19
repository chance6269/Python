# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:12:27 2024

@author: jcp
"""

# 두 날짜의 차이를 알려면?
# datetime.timedelta
# 두 날짜의 차이를 계산할 때
# timedelta 객체에는 산술 연산자 +와 -를 사용할 수 있다.

import datetime
today = datetime.date.today() # 오늘 날짜 
today

diff_days = datetime.timedelta(days=100)
diff_days # datetime.timedelta(days=100)

today + diff_days # datetime.date(2024, 6, 27)

today - diff_days # datetime.date(2023, 12, 10)
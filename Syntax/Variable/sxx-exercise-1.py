# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:07:25 2024

@author: jcp
"""

# [문제1]
# 지갑에 아래와 같은 돈을 가지고 있다.
# 총금액은 얼마인가?
# 각각의 금액을 변수에 담아서 연산을 수행하라.
# 10000원 4장
# 1000원 3장
# 500원 5개
# 100원 9개
# 10원 6개

won10 = 10
won100 = 100
won500 = 500
won1000 = 1000
won10000 = 10000

total = won10 * 6 + won100 * 9 + won500 * 5 + won1000 * 3 + won10000 * 4
print('총액: ',total)

# [문제2]
# 위 1번 문제의 총금액에서 15000원짜리 2개를 지출하고 남은 금액은 얼마인가?

total -= 15000 * 2
print('남은 금액: ', total)

# [문제3]
# 한달 급여가 400만원이다
# 분기별 보너스는 월급여의 30%가 지급된다.
# 세금은 월 급여의 3%이다.
# 보너스에 대한 세금은 없다.
# 월 세후 수령액은 얼마인가?
# 연 총세금은 얼마인가?
# 세후 연수령액은 얼마인가?

pay_month = 4000000
quater_bonus = pay_month * 3 / 10
tax = pay_month * 3 / 100
pay_mon_tax = pay_month - tax
year_tax = tax * 12
pay_year_tax = pay_mon_tax * 12 + quater_bonus * 4
print("월 세후 수령액 : ",pay_mon_tax)
print("연 총 세금 : ",year_tax)
print("세후 연수령액 : ",pay_year_tax)
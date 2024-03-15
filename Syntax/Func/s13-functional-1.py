# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:14:28 2024

@author: jcp
"""

# 함수형 프로그래밍(Functional Programming)

# 자료 처리를 수학적 함수의 계산으로 취급하고
# 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임 중 하나

# %%

# 글로벌 변수
# 경고창이 호출된 횟수 카운트
gcount = 0

# %%
# 경고창을 출력하는 함수
def makeAlert(name):
    def alert(message):
        global gcount
        gcount += 1
        print(f"[{name}] gcount({gcount}): {message}")
        
    return alert

# %%
infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("눈길에 주의 하세요. 조심하세요.'")
infoAlert("빗길에 조심하세요.'")

warnAlert("공사중, 도로끝")
warnAlert("홍수로 도로소실!!")
# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍에 활용

# 정의와 선언이 동시에 이루어짐
# 정의선언: 함수변수 = lambda 파라미터 : 표헌식
# 함수호출 : 함수변수(파라미터)
# 결과 리턴: 표현식의 처리 결과를 리턴

# %%

# 람다함수 : 정의와 함께 호출하는 방법
# (lambda parameter : expression)(parameter)
x = 10
y = 3
print(f"값 {x} * {y} ->", (lambda a, b : a * b)(x, y))
print(f"값 {x} ** {y} ->", (lambda a, b : a ** b)(x, y))


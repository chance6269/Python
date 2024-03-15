# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍에 활용

# 정의와 선언이 동시에 이루어짐
# 정의선언: 함수변수 = lambda 파라미터 : 표헌식
# 함수호출 : 함수변수(파라미터)
# 결과 리턴: 표현식의 처리 결과를 리턴

# %%

# 일반함수 : 정의
# 두 인자를 비교해서 큰 값을 리턴
def max(a,b):
    return a if a > b else b

# %%

# 함수 이름에 None을 할당하면 더이상 함수를 호출할 수 없다.
max = None

max(10, 20) # TypeError: 'NoneType' object is not callable

# %%

# 람다함수 : 정의
# 파라미터: a, b
# 리턴 : 인라인 처리 결과
lambda_max = lambda a, b : a if a > b else b

# %%
# 람다함수 : 호출
x = 99
y = 98
z = lambda_max(x, y)
print(z)
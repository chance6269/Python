# -*- coding: utf-8 -*-

# 예외처리(Exception)
# try ~ except

# 예외가 발생하는 경우
#  - 잘못된 동작을 했을 때
#  - 실행할 때 발생
#  - 프로그램이 종료

# 예외처리:
    # - 비정상적 상황으로 인해서 프로그램이 중단없이 실행 가능하도록 처리
    
# %%

# 0으로 나누었을 경우
x = 10
y = 0
z = x / y #ZeroDivisionError: division by zero
print(z)

# %%

import sys

x = 10
y = 0

if y == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(0)
    
z = x / y

print(z)

# %%
x = 10
y = 0
z = 0

try:
    z = x / y
except ZeroDivisionError as e:
    print("[예외발생]", e)
    
print('작업완료')
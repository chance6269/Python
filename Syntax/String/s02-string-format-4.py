# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:28:30 2024

@author: jcp
"""

# 정렬
# > : 오른쪽
# < : 왼쪽
# ^ : 가운데

n = 12345
s = 'hello'
f = 0.12345

print("#정수")
print(f"정수 : ({n:>10})")
print(f"정수 : ({n:<10})")
print(f"정수 : ({n:>10d})")
print(f"정수 : ({n:^10})")

# %%

print("#실수")
print(f'                 1         2')
print(f"        12345678901234567890")
print(f"실수 : ({f:>10})")
print(f"실수 : ({f:<10})")
print(f"실수 : ({f:^10})")
print(f"실수 : ({f:<10.3})") # 전체 10자리(소수점 포함), 소숫점 이하 3자리
print(f"실수 : ({f:>10.3})") # 전체 10자리(소수점 포함), 소숫점 이하 3자리
print(f"실수 : ({f:^10.3})") # 전체 10자리(소수점 포함), 소숫점 이하 3자리

# %%

# 가변처리(동적처리)
name = '홍길동'
age = 34

msg = '고객님의 이름은 {0}이며 나이는 {1}입니다.'.format(name, age)
print(msg)

fmt = "고객님의 이름은 {0}이며 나이는 {1}입니다."
print(fmt.format(name, age))
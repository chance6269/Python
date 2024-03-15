# -*- coding: utf-8 -*-

# 
a = [1,2,3]
b = [4,5,6]
c = a+b

d = c + [[7,8,9]]

# %%
# 인덱싱할 경우, 원본의 값도 변경이 된다.
print(d) # [1, 2, 3, 4, 5, 6, [7, 8, 9]]
seven = d[-1]
print(seven)
seven[0] *= 10
seven[1] *= 10
seven[2] *= 10
print(d) # [1, 2, 3, 4, 5, 6, [70, 80, 90]]

# %%
# 원본값 변화 없이 사용하려면 슬라이싱

six = c[:]
print(six)
six[1] *= 10
print(six)
print(c)

# seven = d[-1][:]
# print(seven)
# seven[1] *= 10
# print(seven)
# print(d)

# %%
# 원본값 변화 없이 사용하고 싶다면 리스트 연산을 사용.
seven2 = []
seven2 += d[-1] 

seven2[0] /= 10
seven2[1] /= 10

print(d) # [1, 2, 3, 4, 5, 6, [70, 80, 90]]

# %%
# 슬라이싱
# 원본의 값이 변경되지 않는다.
print(d) # [1, 2, 3, 4, 5, 6, [7, 8, 9]]
seven = d[0:2]
print(seven)
seven[0] *= 10
print(seven)
# seven[1] *= 10
# seven[2] *= 10

print(d)
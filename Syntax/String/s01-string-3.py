# -*- coding: utf-8 -*-

# 문자열 인덱싱
# 문자열은 연속된 문자들의 집합
# 참조 : 특정한 위치의 문자를 읽음
# 시작위치 : 0
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0 ~ n-1
# 제약사항 : 참조는 할 수 있지만 바꿀 수 없다.(read_only)

# 문자열 길이 함수: len()

# %%
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sl = len(s) # 문자열 길이 리턴
print(sl, ':', s)
s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# %%

# 참조 : 0부터 25(26-1)
print("첫번째 문자: ", s[0])
print("마지막 문자: ", s[sl-1])

print(s[0], s[1], '...', s[24], s[25])
print(s[0], s[1], '...', s[sl-2], s[sl-1])

print(id(s))
print(id(s1))
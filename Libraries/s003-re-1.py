# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:12:20 2024

@author: jcp
"""

# 정규표현식으로 개인정보를 보호하려면?
# re

# 평범한 해결방법
# 1. 공백 문자를 기준으로 전체 텍스트를 나눈다(split()함수 사용)
# 2. 나눈 단어가 주민 등록 번호 형식인지 조사한다.
# 3. 주민 등록 번호 형식이라면 뒷자리를 *******로 마스킹한다.
# 4. 나눈 단어를 다시 조립한다.

data = """
홍길동의 주민 등록 번호는 800905-1049118 입니다.
그리고 고길동의 주민 등록 번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(' '):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*"*7
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# %%
import re

data = """
홍길동의 주민 등록 번호는 800905-1049118 입니다.
그리고 고길동의 주민 등록 번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:11:21 2024

@author: jcp
"""

student = {
    'name': '홍길동',
    'age':34,
    '주소':'한양',
    '생존':False
    }


# %%
# 딕셔너리 함수를 이용한 객체 모두 요소 지우기
student.clear()
print(student) # {}
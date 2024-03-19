# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:27:59 2024

@author: jcp
"""

class Factorial:
    def __init__(self, n:int):
        self.__n = n

    # 내부 메서드: 비공개
    def __factorial(self, x: int) -> int:
        if x <= 1:
            return 1
        
        return x * self.__factorial(x - 1)
    
    # 공개 메서드
    def compute(self):
        return self.__factorial(self.__n)
    

n = 5
factobj = Factorial(n)
result = factobj.compute()

# print(f'{n},{factobj.__n}의 팩토리얼은 {result}입니다.')
# AttributeError: 'Factorial' object has no attribute '__n'

print(f'{n}의 팩토리얼은 {result}입니다.')
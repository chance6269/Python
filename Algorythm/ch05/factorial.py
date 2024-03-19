# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:27:59 2024

@author: jcp
"""

def factorial(n: int) -> int:
    
    print("[factorial] n:{}".format(n))
    
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
    

if __name__ == '__main__':
        n = int(input('출력하라 팩토리얼 값을 입력하세요.: '))
        print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
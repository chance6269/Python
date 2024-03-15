# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:09:41 2024

@author: jcp
"""

# [전자] 전자계산기
# 1. 다중 상속을 이용하라.
# 2. 사칙연산을수행하는 클래스를 각각 정의
#  - 덧셈 클래스
#  - 뺄셈 클래스
#  - 곱셉 클래스
#  - 나눗셈 클래스
# 3. 최하위 클래스에서 다중상속을 하여 통합.
#  - 총점, 평균 처리
# %%

# 덧셈
class Add:
    def plus(self, a, b):
        return a + b
    
# 뺄셈
class Sub:
    def minus(self, a, b):
        return a - b
    
# 곱셈
class Multi:
    def mul(self, a, b):
        return a * b

# 나눗셈
class Divde:
    def div(self, a, b):
        return a / b
    
    def mod(self, a, b):
        return a % b
    
# 계산기
class Calc(Add, Sub, Multi, Divde):
    
    def __init__(self):
        self.hist = []
        self.tot = 0
    
    def record(self, *cal):
        self.hist.append(cal)
        
    def plus(self, a, b):
        calc = (a, '+', b)
        self.record(self, calc)
        result = Add.plus(self, a, b)
        self.tot += result
        return result
        
    def minus(self, a, b):
        calc = (a, '-', b)
        self.record(self, calc)
        result = Sub.minus(self, a, b)
        self.tot += result
        return result
    
    def mul(self, a, b):
        calc = (a, '*', b)
        self.record(self, calc)
        result = Multi.mul(self, a, b)
        self.tot += result
        return result
        
    
    def div(self, a, b):
        calc = (a, '/', b)
        self.record(self, calc)
        result = Divde.div(self, a, b)
        self.tot += result
        return result
    
    def mod(self, a, b):
        calc = (a, '%', b)
        self.record(self, calc)
        result = Divde.mod(self, a, b)
        self.tot += result
        return result


def cal_avg(calc):
    return calc.tot / len(calc.hist)
    
def show_avg(calc):
    print("평균 : ",cal_avg(calc))
        
def show_tot(calc):
    print("총합 : ",calc.tot)
        
def show_hist(calc):
    for cal in calc.hist:
        print(cal)
        

# %%
calc1 = Calc()
print(calc1.plus(10, 20))
print(calc1.minus(20, 5))
show_avg(calc1)
show_tot(calc1)
show_hist(calc1)

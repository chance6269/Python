# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:51:59 2024

@author: Solero
"""

# 클래스(class) : 상속(inheritance)

# 정의
"""
class 자식클래스(부모클래스):
"""


#%%
class Student:
    def __init__(self, sid='이름없음', kor=0, eng=0, math=0): # 생성자(constructor)
        print(f"[생성자] {self}")
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor)
        print(f"[소멸자] {self}")
        
    def name(self, val):
        self.sid = val
    
    def korean(self, val):
        self.kor = val
        
    def english(self, val):
        self.eng = val
        
    def maths(self, val):
        self.math = val
        
    def score(self):
        return self.sid, self.kor, self.eng, self.math
    
    def total(self):
        return self.kor + self.eng + self.math
    
    def avg(self):
        return self.total() // 3 
        
#%%        

class School(Student):
    pass

#%%

# 학교 클래스
sc = School()
print(sc.score())

#%%
sc = School('전교생')
print(sc.score())
#%%
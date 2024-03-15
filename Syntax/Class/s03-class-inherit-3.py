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
        print(f"[Student] 생성자: {self}")
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
# 자식이 자신의 생성자를 정의하면 더이상 
# 부모의 생성자가 자동으로 호출되지 않는다.
class School(Student):
    def __init__(self):
        print(f"[School] 생성자: {self}")

#%%

# 학교 클래스
sc = School()
print(sc.score()) # AttributeError: 'School' object has no attribute 'sid'
# [이유]
# 자식이 생성자를 정의하여 더 이상 부모의 생성자가 자동으로 호출되지 않아
# 자식 생성자에 정의 되어 있는 속성들이 만들어지지 않는다.
# 그래서 아래와 같은 오류가 발생 한다.
# AttributeError: 'School' object has no attribute 'sid'
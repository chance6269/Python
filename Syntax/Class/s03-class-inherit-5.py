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
    def __init__(self, name, kor, eng, math):
        print(f"[School] 생성자: {self}")
        super().__init__(name, kor, eng, math) # 부모 생성자 호출
        
    def score(self): # 메서드 오버라이드
        return self.sid, self.kor, self.eng, self.math, self.total(), self.avg()

#%%

# 학교 클래스
sc = School('고길동', 60, 50, 40)

# %%

print(sc.score()) # ('고길동', 60, 50, 40, 150, 50)
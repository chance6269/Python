# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:16:53 2024

@author: jcp
"""

# 다중상속
# 상속을 받는 것은 속성, 메소드를 상속



# %%
class A:
    def __init__(self, val):
        self.cnt = val
        
    def count(self, val):
        self.cnt += val
        print("[A] self :", self)
        print("[A] count=", self.cnt)
        
    def printval(self, val):
        self.cnt += 1
        print(f"[A] cnt={self.cnt}, val={val}")
        
# %%

class B:
    def __init__(self, val):
        self.cnt = val
    
    def count(self):
        self.cnt += 1
        print("[B] count=", self.cnt)
        
    def printval(self, val):
        self.cnt += 1
        print(f"[B] cnt={self.cnt}, val={val}")    
# %%
# 다중상속:
# 명시적으로 부모를 지정
class C(B,A):
    def count(self,val):
        print("[C] self :", self)
        print("[C] count=", self.cnt)
        A.count(self,val)
        return self.cnt # 부모 B


# %%
# self : A, B, C의 인스턴스가 하나이다. 즉 C의 인스턴스 이다.
c = C(1)
cnt = c.count(7)
c.printval(10) # [B] cnt=9, val=10
print(cnt) # 8

# %%
# B의 메서드를 호출할 수 있는가?
# 즉 메서드 오버로딩을 지원하지 않는다.
# C에서 count()를 재정의 했기 때문에
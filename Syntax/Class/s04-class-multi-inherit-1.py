# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:16:53 2024

@author: jcp
"""

# 다중상속
# 상속을 받는 것은 속성, 메소드를 상속



# %%
class A:
    def printval(self, val):
        print("[A] val=", val)
        
# %%

class B:
    def printval(self, val):
        print("[B] val=", val)
        
# %%
# 다중상속:
    # 상속된 부모 클래스에서 동일한 메소드가 있으면?
    #  -> 먼저 상속된 클래스의 메소드가 사용된다.
class C(B,A):
    pass

class D(A,B):
    pass

# %%
c = C()
c.printval(10) # [B] val= 10

d = D()
d.printval(19) # [A] val= 19
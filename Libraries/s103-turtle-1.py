# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:53:25 2024

@author: jcp
"""

# Turtle

import turtle

t = turtle.Pen()

for x in range(100):
    t.forward(x) # 전진~99
    t.left(90) # 회전(왼쪽으로 90도)
    
turtle.done()

# %%

t = turtle.Pen()

for x in range(100):
    t.circle(100)
    t.left(5)
    
turtle.done()

# %%
import turtle as t
t.home()
t.shape("turtle")
t.forward(100)
t.left(120)
t.clear()
t.home()
t.shape('turtle')
for i in range(3):
    t.forward(100)
    t.left(120)
    
# %%
def draw_polygon(length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
        
# %%
import turtle as t

def draw_polygon(length, n):
    t.home()
    t.shape('turtle')
    t.color('red','yellow') # 빨간색, 노란색
    t.begin_fill() # 색을 채우기 시작
    for i in range(n):
        t.forward(length)
        t.left(360/n)
    t.end_fill() # 색 채우기 종료
    t.done() # 이벤트 루프
    
draw_polygon(100, 5)
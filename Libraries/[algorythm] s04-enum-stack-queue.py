# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:04:34 2024

@author: jcp
"""

from enum import Enum

Menu = Enum('Menu',['인큐','디큐','피크','검색','덤프','종료'])

print(Menu.인큐.name) # 인큐
print(Menu.인큐.value) # 1

print(Menu.덤프.name)
print(Menu.덤프.value) # 5

# %%

# 전체 멤버 확인
for menu in Menu:
    print("{}:{}".format(menu.name, menu.value))
    
"""
인큐:1
디큐:2
피크:3
검색:4
덤프:5
종료:6
"""

# %%
import random

# 리턴하는 자료형을 명시적으로 표현 : ->
def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    print(*s,sep='    ')
    n = random.randint(1, 6)
    return Menu(n)
    # while True:
    #     print(*s, sep='    ', end='')
def print_menu(menu: Menu):
    prnt("[print_menu] {} : {}".format(menu.name, menu.value))
    
    
# %%
    menu = select_menu()
print(menu)
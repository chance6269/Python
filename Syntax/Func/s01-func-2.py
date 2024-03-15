# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:47:35 2024

@author: jcp
"""

def hellocnt(msg, cnt):
    print(f"[hellox] msg({msg}), cnt({cnt})")
    for n in range(cnt):
        print(msg)
        
# %%
hellocnt("Hello, World", 10)
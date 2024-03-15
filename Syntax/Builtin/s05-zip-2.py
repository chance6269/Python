# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:14:32 2024

@author: jcp
"""

# zip()
# zip(*iterable)
# 여러개로 구성된 데이터를 인덱스별로 묶어서 리턴
# 최소 인덱스에 맞춰서

# %%

kw = ['월','화','수','목','금','토','일']
ew = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

weeks = tuple(zip(kw,ew))

print(weeks)
# (('월', 'Mon'), ('화', 'Tue'), 
# ('수', 'Wed'), ('목', 'Thu'), 
# ('금', 'Fri'), ('토', 'Sat'), ('일', 'Sun'))

# %%

for week in weeks:
    print(week)
"""
('월', 'Mon')
('화', 'Tue')
('수', 'Wed')
('목', 'Thu')
('금', 'Fri')
('토', 'Sat')
('일', 'Sun')
"""

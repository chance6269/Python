# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:35:49 2024

@author: jcp
"""

# None

lst = ['삼성','SK','LG']

# lst가 가리키고 있는 주소를 복사
# 데이터 복사가 아님
bst = lst

lst = lst.append(['APPLE', 'HD']) # append() 함수의 리턴값이 None이기 때문에

# lst : None
# 데이터를 더 이상 사용할 수 없다

print(lst) # None
print(bst) # ['삼성', 'SK', 'LG', ['APPLE', 'HD']]
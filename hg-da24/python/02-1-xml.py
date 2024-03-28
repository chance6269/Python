# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:22:35 2024

@author: jcp
"""

# ## 파이썬에서 XML 다루기

# In[12]:

    # XML : eXtensible Markup Language
    # 컴퓨터와 사람 모두 읽고 쓰기 편한 문서 포맷
    # 엘리먼트들이 계층 구조를 이루면서 정보를 표현
    # 이해하기 쉽지만 낭비가 심하다.


    # 부모 엘리먼트, 부모 노드 : book
    # 자식 엘리먼트 : name, author, year
x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""


# In[13]:

# XML 문자열을 파이썬 객체로 변환하기
# fromstring()

import xml.etree.ElementTree as et

book = et.fromstring(x_str)


# In[14]:


print(type(book)) # <class 'xml.etree.ElementTree.Element'>


# In[15]:


print(book.tag) # book


# In[16]:

# 

book_childs = list(book)

print(book_childs) 
# [<Element 'name' at 0x000001CE981E9530>, <Element 'author' at 0x000001CE981E9580>, <Element 'year' at 0x000001CE981E93F0>]


# In[17]:

    
# etree.ElementTree.Element
name, author, year = book_childs # 각 자식 엘리먼트들을 순서에 맞게 언패킹

# Element.text
print(name.text) # 혼자 공부하는 데이터 분석
print(author.text) # 박해선
print(year.text) # 2022

# 잘 출력되지만, XML은 자식 엘리먼트 순서가 항상 일정하지 않다.


# In[18]:

# findtext() : 자식 엘리멘트 찾기
# 해당하는 자식 엘리먼트를 탐색하여 자동으로 텍스트를 반환
# 순서가 어떻게 되있든 상관없기 때문에 안전하다.

name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')
# 존재하지 않는 자식
age = book.findtext('age')

print(name) # 혼자 공부하는 데이터 분석
print(author) # 박해선
print(year) # 2022
print(age) # None


# In[19]:

# JSON과 달리 XML은 배열 같은 구조가 없음
# 대신 두 개의 <book> 엘리먼트를 감싸는 부모 엘리먼트<books>를 생성

x2_str = """
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼자 공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""


# In[20]:


books = et.fromstring(x2_str)

print(books.tag) # books


# In[21]:

# 동일한 이름을 가진 여러 개의 자식 엘리먼트 찾기.
# findall()과 for

for book in books.findall('book'):
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')
    
    print(name)
    print(author)
    print(year)
    print()
# JSON VS XML
# JSON : API에서 전달한 텍스트를 json.loads()로 파이썬 객체로 바꾸어 내용 추출
# XML : fromstring() 함수로 부모 엘리먼트를 얻고, findall()로 자식 엘리먼트에 담긴 텍스트 추출

# In[22]:

# 판다스에서 XML 형식 처리    

import pandas as pd
pd_xml = pd.read_xml(x2_str)

print(pd_xml)

# %%
# x2_str을 리스트[딕셔너리, 딕셔너리] 객체로 변환하여 데이터프레임으로 바꾼다면?

x2 = []
for book in books.findall('book'):
    book_dict = {}
    book_dict['name'] = book.findtext('name')
    book_dict['author'] = book.findtext('author')
    book_dict['year'] = book.findtext('year')
    
    x2.append(book_dict)
    
print(x2)

pd_x2 = pd.DataFrame(x2)


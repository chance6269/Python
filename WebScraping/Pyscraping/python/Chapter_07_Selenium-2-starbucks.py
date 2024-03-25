# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:21:27 2024

@author: jcp
"""

# ## 7.3 동적 웹 페이지에서 데이터 가져오기

# ### 7.3.1 커피 전문점 음료 메뉴 가져오기

# [7장: 306페이지]

# <dd>메뉴 이름</dd>가 보이지만 이를 이용하면 원하는 결과를 가져올 수 없음.
# 상위에 있는 태그와 속성을 이용해 soup.select('태그_속성')에 활용


# In[ ]:


import requests  
from bs4 import BeautifulSoup 

url = "https://www.starbucks.co.kr/menu/drink_list.do"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

# 요소 검사를 수행한 결과의 상위 태그와 속성을 이용
products = soup.select('li.menuDataSet dl dd') 
products # []
# 메뉴 이름을 가져오지 못함.


# [7장: 307페이지]

# In[ ]:

# 조금 더 상위에 있는 태그와 속성 이용
products = soup.select('div.product_list dl dd')
products[0:3]
""" 
[<dd>
 <ul class="product_cold_brew">
 </ul>
 </dd>,
 <dd>
 <ul class="product_brewed">
 </ul>
 </dd>,
 <dd>
 <ul class="product_espresso">
 </ul>
 </dd>]
"""
# 태그 안 메뉴 이름과 관련된 내용이 없음.
# 자바스크립트가 포함된 웹사이트는 requests 라이브러리로는 모든 내용을 가져올 수 없다.

# 셀레니움을 이용해 HTML 소스를 모두 가져온 후 CSS 선택자를 이용해 원하는 내용을 가져와야함.
# 1. 드라이버 객체에 대해 driver.get(url)를 수행한 후 driver.page_source를 수행 :
    # 웹 브라우저가 자바스크립트를 해석한 HTML 코드를 가져옴.
# 2. Beautiful Soup를 이용해 가져온 HTML 코드를 파싱해 원하는 데이터를 찾고 추출.

# [7장: 308페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome() # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do" # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source          # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드를 파싱함

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# In[ ]:


drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
drink_products[0] # 첫 번째 음료 메뉴의 요소 출력


# [7장: 309페이지]

# In[ ]:


print(drink_products[0].prettify())


# In[ ]:
# 메뉴 이름 추출

drink_menu_name = drink_products[0].select_one('dd').get_text()
drink_menu_name


# [7장: 310페이지]

# In[ ]:
# 메뉴 사진 링크 추출

drink_menu_photo_link = drink_products[0].select_one('a img')['src']
drink_menu_photo_link


# In[ ]:
# 메뉴 전체에 대한 이름과 사진 링크를 추출해 리스트로 할당

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
import pandas as pd

options = Options()
options.headless = True # 헤드리스 모드로 지정해 크롬을 GUI 없이 수행

driver = Chrome(options=options) # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do"  # URL 지정
driver.get(url)              # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)    # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source    # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드 파싱

drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
driver.quit() # 웹 브라우저를 종료함

drink_menu_name_photo_links = [] 
for drink_product in drink_products:
    menu_name = drink_product.select_one('dd').get_text()
    menu_photo_link = drink_product.select_one('a img')['src']
    drink_menu_name_photo_links.append((menu_name, menu_photo_link))

drink_menu_name_photo_links[0:4]

# %%
print(type(drink_products)) # <class 'bs4.element.ResultSet'>
# %%
# [7장: 311페이지]

# In[ ]:


len(drink_menu_name_photo_links) # 스타벅스 음료 메뉴의 개수


# In[ ]:


col_drink_menu = ["메뉴", "사진"]
df = pd.DataFrame(drink_menu_name_photo_links, columns=col_drink_menu)
df.head(4)


# In[ ]:


# 이미지의 링크를 HTML img 태그로 만드는 함수 
def make_HTML_image_tag(link):
    image_width = 80   # 이미지 크기(너비)를 지정
    image_tag = f'<img src="{link}" width="{image_width}">' # img 태그
    return image_tag  # img 태그를 반환


# In[ ]:


make_HTML_image_tag(df["사진"][0])


# [7장: 313페이지]

# In[ ]:

# df.to_html() 
# DataFrame 데이터의 한 열에 있는 요소의 링크를 img 태그로 변환하기 위해
# formatters와 escape 옵션 이용.

html_table = df.head(4).to_html(formatters=dict(사진=make_HTML_image_tag), escape=False)
print(html_table)


# [7장: 314페이지]

# In[ ]:


from IPython.display import HTML

HTML(html_table) # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [7장: 315페이지]

# In[ ]:


folder = "C:/myPyScraping/data/ch07/"            # 폴더 지정
file_name = folder + "starbucks_drink_menu.html" # 생성할 HTML 파일 이름 지정 

df.to_html(file_name, formatters=dict(사진=make_HTML_image_tag), escape=False)

print("생성한 파일:", file_name)



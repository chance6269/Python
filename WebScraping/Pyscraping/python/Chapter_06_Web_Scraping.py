#!/usr/bin/env python
# coding: utf-8

# # 6장 웹 스크레이핑
#  : 웹 사이트 내 정보를 자동으로 추출하는 것

# ## 6.1 웹 스크레이핑을 위한 기본 지식

# ### 6.1.1 웹 스크레이핑의 과정
"""
- 주제 선정
- 웹사이트 분석 :
    데이터 추출이 가능 한지 판단
- 데이터 추출 :
    HTML 소스를 가져온 후 원하는 데이터 추출
- 데이터 처리 
- 데이터 활용
"""

# ### 6.1.2 웹 스크레이핑 시 주의 사항

# #### 주요 주의 사항
"""
- 웹 페이지 소스코드에서 데이터를 얻기 위한 규칙을 발견할 수 있어야 함.
- 웹 스크레이핑 수행 시 특정 웹 사이트에 너무 빈번하게 접근하지 말아야 함.:
    접근 주기를 짧게 설정하지 말 것.
- 코드를 지속해서 관리할 것 :
    웹 사이트는 예고없이 변경될 수 있음
- 저작권 침해 여부 확인
"""
# #### 웹 사이트 이용 규약
"""
 [robots.txt 항목]
 user-agent : 대상 웹 크롤링 봇의 이름. *이면 전체 대상
 Disallow : 접근을 허용하지 않는 경로. /이면 모든 경로 허용 안함
 Allow : 접근을 허용하는 경로. /이면 모든 경로 허용.
 Crawl-delay : 접근 주기 제한 시간
 Sitemap : 사이트맵 파일의 URL
"""
# ### 6.1.3 웹 데이터의 요청과 응답 과정
"""
 - GET : 요청에 필요한 내용(매개변수, 파라미터)을 본문에 담지 않고 
     URL 뒤에 ?로 연결해 보내기 때문에 바디 없음. ? 다음 문자열=쿼리 스트링
     * 쿼리 스트링 : 키=값 형태. 여러 개의 매개변수를 넘길 경우 &로 연결
 - POST : 
 - PUT
 - DELETE
 
"""

# ### 6.1.4 웹 페이지 언어(HTML) 구조
# - head, body 구조
# 
# [6장: 215페이지]

# In[ ]:


# get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\data\\ch06\\HTML_example.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p id="book_title">이해가 쏙쏙 되는 파이썬</p>\n  <p id="author">홍길동</p>\n  <p id="publisher">위키북스 출판사</p>\n  <p id="year">2018</p>\n </body>\n</html>\n')


# [6장: 216페이지]

# In[ ]:


# get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example2.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p>이해가 쏙쏙 되는 파이썬</p>\n  <p>홍길동</p>\n  <p>위키북스 출판사</p>\n  <p>2018</p>\n  </body>\n</html>\n')


# ### 6.1.5 웹 페이지의 소스 가져오기

# #### 웹 브라우저로 웹 페이지 소스 보기

# ####  requests 라이브러리 활용

# ####  GET 메서드로 웹 사이트의 소스 가져오기

# [6장: 220페이지]

# In[ ]:


import requests

r = requests.get("https://www.google.co.kr")
r # <Response [200]>
# HTML 소스를 위한 응답 객체를 반환.
# 접속이 잘 됐을 경우 응답 객체를 실행하면 <Response [200]> 출력

# In[ ]:


r.status_code


# [6장: 221페이지]

# In[ ]:


r.text[0:100]


# In[ ]:


r.headers


# In[ ]:


import requests

html = requests.get("https://www.google.co.kr").text
html[0:100]


# ### 6.1.6 웹 페이지의 소스 분석하고 처리하기

# #### 데이터 찾고 추출하기

# [6장: 222페이지]

# In[ ]:


from bs4 import BeautifulSoup

# 테스트용 html 소스
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        </span></div></body></html>""" 

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml') 
soup


# In[ ]:


print(soup.prettify())


# [6장: 224페이지]

# In[ ]:


soup.find('a')


# In[ ]:


soup.find('a').get_text()


# In[ ]:


soup.find('a')['href'] # soup.find('a').get('href') 도 동일


# [6장: 225페이지]

# In[ ]:


soup.find_all('a')


# In[ ]:


[x.get_text() for x in soup.find_all('a')]


# In[ ]:


from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
  </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")


# [6장: 226페이지]

# In[ ]:


soup2.title


# In[ ]:


soup2.body


# [6장: 227페이지]

# In[ ]:


soup2.body.h1


# In[ ]:


soup2.p


# In[ ]:


soup2.find_all('p')


# [6장: 228페이지]

# In[ ]:


soup2.find('p', {"id":"book_title"})


# In[ ]:


soup2.find('p', {"id":"author"})


# In[ ]:


soup2.find_all('p', {"id":"book_title"})


# In[ ]:


soup2.find_all('p', {"id":"author"})


# In[ ]:


from bs4 import BeautifulSoup

soup2 = BeautifulSoup(html2, "lxml")

book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())


# [6장: 230페이지]

# In[ ]:


soup2.select_one('body h1') # body 내의 h1 태그를 갖는 최초의 요소 찾기


# In[ ]:


soup2.select('body h1') # body 내의 h1 태그를 갖는 모든 요소 찾기 


# In[ ]:


soup2.select_one('body p')


# In[ ]:


soup2.select('body p')


# In[ ]:


soup2.select('p')


# [6장: 231페이지]

# In[ ]:


soup2.select('p#book_title')


# In[ ]:


soup2.select('p#author')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example_my_site.html', '<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <title>사이트 모음</title>\n  </head>\n  <body>\n    <p id="title"><b>자주 가는 사이트 모음</b></p>\n    <p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>\n    <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>\n    <a href="https://www.google.com" class="search" id="google">구글</a> <br>\n    <a href="http://www.daum.net" class="portal" id="daum">다음</a> <br>\n    <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a>\n  </body>\n</html>\n')


# [6장: 232페이지]

# In[ ]:


f = open('C:/myPyScraping/data/ch06/HTML_example_my_site.html', encoding='utf-8')

html3 = f.read()
f.close()

soup3 = BeautifulSoup(html3, "lxml")


# In[ ]:


soup3.select('a')


# [6장: 233페이지]

# In[ ]:


soup3.select('a.portal')


# In[ ]:


soup3.select_one('a').get_text()


# In[ ]:


[x.get_text() for x in soup3.select('a')]


# #### 웹 브라우저의 요소 검사

# [6장: 235페이지]

# In[ ]:


soup3.select('a')


# In[ ]:


soup3.select('a.portal')


# [6장: 236페이지]

# In[ ]:


soup3.select('a#naver')


# In[ ]:


soup3.select('a#naver.portal')


# In[ ]:


soup3.select('a.portal#naver')


# ### 6.1.7 웹 사이트 주소에 부가 정보 추가하기

# #### 웹 사이트 주소에 경로 추가하기

# [6장: 237페이지]

# In[ ]:


base_url = "https://api.github.com/"
sub_dir = "events"
url = base_url + sub_dir
print(url)


# In[ ]:


import requests

base_url = "https://api.github.com/"
sub_dirs = ["events", "user", "emails"]

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)


# #### 웹 사이트 주소에 매개변수 추가하기

# [6장: 238페이지]

# In[ ]:


import requests

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

base_url = "https://search.naver.com/search.naver"
parameter = "?where={0}&sm={1}&fbm={2}&ie={3}&query={4}".format(where_value, sm_value, fbm_value, ie_value, query_value)
url_para = base_url + parameter
r = requests.get(url_para)

print(r.url)


# [6장: 239페이지]

# In[ ]:


import requests  

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

url = "https://search.naver.com/search.naver"
parameters = {"where":where_value, "sm":sm_value, "fbm":fbm_value, "ie":ie_value, "query":query_value}
r = requests.get(url, params=parameters)
print(r.url)



#!/usr/bin/env python
# coding: utf-8

# # 7장 셀레니움을 이용한 웹 스크레이핑

# ## 7.1 셀레니움 소개 및 설치

# ## 7.2 셀레니움으로 웹 브라우저 제어

# ### 7.2.1 웹 사이트 접속

# [7장: 285페이지]

# In[ ]:


from selenium.webdriver import Chrome

driver = Chrome()                   # 크롬 드라이버 객체 생성

driver.set_window_size(800, 600)    # 웹 브라우저의 창 크기 설정
# driver.maximize_window()        

driver.get("https://www.google.com") # 웹 브라우저를 실행해 지정한 URL에 접속

print("- 접속한 웹 사이트의 제목:", driver.title)       # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 웹 사이트의 URL 출력


# ### 7.2.2 HTML 코드에서 요소 찾기

 # find_element(By.속성, '입력값') : 첫번째만
 # find_elements(By.속성, '입력값') : 모든 요소
"""
By 클래스 속성:
 ID
 NAME
 XPATH
 LINK_TEXT
 PARTIAL_LINK_TEXT
 TAG_NAME
 CLASS_NAME
 CSS_SELECTOR
"""

# ### 7.2.3 검색창에 문자열 입력하기

# [7장: 289페이지]
"""
 input_element = driver.find_element(By.속성, '입력값') # 1) By.속성의 입력값으로 입력창 찾기
 input_element.send_keys('문자열') # 2) 입력창에 문자열 입력
 input_element.submit() # 3) 문자열을 보낸 결과 요청
"""
# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 800) # 웹 브라우저의 창 크기 설정      

url = "https://www.google.com"   # URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

query = "python"
input_element = driver.find_element(By.NAME, "q") # 검색어를 입력할 수 있는 검색창 찾기
input_element.send_keys(query)                    # 검색창에 검색어 입력 
input_element.submit()                            # 검색 결과 요청

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력
print(type(input_element))

# [7장: 291페이지]

# In[ ]:


from selenium.webdriver import Chrome

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 800) # 웹 브라우저의 창 크기 설정      

url = "https://www.naver.com"    # URL 지정
driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

query = "파이썬"

# 검색어를 입력할 수 있는 검색창의 찾기
input_element = driver.find_element(By.NAME, "query")   
input_element.send_keys(query)   # 검색창에 검색어 입력 
input_element.submit()           # 검색 결과 요청

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 URL 출력


# ### 7.2.4 웹 사이트 로그인 자동화

# [7장: 295페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                  # 크롬 드라이버 객체 생성    
driver.set_window_size(800, 900)   # 웹 브라우저의 창 크기 설정

url = "https://accounts.kakao.com" # 카카오 계정 로그인 URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속

my_id = "kakao_id"                 # 자신의 아이디 입력
my_pw = "kakao_password"           # 자신의 패스워드 입력

# 아이디 입력
# user_id = driver.find_element(By.ID, "id_email_2")    # id 속성으로 아이디(ID) 입력창 찾기 
user_id = driver.find_element(By.NAME, "email")         # name 속성으로 아이디(ID) 입력창 찾기
user_id.send_keys(my_id)                                # 아이디 전송

# 패스워드 입력
# user_pw = driver.find_element(By.ID, "id_password_3") # id 속성으로 패스워드(비밀번호) 입력창 찾기 
user_pw = driver.find_element(By.NAME, "password")      # name 속성으로 패스워드(비밀번호) 입력창 찾기
user_pw.send_keys(my_pw)                                # 패스워드 전송
time.sleep(1)

# 로그인 버튼 클릭하기 
xpath = '//*[@id="login-form"]/fieldset/div[8]/button[1]' # XPath
login_button = driver.find_element(By.XPATH, xpath)       # XPath로 로그인 버튼 찾기
login_button.click()                                      # 버튼 클릭
    
print("- 접속한 웹 사이트의 제목:", driver.title)       # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 URL 출력


# [7장: 297페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 900) # 웹 브라우저의 창 크기 설정

url = "https://nid.naver.com/"   # 네이버 계정 로그인 URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

my_id = "naver_id"               # 자신의 아이디 입력
my_pw = "naver_password"         # 자신의 패스워드 입력

# 아이디 입력
script_id = f"document.getElementsByName('id')[0].value='{my_id}'"
driver.execute_script(script_id)  # 자바스크립트로 아이디 입력

# 패스워드 입력
script_pw = f"document.getElementsByName('pw')[0].value='{my_pw}'"
driver.execute_script(script_pw)  # 자바스크립트로 패스워드 입력

time.sleep(1)

# 로그인 버튼 클릭하기 
xpath = '//*[@id="log.login"]'                     # XPath
login_button = driver.find_element(By.XPATH, xpath)# XPath로 로그인 버튼 찾기
login_button.click()                               # 버튼 클릭
    
print("- 접속한 웹 사이트의 제목:", driver.title)  # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 URL 출력


# ### 7.2.5 웹 브라우저 스크롤

# [7장: 299페이지]
"""
execute_script()
window.scrollTo(x,y) # 절대위치
window.scrollBy(dx,dy) # 현재 위치 기준 상대위치

driver.execute_script("window.scrollTo(0,y)") # 절대 위치 y로 수직 스크롤
driver.execute_script("window.scrollBy(0,dy)") # 현재 위치에서 상대 위치 dy만큼 수직 스크롤

document.body.scrollHeight : 자바스크립트 코드
# 해당 웹사이트 문서의 높이 구하기
scroll_height = driver.execute_script("return document.body.scrollHeight") 

"""

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                  # 크롬 드라이버 객체 생성
driver.set_window_size(1000, 1000) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"     # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()              # 검색창 내용 모두 지우기
query = "python"
input_element.send_keys(query)     # 검색창에 검색어 입력
input_element.submit()             # 검색 결과 요청

# 웹 사이트 문서 높이 가져오기
scroll_height = driver.execute_script("return document.body.scrollHeight")
print("- 웹 사이트 문서 높이:", scroll_height)

y = 0         # Y축 좌표의 초깃값
y_step = 200  # Y축 아래로 이동하는 단계

while (True):
    y = y + y_step
    script =  "window.scrollTo(0,{0})".format(y)
    driver.execute_script(script)   # 스크립트 실행
    time.sleep(1)                   # 데이터를 받아올 때까지 기다림
    
    # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
    if (y >= scroll_height):
        break


# ### 7.2.6 웹 브라우저 내용을 이미지 파일로 저장

# [7장: 300페이지]

# driver.save_screeshot(img_file) : 
    # 웹브라우저 캡쳐해 저장하기
    # img_file = (file name 포함한)file path


# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"   # URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()                   # 검색창 내용 모두 지우기
query = "환율"
input_element.send_keys(query)         # 검색창에 검색어 입력
input_element.submit()                 # 검색 결과 요청

folder = "E:/Temp/" # 폴더 지정
image_file = folder + "환율정보.png"  # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)    # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

time.sleep(3) 
driver.quit()  # 웹 브라우저를 종료함

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력


# [7장: 301페이지]

# In[ ]:


driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정
driver.get(image_file)           # 웹 브라우저로 이미지 파일 열기


# ### 7.2.7 헤드리스(Headless) 웹 브라우저 이용하기

# [7장: 303페이지]
# 헤드리스 웹 브라우저 :
#   내부적으로 웹 브라우저를 실행
#   GUI 프로그램을 이용할 수 없는 리눅스 서버에서도 이용 가능

# Options() : 옵션 설정을 위한 객체
# options.add_argument('headless')
# driver.implicitly_wait(n) : 
    # 웹 사이트 내용을 다 받아오기까지 최대 n초 동안 기다리기.
    # 다 받아온 후에는 기다리지 않고 다음으로 넘어감.
    # 요소가 다 나타나기를 기다리는 것.
    # 만약 기다리지 않는다면? -> NoSuchElementError
    
# 

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()                  # 옵션 설정을 위한 객체 생성
options.add_argument('headless')     # 헤드리스 웹 브라우저로 옵션 설정
options.add_argument('window-size=1100,1000') # 웹 브라우저의 창 크기 설정

driver = Chrome(options=options)     # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://finance.naver.com/"   # URL 지정
driver.get(url)                      # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)            # 웹 사이트의 내용을 받아오기까지 기다림

folder = "D:/Temp/"   # 폴더 지정
image_file = folder + "네이버_금융.png" # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)      # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

driver.quit() # 웹 브라우저 종료

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력


# [7장: 304페이지]

# In[ ]:



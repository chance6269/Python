# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:26:48 2024

@author: jcp
"""

# ### 6.2.5 웹 페이지에서 이미지 가져오기

# [6장: 275페이지]

# In[ ]:


import requests  

image_url = 'https://www.python.org/static/img/python-logo.png' # 이미지 링크(주소)
r = requests.get(image_url) # 이미지 주소의 HTTP 응답 객체
r


# [6장: 276페이지]

# In[ ]:


file_name = image_url.split("/")[-1]
file_name


# In[ ]:


from pathlib import Path

download_folder = 'E:/Workspace/Python/WebScraping/Pyscraping/python/download' 
image_dir_path = Path(download_folder)

if not image_dir_path.exists():
    image_dir_path.mkdir(parents=True, exist_ok=True)
    
print("생성한 폴더:", download_folder)


# [6장: 277페이지]

# In[ ]:


image_path = image_dir_path/file_name
image_path


# [6장: 278페이지]

# In[ ]:


r = requests.get(image_url) # 이미지 주소의 HTTP 응답 객체
image_data = r.content # 응답 객체(r)을 이용해 받은 이미지 데이터

with open(image_path, 'wb') as f:
    f.write(image_data)


# In[ ]:


import requests 
from pathlib import Path

# Unsplash의 사진 이미지 주소
image_url = "https://images.unsplash.com/photo-1645956734658-8b6e62e7d35a"
  
file_name = image_url.split("/")[-1] + ".jpg" # 파일 이름 생성(확장자 추가)
download_folder = 'E:/Workspace/Python/WebScraping/Pyscraping/python/download' # 다운로드 폴더 지정

# 지정한 다운로드 폴더를 생성하지 않았으면 생성
image_dir_path = Path(download_folder)
if not image_dir_path.exists():
    image_dir_path.mkdir(parents=True, exist_ok=True)
    
image_path = image_dir_path/file_name # 전체 경로(폴더 + 파일명)

r = requests.get(image_url, stream=True)
if r.status_code == 200:  
    with open(image_path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    print("- 이미지를 다운로드했습니다")
else:
    print("- 지정한 이미지 링크의 응답이 없습니다.")


# ## 6.3 정리

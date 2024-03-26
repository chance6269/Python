#!/usr/bin/env python
# coding: utf-8

# # 8장 웹 API

# ## 8.1 웹 API의 이해

# 응용 프로그램 프로그래밍 인터페이스(API) : 
    # 응용 프로그램에서 사용할 수 있도록 OS나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
    # 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스 제공
    
# 웹 API :
    # 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

# ### 8.1.1 웹 API의 데이터 획득 과정

# 클라이언트 - 요청 : 데이터
# 서버 - 

# ### 8.1.2 웹 API의 인증 방식

# ### 8.1.3 응답 데이터의 형식 및 처리

# #### JSON 데이터 형식

# #### JSON 데이터 변환 및 데이터 추출

# [8장: 341페이지]

# In[ ]:


import json

python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}
type(python_dict)


# In[ ]:
    
    # JSON 데이터 변환 및 데이터 추출
    # json.dumps()


json_data = json.dumps(python_dict)
type(json_data)


# [8장: 342페이지]

# In[ ]:


print(json_data)


# In[ ]:


json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)


# In[ ]:


dict_data = json.loads(json_data) # JSON 데이터를 파이썬의 딕셔너리 타입으로 변환
type(dict_data)


# [8장: 343페이지]

# In[ ]:


dict_data['신체정보']['몸무게']


# In[ ]:


dict_data['취미']


# In[ ]:


dict_data['취미'][0]



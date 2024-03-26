# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:08:34 2024

@author: jcp
"""

# ## 8.2 API 키 없이 시간 관련 데이터 가져오기 

# ### 8.2.1 시간대 리스트와 현재 시각 데이터 가져오기

# [8장: 345페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"

r = requests.get(url)
r.text[:70] # 문자열 중 앞의 일부만 출력
# r.text    # 문자열 전체를 출력


# [8장: 346페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

r = requests.get(url)
print(r.text) 


# In[ ]:


url = "https://timeapi.io/api/Time/current/zone" # 요청 주소
parameters = {"timeZone": "Asia/Seoul"}          # 요청 매개 변수 생성

r = requests.get(url, params=parameters)
print(r.text) 


# In[ ]:


json_to_dict = json.loads(r.text)
type(json_to_dict)


# [8장: 347페이지]

# In[ ]:

# Response.json()을 이용해서 직접
# json -> dict
json_to_dict = r.json() #JSON 형태의 데이터를 파이썬의 딕셔너리 타입으로 변환
type(json_to_dict)


# In[ ]:


import requests
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

date_time_dict = requests.get(url).json()
type(date_time_dict)


# In[ ]:


date_time_dict


# [8장: 348페이지]

# In[ ]:


date_time_dict["dateTime"], date_time_dict["timeZone"], date_time_dict["dayOfWeek"]


# ### 8.2.2 시간대 변환 데이터 가져오기

# GET vs POST
# GET : 주소에다 실어서 보냄
# POST : 주소에 서비스를 요청

# [8장: 349페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "UTC" # GMT로 지정해도 결과는 동일

headers = {"Content-Type": "application/json"}

# dict -> json
# json_data = json.dumps({"fromTimeZone": from_time_zone,
#                         "dateTime": from_date_time,
#                         "toTimeZone": to_time_zone})

json_data = json.dumps({"fromTimeZone": from_time_zone,
                        "dateTime": from_date_time,
                        "toTimeZone": to_time_zone,
                        "dstAmbiguity": ""})

r = requests.post(url, headers=headers, data=json_data) # POST 방법으로 요청해 응답받음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# [8장: 350페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "GMT" # UTC로 지정해도 결과는 동일

dict_data = {"fromTimeZone": from_time_zone,
              "dateTime": from_date_time,
              "toTimeZone": to_time_zone,
              "dstAmbiguity": ""}

r = requests.post(url, json=dict_data) # POST 방법으로 요청해 응답받음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# [8장: 351페이지]

# In[ ]:


dateTime = ctz_json_to_dict['conversionResult']['dateTime'] # 변환된 날짜와 시각 데이터를 추출
to_date_time = f"{dateTime.split('T')[0]} {dateTime.split('T')[1]}"
from_date_time, to_date_time



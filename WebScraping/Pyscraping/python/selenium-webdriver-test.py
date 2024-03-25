# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:36:17 2024

@author: jcp
"""

# 셀레니움 웹드라이브 자동 설치 예제
# pip install selenium
# pip install webdriver_manager

# %%

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriver
# from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.naver.com")
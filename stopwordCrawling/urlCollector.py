from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import requests

'''
* 알고리즘
    1. homepageUrl 접속
    2. id='video-title-link'인 a tag 추출
    3. homepageUrl + link를 파일에 저장
'''

# id="video-title-link" -> href

SCROLL_PAUSE_TIME = 0.7

homepageUrl = "https://www.youtube.com"
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(homepageUrl)
actions = driver.find_element(By.CSS_SELECTOR, 'body')
time.sleep(1)

for i in range(11):
    actions.send_keys(Keys.END)
    time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
titleLink = soup.find_all('a', {'id': 'video-title-link'})
with open('urlLink.txt', 'wt') as f:
    for link in titleLink:
        f.write(homepageUrl+ '/' + str(link['href']))
        f.write('\n')
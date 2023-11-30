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
    1. 파일에서 url 하나씩 읽어옴
    2. 해당 url 접속
    3. 페이지 다운 반복
    4. 파싱
    5. 텍스트 추출
    6. 토크나이저(norm=True)
    7. BoW 생성
    8. index로 값 저장
'''

SCROLL_PAUSE_TIME = 0.8

urlLinks = open('urlLink.txt')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

time.sleep(SCROLL_PAUSE_TIME)
for i, link in enumerate(urlLinks):
    driver.get(link)
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    time.sleep(SCROLL_PAUSE_TIME)

    for j in range(10):
        actions.send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE_TIME)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    comment_list = soup.select("yt-formatted-string#content-text")
    comment_final = []

    if(len(comment_list) >= 50):
        for k in range(len(comment_list)):
            temp_comment = comment_list[k].text
            temp_comment = temp_comment.replace('\n', '')
            temp_comment = temp_comment.replace('\t', '')
            if temp_comment:
                comment_final.append(temp_comment)

        with open(f'comments/video{i}.txt', 'w') as commentRepository:
            for comment in comment_final:
                commentRepository.write(str(comment))
                commentRepository.write('\n')

urlLinks.close()
driver.close()
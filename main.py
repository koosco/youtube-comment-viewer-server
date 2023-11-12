from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

start = time.time()
url = "https://www.youtube.com/watch?v=F2pQEXieIqM"
SCROLL_PAUSE_TIME = 0.7

driver.get(url)
time.sleep(SCROLL_PAUSE_TIME)

actions = driver.find_element(By.CSS_SELECTOR, 'body')

for _ in range(10):
    actions.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)

# 내용 가져오기
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

id_list = soup.select("div#header-author > h3 > #author-text > span")
comment_list = soup.select("yt-formatted-string#content-text")

id_final = []
comment_final = []

for i in range(len(comment_list)):
    temp_comment = comment_list[i].text
    temp_comment = temp_comment.replace('\n', '')
    temp_comment = temp_comment.replace('\t', '')
    comment_final.append(temp_comment)

driver.close()
end = time.time()

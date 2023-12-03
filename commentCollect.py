from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from commentCollect import *
from resultProcessing import *
from typing import List
import threading
import time

SCROLL_PAUSE_TIME = 0.7

def getContet(url: str, iterationCount: int, fileName: str):
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(SCROLL_PAUSE_TIME)
    actions = driver.find_element(By.CSS_SELECTOR, 'body')

    for i in range(iterationCount):
        actions.send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE_TIME)

    comments = getComments(fileName, driver.page_source)
    driver.close()

    print("getContent with " + fileName + " end")
    return comments
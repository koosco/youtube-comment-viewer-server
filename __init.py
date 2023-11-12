from flask import Flask, jsonify, request
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_response():
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    url = request.form.get('url')
    print('received url is', url)

    print('check point: scraping start')
    driver.get(url)
    start = time.time()
    time.sleep(SCROLL_PAUSE_TIME)
    print('check point: before get page')
    actions = driver.find_element(By.CSS_SELECTOR, 'body')

    print('check point: before Keys.END')
    print('time:', time.time() - start)
    for i in range(1, 11):
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight, 'instant');")
        actions.send_keys(Keys.END)
        time.sleep(1)
        print('check point: scroll loop', i)

    print('check point: before get page source')
    print('time:', time.time() - start)
    time.sleep(3)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    comment_list = soup.select("yt-formatted-string#content-text")
    comment_final = []

    end = time.time()
    print('총 소요 시간:', end - start)
    print('check point: remove \\n, \\t')
    for i in range(len(comment_list)):
        temp_comment = comment_list[i].text
        temp_comment = temp_comment.replace('\n', '')
        temp_comment = temp_comment.replace('\t', '')
        comment_final.append(temp_comment)

    print('program still working')
    result = '\n'.join(comment_final)
    driver.close()
    

    data = {'text': result}
    with open('res.txt', 'w') as f:
        for comment in comment_final:
            f.write(comment)
            f.write('\n')
    return jsonify(data)

if __name__ == '__main__':
    SCROLL_PAUSE_TIME = 0.7
    display = Display(visible=0, size=(1024, 768))
    display.start()
    app.run('0.0.0.0', port=5000, debug=True)

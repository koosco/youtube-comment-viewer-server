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
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
  r"*": {"origin": "*"}
})

@app.route('/post', methods=['POST'])
def post_response():
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    start = time.time()
    # url = request.form.get('url')
    data = request.get_json()
    if data and 'url' in data:
        url = data['url']
    print(url)
    print(type(url))

    driver.get(url)
    start = time.time()
    time.sleep(SCROLL_PAUSE_TIME)
    actions = driver.find_element(By.CSS_SELECTOR, 'body')

    for i in range(1, 6):
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight, 'instant');")
        actions.send_keys(Keys.END)
        time.sleep(1)

    time.sleep(2)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    comment_list = soup.select("yt-formatted-string#content-text")
    comment_final = []

    end = time.time()
    for i in range(len(comment_list)):
        temp_comment = comment_list[i].text
        temp_comment = temp_comment.replace('\n', '')
        temp_comment = temp_comment.replace('\t', '')
        comment_final.append(temp_comment)

    result = ' '.join(comment_final)
    driver.close()
    
    end = time.time()
    print(end - start)
    data = {'text': result}
    with open('res.txt', 'w') as f:
        for comment in comment_final:
            f.write(comment)
            f.write('\n')
    return jsonify(data)

if __name__ == '__main__':
    SCROLL_PAUSE_TIME = 0.7
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    app.run('0.0.0.0', port=8081, debug=True)

from flask import Flask, jsonify, request
from commentCollect import *
from flask_cors import CORS
import time
import json
import threading

entireIteration = 10
initialIteration = 2

app = Flask(__name__)
cors = CORS(app, resources={
  r"*": {"origin": "*"}
})

@app.route('/post', methods=['POST'])
def post_response():
    data = request.get_json()
    if data and 'url' in data:
        entireCommentThread = threading.Thread(target=getContet, args=(data['url'], entireIteration, 'entireComments.txt'))
        entireCommentThread.start()

    initialComments = getContet(data['url'], initialIteration, 'initialComments.txt')

    data = {'text': initialComments}
    return jsonify(data)

if __name__ == '__main__':
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    app.run('0.0.0.0', port=8081, debug=True)

@app.route('/additionalContent', methods=['POST'])
def additional_response():
    pass
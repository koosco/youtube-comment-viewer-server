from glob import glob
from konlpy.tag import Okt
from collections import Counter
import re

def clean_str(text):
    text = re.sub(r'([1-9]|[0-5][0-9]):(0[1-9]|[0-5][0-9])', '', text)
    text = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', repl='', string=text)
    text = re.sub(r'(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', repl='', string=text)
    text = re.sub(r'([ㄱ-ㅎㅏ-ㅣ]+)', repl='', string=text)
    text = re.sub(r'[^\w\s\n]', repl='', string=text)
    text = re.sub(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', string=text)
    text = re.sub(r'\n', '.', string=text)

    return text 

paths = glob('comments/*.txt')
paths.sort(key=lambda x: [len(x), x])

# stop word list
del_list = []
with open('korean_stopwords.txt', 'rt') as stopwordFile:
    for line in stopwordFile.readlines():
        del_list.append(line[:-1])

words = set()

for path in paths:
    data = []
    with open(path, 'rt') as commentFile:
        lines = commentFile.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)

    data = ' '.join(data)
    tokenizer = Okt()
    raw_pos = tokenizer.pos(clean_str(data), norm=True, stem=True)

    word_cleaned = []
    for word in raw_pos:
        if word[1] == 'Noun':
            if (len(word[0]) > 1) & (word[0] not in del_list):
                word_cleaned.append(word[0])
            if word[0] not in words:
                words.add(word[0])

    word_cleaned = Counter(word_cleaned)

    with open('BoWs/' + path[9:-4] + '.txt', 'wt') as writeFile:
        for word, cnt in word_cleaned.items():
            writeFile.write(word)
            writeFile.write(' ')
            writeFile.write(str(cnt))
            writeFile.write('\n')

words = list(words)
with open('BoWs/wordList.txt', 'wt') as wordList:
    for word in words:
        wordList.write(word)
        wordList.write('\n')
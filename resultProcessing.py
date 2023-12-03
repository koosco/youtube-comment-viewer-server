from bs4 import BeautifulSoup
from typing import List
 
def parsingPage(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')

    commentList = soup.select("yt-formatted-string#content-text")
    commentFinal = []

    for i in range(len(commentList)):
        tempComment = commentList[i].text
        tempComment = tempComment.replace('\n', '')
        tempComment = tempComment.replace('\t', '')
        commentFinal.append(tempComment)
    
    return commentFinal

def saveContent(fileName: str, comments: List[str]):
    with open('result/' + fileName, 'wt') as file:
        for comment in comments:
            file.write(comment)
            file.write('\n')

def getComments(fileName: str, pageSource):
    comments = parsingPage(pageSource)
    saveContent(fileName, comments)

    return comments
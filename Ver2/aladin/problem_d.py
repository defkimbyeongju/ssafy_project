'''
import json


def best_book(books):
    best = 0
    best_book = None
    for i in books:
        try:
            if i["customerReviewRank"] > best:
                best = i['customerReviewRank']
                best_book = i['title']
        except:
            continue  
    return best_book




        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('aladin/data/books/*.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))
'''

import json
import glob

def read_json_files(path_pattern):
    json_files = glob.glob(path_pattern)
    data = []
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))
    return data

def best_book(books):
    best = 0
    best_book = None
    for book in books:
        if int(book["customerReviewRank"]) > best:
            best = int(book["customerReviewRank"])
            best_book = book['title']
    return best_book

if __name__ == '__main__':
    books_list = read_json_files('aladin/data/books/*.json')
    print(best_book(books_list))

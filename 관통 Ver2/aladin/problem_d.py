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
    books_json = open('관통 Ver2/aladin/data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))

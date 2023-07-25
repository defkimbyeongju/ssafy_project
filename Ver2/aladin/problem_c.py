import json
from pprint import pprint


def books_info(books, categories):
    books_list = []
    
    for k in books:
        cate_name = []
        for i in categories:
            if i['id'] in k['categoryId']:
                cate_name.append(i['name'])
        books_info = {'author' : k['author'],
                    'categoryName' : cate_name,
                    'cover' : k['cover'],
                    'description' : k['description'],
                    'id' : k['id'],
                    'priceSales' : k['priceSales'],
                    'title' : k['title'],
                        }
        books_list.append(books_info)
    return books_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('aladin/data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('aladin/data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
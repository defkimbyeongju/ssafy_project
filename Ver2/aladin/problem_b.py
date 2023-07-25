import json
from pprint import pprint


def book_info(book, categories):
    cate_name = []
    for i in categories:
        if i['id'] in book['categoryId']:
            cate_name.append(i['name'])
    book_dict = {'author' : book['author'],
                 'categoryName' : cate_name,
                 'cover' : book['cover'],
                 'description' : book['description'],
                 'id' : book['id'],
                 'priceSales' : book['priceSales'],
                 'title' : book['title'],
                  }
    return book_dict

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('aladin/data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('aladin/data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

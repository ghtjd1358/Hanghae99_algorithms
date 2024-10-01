# ====================== 테스트 8 =====================================

N = int(input())
books_list = {}

for _ in range(N):
    book = input()
    if book in books_list:
        books_list[book] += 1
    else :
        books_list[book] = 1
    
book_cnt = max(books_list.values())

books_cnt_key = []

for book, cnt in books_list.items():
    if cnt == book_cnt:
        books_cnt_key.append(book)

print(sorted(books_cnt_key)[0]) 
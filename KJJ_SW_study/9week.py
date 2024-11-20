# https://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authorKey=b321186f87c5e8a01327c6541203a4d490818c0ed5ecd9cbcfadfb56141f167b
import pandas as pd
import requests
url = "https://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authorKey=b321186f87c5e8a01327c6541203a4d490818c0ed5ecd9cbcfadfb56141f167b"

r = requests.get(url)

data = r.json()
print(data)

books = []
for d in data['response']['docs']:
    books.append(d['doc'])

books_df = pd.DataFrame(books)
print(books_df)

books_df.to_json('20s_bset_book.json')

x_str = """
<book>
    <name> 혼자공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""
import xml.etree.ElementTree as et
book = et.fromstring(x_str)

print(type(book))

print(book.tag)

book_childs = list(book)
print(book_childs)

name, author, year = book_childs
print(name.text)
print(author.text)
print(year.text)

name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')

print(name)
print(author)
print(year)

x2_str = """
<books>
    <book>
        <name> 혼자공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name> 혼자공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""

books = et.fromstring(x2_str)
print(book.tag)

for book in books.findall('book'):
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')
    print(name)
    print(author)
    print(year)
    print()
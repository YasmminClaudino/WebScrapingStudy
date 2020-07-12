from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://www.amazon.com.br/gp/bestsellers/books")
bs = BeautifulSoup(html.read(), 'html.parser')
count = 0;
for books in bs.find_all('div', {'class':'p13n-sc-truncate p13n-sc-line-clamp-1'}):
    count += 1
    print("#", count, " " + books.parent.get_text())
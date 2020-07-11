import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
print(result)
src = result.content
print(src)
soup = BeautifulSoup(src, 'lxml')

urls = [h2_tag.find('a').attrs['href'] for h2_tag in soup.find_all('h2')]

print('Oto linki na stronie \"www.whitehouse.gov/briefings-statements/\":')
for url in urls:
    print(url)

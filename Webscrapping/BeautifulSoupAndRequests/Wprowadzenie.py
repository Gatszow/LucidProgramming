import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

# code '200' - good
# else - bad (see on the wikipedia):
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# print(result.status_code)

# explanation what headers mean
# https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
# print(result.headers)

# page content of the website
src = result.content

# we have the page source stored, so we will use the
# BeautifulSoup module to parse and process the source.
# to do so, we create a BeautifulSoup object based on the
# source variable we created above:
soup = BeautifulSoup(src, "lxml")

# Now that the page source has been processed via Beautifulsoup
# we can access specific information directly from it. For instance,
# say we want to see a list of all of the links on the page:
links = soup.find_all("a")
print(links)
# print('\n')

# Perhaps we just want to extract the link that has contains the text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags.
for link in links:
    if "Wszystko" in link.text:
        print(link)
        print(link.attrs['href'])

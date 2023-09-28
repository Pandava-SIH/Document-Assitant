import requests
from bs4 import BeautifulSoup

url = "https://lawrato.com/legal-documents/banking-finance-legal-forms"
response = requests.get(url)

data = {}

# if response.status_code == :
soup = BeautifulSoup(response.text, 'html.parser')

for article in soup.find_all(class_='question-body'):
    title = article.text
    link = article.get('href')
    data[title] = link
    
    # link = article.find('a')['href']

# else :
#     print("Failed to retrieve the web page . Status Code : ", response.status_code)

for title, link in data.items():
    print(f"Title : {title}")
    print(f"Link : {link}")

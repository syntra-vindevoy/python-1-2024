from bs4 import BeautifulSoup
import requests

url = "https://www.dendermonde.be/"

bs4 = BeautifulSoup(requests.get(url).text, "lxml")

print(bs4.prettify())

hrefs=[r for r in bs4.find_all("a", href=True) if r.get("href").startswith("https")]
for href in hrefs:
    print(href.get("href"))

print("==========================")

imgs=[r for r in bs4.find_all("img")]
for img in imgs:
    if img.get("src").startswith("http"):
        url_img=img.get("src")
    else:
        url_img=url+img.get("src")
    print(url_img)
    res =requests.get(url_img)

    print(res.status_code)

url = "https://www.jobat.be/nl/jobs/ict"

bs4 = BeautifulSoup(requests.get(url).text, "lxml")

jobs=bs4.find_all("div", class_="jobResults-card open")
for job in jobs:
    print(job.find("h2").text)
    print(job.find("h2").find("a").get("href"))
    link="https://www.jobat.be/nl/jobs"+job.find("h2").find("a").get("href")
    bs4l = BeautifulSoup(requests.get(link).text, "lxml")
    print(bs4l.prettify())
    print("==========================")



from bs4 import BeautifulSoup
import requests

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("http://quotes.toscrape.com")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
if soup.status_code == 200:
    print("SUCCESS")
else:
    print("ERROR")

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE
#quotes = soup.findAll('span', attrs={'class':'text'})
quotes = soup.find_all('span', class_='text')
#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
#authors = soup.findAll('small', attrs={"class":"author"})
authors = soup.find_all('small', class_="author")
#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)


import pandas as pd

current_page = 1

data = []

proceed = True

while (proceed):
    print("Currently scraping page: " + str(current_page))

    url = "https://books.toscrape.com/catalogue/page-" + str(current_page) + ".html"

    proxies = ""

    # proxies={'http': 'http://customer-[your_username]:[your_password]_@pr.oxylabs.io:7777'}

    page = requests.get(url, proxies=proxies)

    soup = BeautifulSoup(page.text, "html.parser")

    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}

            item['Title'] = book.find("img").attrs["alt"]

            item['Link'] = "https://books.toscrape.com/catalogue/" + book.find("a").attrs["href"]

            item['Price'] = book.find("p", class_="price_color").text[2:]

            item['Stock'] = book.find("p", class_="instock availability").text.strip()

            data.append(item)

    current_page += 1

df = pd.DataFrame(data)
df.to_excel("books.xlsx")
df.to_csv("books.csv")
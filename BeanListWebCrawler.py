import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def parse_and_extract_titles_and_prices(html_content):
    titles = []
    prices = []
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract titles
    headers = soup.find_all('p', class_='grid-link__title')
    for header in headers:
        titles.append(header.text.strip())

    # Extract prices
    money_spans = soup.find_all('span', class_='money')
    for price in money_spans:
        prices.append(price.text.strip())

    return titles, prices

def main():
    url = "https://www.mrdodocoffee.com/collections/all"
    html_content = fetch_page_content(url)
    if html_content:
        titles, prices = parse_and_extract_titles_and_prices(html_content)
        print("Mr. Dodo Coffee Menu:")
        for title, price in zip(titles, prices):
            print("Title:", title)
            print("Price:", price)
            print()

    else:
        print("Failed to fetch the mrdodocoffee page content.")

if __name__ == "__main__":
    main()

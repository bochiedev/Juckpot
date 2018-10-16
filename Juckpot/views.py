from bs4 import BeautifulSoup
import requests
import json


def crawl_jumia(url):

    result = []
    keywords = []
    href_links = []
    url_dict = {}

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")

    # find urls page
    for a in soup.find_all('a', href=True):
        link = a.get('href')
        print(link)
        href_links.append(link)

    for page in href_links:
        req_2 = requests.get(page)
        soup_2 = BeautifulSoup(req_2.text, "lxml")

        for a in soup_2.find_all('a', href=True):
            link_2 = a.get('href')
            print(link_2 + str(23451))
            href_links.append(link_2)

    return href_links


url = 'https://www.jumia.co.ke'
crawl = crawl_jumia(url)
with open("../kompas.json", "w") as f:
    json.dump(crawl, f)

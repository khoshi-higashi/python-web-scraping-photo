import requests
import urllib.request
import urllib.error
import time
import pprint
import os
from bs4 import BeautifulSoup

html_doc = "./sample.html"
soup = BeautifulSoup(open(html_doc))


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))


dst_dir = ''
download_dir = ''

url_list = []

sleep_time_sec = 1


for link in soup.find_all('div', class_="separator"):
    # print(link.get('href'))
    url = link.contents[1].get('href')
    # print(link.contents[1].get('href'))
    # download_file_to_dir(url, dst_dir)
    url_list.append(url)

# print(url_list)

i = 0

for url in url_list:
    print(url)
    # download_file_to_dir(url, download_dir)

    # url = "ダウンロードしたい画像のURL"
    file_name = ""
    file_name += str(i)
    file_name += ".jpg"

    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as aaa:
        aaa.write(image)

    time.sleep(sleep_time_sec)
    i += 1

import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 250)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


URL = "https://images.unsplash.com/photo-1496483353456-90997957cf99?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=41b8b9c2e1f7c34508103bada6bd25f0&auto=format&fit=crop&w=332&q=80"

if __name__ == '__main__':
    download_web_image(URL)

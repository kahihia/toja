
import re
import urlparse
import requests

from bs4 import BeautifulSoup

import django
django.setup()

from venues.models import Category


def add_category_image(url, soup, category):

    name = category.name
    image = None

    for elem in soup.find_all('a', text=re.compile(r''+name, re.IGNORECASE)):
        try:
            container = elem.parent.parent
            img = container.find('img')
            href = img.get('src')
            href = urlparse.urljoin(url, href)
            image = href
            print(name + ' ' + href)
        except AttributeError:
            pass

    if image is not None:
        category.image = image
        category.save()


def add_all_images():

    url = 'https://gurunavi.com/en/cat/'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    categories = Category.objects.all()
    print(len(categories))
    for category in categories:
        add_category_image(url, soup, category)


if __name__ == '__main__':
    add_all_images()
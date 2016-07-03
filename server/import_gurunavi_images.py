
import requests
from bs4 import BeautifulSoup


def import_images(gurunavi_id):

    url = 'https://gurunavi.com/en/' + gurunavi_id + '/ph/all/rst/'
    request = requests.get(url)

    images = []

    # try:
    soup = BeautifulSoup(request.text, 'html.parser')
    cassette = soup.find('body')\
        .find('div', class_='contents', recursive=False)\
        .find('div', class_='container', recursive=False)\
        .find('div', class_='main', recursive=False)\
        .find('div', class_='cassette', recursive=False)

    try:
        panel = cassette.find('div', class_='panel', recursive=False)
        links = panel.find_all('a')

        for link in links:
            href = link.get('href')
            image = 'http:' + href
            # print(image)
            images.append(image)

    except AttributeError:
        imgs = cassette.find_all('img')
        for img in imgs:
            href = img.get('src')
            image = 'http:' + href
            images.append(image)

    # except AttributeError:
    #     print('No images for ' + gurunavi_id)

    if len(images) == 0:
        images = '[]'
    else:
        images = '["' + '","'.join(images) + '"]'

    return images

if __name__ == '__main__':

    venue_images = import_images('a011200')
    print(len(venue_images))

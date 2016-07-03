import re
import requests
from bs4 import BeautifulSoup

import django
django.setup()

from venues.models import Venue, Food


def create_menu_item(menu):

    # print(menu)

    food = Food()
    food.name_jp = menu.find('div', class_='small').text.strip()
    food.name = menu.find('h3', class_='huge').text.strip()

    if len(food.name) == 0:
        raise ValueError('Ignoring menu item with empty name.')

    try:
        food.description = menu.find('p', class_='default').text.strip()
    except AttributeError as e:
        food.description = ''

    try:
        img = menu.find('img')
        href = img.get('src')
        food.image = href
    except AttributeError:
        food.image = ''

    return food


def get_menus(venue):

    url = find_menu_page(venue)
    print(url)

    if url is None:
        print(venue.gurunavi_id + ': No menu button found.')
        return

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    try:

        menu_container = soup.find('body')\
            .find('div', class_='contents', recursive=False)

        menu_container = menu_container.find('div', class_='container', recursive=False)
        menu_container = menu_container.find('div', class_='main', recursive=False)

            # .find('div', class_='container', recursive=False)
            # .find('div', class_='main', recursive=False)

        found = False

        try:
            container_a = menu_container.find('div', class_='tetris-spacing')
            menu_items = menu_container.find_all('div', class_='cassette', recursive=False)
            found = True
        except AttributeError:
            pass

        # try:
        #print(menu_container)
        menu_items = menu_container.find_all('div', class_='normal-colored', recursive=False)
        found = True
        # except AttributeError as e:
        #     print(e)

        if not found:
            raise AttributeError('Could not find menu container on page.')

        for menu in menu_items:

            try:
                food = create_menu_item(menu)
                food.venue = venue
                food.save()
                print(venue.gurunavi_id + ': ' + food.name)
            except AttributeError as e:
                print(e)
            except ValueError as e:
                print(e)

    except AttributeError as e:
        print('No menu for ' + venue.gurunavi_id + ' ' + str(e))


def find_menu_page(venue):

    try:
        url = 'https://gurunavi.com/en/' + venue.gurunavi_id + '/rst/'
        print(url)
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        menu_bar = soup.find('body').find('div', class_='global-navigation', recursive=False)
        menu_item = menu_bar.find('a', text='Menu')

        return menu_item.get('href')

    except AttributeError:
        return None


if __name__ == '__main__':

    # venue = Venue.objects.get(gurunavi_id='a105600')
    # get_menus(venue)
    # import sys
    # sys.exit()

    Food.objects.all().delete()

    venues = Venue.objects.all()
    for venue in venues:
        print(venue.gurunavi_id)
        get_menus(venue)

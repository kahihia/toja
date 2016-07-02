
import sys
import json
import argparse

import django
django.setup()

from venues.models import Venue, Category
from import_gurunavi_images import import_images


def load_venues(input_filename):
    js_obj = None

    # Load JSON from file
    try:
        with open(input_filename, 'r') as f:
            js_obj = json.load(f)
    except Exception as e:
        print("Parse error.")
        print(e)

    return js_obj


def assign_value(object_from, object_to, property, keylist):

    if len(keylist) == 0:
        setattr(object_to, property, object_from)
    else:
        assign_value(object_from[keylist[0]], object_to, property, keylist[1:])


def json_to_venue(item):

    venue = Venue()

    value_mapping = {
        'name': ['name', 'name'],
        'name_jp': ['name', 'name_sub'],
        'gurunavi_id': ['id'],
        'gurunavi_url': ['url'],
        'longitude': ['location', 'longitude'],
        'latitude': ['location', 'latitude'],
        # 'budget': ['budget'],
        'address': ['contacts', 'address'],
        'phone': ['contacts', 'tel'],
        'description': ['sales_points', 'pr_short'],
        'opening_times': ['business_hour'],
    }

    try:
        venue.budget = float(item['budget'])
    except ValueError:
        venue.budget = 0

    for key in value_mapping:
        try:
            assign_value(item, venue, key, value_mapping[key])
        except KeyError as e:
            print('Could not get key: ' + key + ': ' + str(value_mapping[key]))
            setattr(venue, key, '')

    return venue


def add_categories(venue, js_obj):

    categories = js_obj['categories']['category_name_l']
    categories.extend(js_obj['categories']['category_name_s'])
    categories = [category.split()[0].lower() for category in categories if isinstance(category, unicode)]
    categories = list(set(categories))

    for category in categories:

        stored_category = None

        try:
            stored_category = Category.objects.get(name=category)
        except Category.DoesNotExist:
            stored_category = Category(name=category)
            stored_category.save()

        venue.categories.add(stored_category)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='delete', action='store_const', const=True, default=False)
    args = parser.parse_args()

    if args.delete:
        # Drop all objects before importing.
        all_objects = Venue.objects.all()
        print('Deleting ' + str(len(all_objects)) + 'venues.')
        all_objects.delete()
        print('Now have ' + str(len(Venue.objects.all())) + ' venues.')

        # Drop all categories.
        all_categories = Category.objects.all()
        print('Deleting ' + str(len(all_categories)) + ' categories.')
        all_categories.delete()
        print('Now have ' + str(len(Category.objects.all())) + ' categories.')

    input_filename = 'dump.json'
    objects = load_venues(input_filename)

    if objects is None:
        sys.exit(-1)

    ids = {}

    i = 1
    for item in objects:

        print(str(i) + ' ' + item['id'])
        i += 1

        venue = json_to_venue(item)

        if venue.gurunavi_id in ids:
            ids[venue.gurunavi_id] += 1
            continue

        ids[venue.gurunavi_id] = 1

        # Scrape images from Gurunavi site.
        venue.images = import_images(venue.gurunavi_id)
        venue.save()

        add_categories(venue, item)

    print('Now have ' + str(len(Venue.objects.all())) + ' venues.')
    print('Now have ' + str(len(Category.objects.all())) + ' categories.')


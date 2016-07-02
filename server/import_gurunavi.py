
import sys
import json
import argparse

import django
django.setup()

from venues.models import Venue


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
    venue.images = '[https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg,'\
        + 'https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg]'

    value_mapping = {
        'name': ['name', 'name'],
        'name_jp': ['name', 'name_sub'],
        'gurunavi_id': ['id'],
        'gurunavi_url': ['url'],
        'longitude': ['location', 'longitude'],
        'latitude': ['location', 'latitude'],
        'budget': ['budget'],
        'address': ['contacts', 'address'],
        'phone': ['contacts', 'tel'],
        'description': ['sales_points', 'pr_short'],
        'opening_times': ['business_hour'],
    }

    for key in value_mapping:
        try:
            assign_value(item, venue, key, value_mapping[key])
        except KeyError as e:
            print('Could not get key: ' + key + ': ' + str(value_mapping[key]))
            setattr(venue, key, '')

    from pprint import pprint
    #pprint(vars(venue))

    return venue


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='delete', action='store_const', const=True, default=False)
    args = parser.parse_args()

    if args.delete:
        # Drop all objects before importing.
        all_objects = Venue.objects.all()
        print('Deleting ' + str(len(all_objects)) + '.')
        all_objects.delete()
        print('Now have ' + str(len(Venue.objects.all())) + ' venues.')

    input_filename = 'dump.json'
    objects = load_venues(input_filename)

    if objects is None:
        sys.exit(-1)

    ids = {}

    for item in objects:
        venue = json_to_venue(item)

        if venue.gurunavi_id in ids:
            ids[venue.gurunavi_id] += 1
        else:
            ids[venue.gurunavi_id] = 1
            venue.save()

    print(len(ids))

    print('Now have ' + str(len(Venue.objects.all())) + ' venues.')
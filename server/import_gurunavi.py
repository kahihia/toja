
import sys
import json

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


def json_to_venue(item):

    venue = Venue()

    venue.name = item['name']['name']
    venue.name_jp = item['name']['name_sub']

    venue.gurunavi_id = item['id']
    venue.gurunavi_url = item['url']
    venue.longitude = item['location']['longitude']
    venue.latitude = item['location']['latitude']
    venue.budget = item['budget']

    venue.address = item['contacts']['address']
    venue.phone = item['contacts']['phone']
    venue.description = item['contacts']['sales_points']

    venue.opening_times = item['business_hour']

    return venue


if __name__ == '__main__':
    input_filename = 'dump.json'
    objects = load_venues(input_filename)

    if objects is None:
        sys.exit(-1)

    for item in objects:
        venue = json_to_venue(item)
        venue.save()
        break


import csv
import json
import googlemaps

import django
django.setup()

from places.models import Area, Attraction, Hospital
from server.secrets import GMAPS_KEY


def address_to_latlong(address):
    gmaps = googlemaps.Client(key=GMAPS_KEY)
    geocode_result = gmaps.geocode(address)

    if geocode_result:
        json_string = json.loads(json.dumps(geocode_result[0]))
        lat = json_string['geometry']['location']['lat']
        lng = json_string['geometry']['location']['lng']
        return True, lat, lng

    return False, None, None


def delete_old():
    Area.objects.all().delete()
    Attraction.objects.all().delete()
    Hospital.objects.all().delete()


def add_area(line):
    current_area = Area(name=line[0])
    if len(line) == 2:
        current_area.description = line[1]
    current_area.save()
    return current_area


def add_attraction(line, current_area):

    attraction = Attraction()
    attraction.area = current_area

    attraction.name = line[0]
    attraction.address = line[1]
    attraction.address_jp = line[2]

    if len(attraction.address) > 10:
        success, la, lo = address_to_latlong(attraction.address)
        if success:
            attraction.latitude, attraction.longitude = la, lo
            attraction.has_location = True

    images = []

    if len(line) >= 4:
        attraction.description = line[3]

        images = []
        for i in xrange(4, len(line)):
            img_url = line[i].strip()
            if len(img_url) > 0:
                images.append(line[i])

    if len(images) > 0:
        attraction.images = '["' + '","'.join(images) + '"]'
    else:
        attraction.images = '[]'

    attraction.save()
    return attraction


def add_hospitals(input_file):
    with open(input_file, 'rU') as f:

        reader = csv.DictReader(f)

        for line in reader:

            hospital = Hospital()
            hospital.name = line['Name']
            hospital.tel = line['Tel']
            hospital.hours = line['Hours']
            hospital.after_hours = line['After hours']
            hospital.address = ", ".join([line['Address'], line['City']])
            hospital.url = line['Link']
            hospital.image = line['Picture']

            success, lat, lon = address_to_latlong(hospital.address)
            if success:
                hospital.has_location = True
                hospital.latitude, hospital.longitude = lat, lon

            hospital.save()


def add_area_attraction_data(input_file):
    with open(input_file, 'r') as f:

        current_area = None
        reader = csv.reader(f)

        for line in reader:

            # Drop empty cells (,,,,).
            line = [cell.strip() for cell in line if len(cell.strip()) > 0]

            # Skip blank lines.
            if len(line) == 0:
                continue

            # New area category.
            if 1 <= len(line) <= 2:
                current_area = add_area(line)
                continue

            # Add an attraction to the current area.
            add_attraction(line, current_area)

if __name__ == '__main__':

    delete_old()
    add_area_attraction_data('locations.csv')
    add_hospitals('hospital.csv')


import django
django.setup()

from places.models import Area, Attraction

import csv


def delete_old():
    Area.objects.all().delete()
    Attraction.objects.all().delete()


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


def add_new_data(input_file):
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
    add_new_data('locations.csv')


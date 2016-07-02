import django
django.setup()

from places.models import Area, Attraction

import csv

input_file = 'locations.csv'

Area.objects.all().delete()
Attraction.objects.all().delete()


with open(input_file, 'r') as f:

    current_area = None

    reader = csv.reader(f)
    
    for line in reader:

        line = [cell.strip() for cell in line if len(cell.strip()) > 0]

        if len(line) == 0:
            continue

        if 1 <= len(line) <= 2:
            current_area = Area(name=line[0])
            if len(line) == 2:
                current_area.description = line[1]
            current_area.save()
            continue

        # Otherwise add attraction to that area.
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

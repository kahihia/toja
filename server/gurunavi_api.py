import json
import requests
import argparse


# Execute query against API.
def request(base_url, params):

    params['keyid'] = '9697d47a8e9afcf3b214700fffe77d97'
    params['format'] = 'json'
    params['lang'] = 'en'

    return requests.get(base_url, params=params)


# Execute lookup request.
def general(params):
    base_url = 'http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/'
    return request(base_url, params)


# Get API master.
def master(params):
    base_url = 'http://api.gnavi.co.jp/master/AreaSearchAPI/20150630/'
    return request(base_url, params)


# Display json prettily.
def pp(json_obj):
    print json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))


def get_establishments():
    # Get areas.
    m = master({})

    # Find Tokyo's area code.
    tokyo = [area for area in json.loads(m.text)['area'] if 'Tokyo' in area['area_name']][0]

    # Find out how many restaurants there are in that area:
    result = general({'area': tokyo['area_code']})
    total_establishments = int(result.json()['total_hit_count'])

    # Can't have more than this many results per query.
    max_hit = 500

    # Now know total requests needed.
    number_requests = int(total_establishments/max_hit) + 1

    # Store data we receive.
    data = []

    # Download all the information about all establishments in Tokyo.
    for i in xrange(1, number_requests+1):

        # Execute query.
        result = general({'area': tokyo['area_code'], 'hit_per_page': max_hit, 'offset': i})

        # Check HTTP error state.
        if not result.ok:
            print('API query failed (' + str(result.status_code) + ')')
            continue

        # Verify JSON.
        try:
            js_obj = result.json()

        except ValueError:
            print("Could not decode JSON from:")
            print(result.text)
            continue

        # API doesn't use HTTP error codes, therefore have to check error state in returned JSON.
        if 'error' in js_obj:
            print(str(i) + '/' + str(number_requests) + ': Error ' + js_obj['error']['code'] + ' - ' + js_obj['error']['message'])
            continue

        # Select rest object; this contains list of establishments.
        js_obj = js_obj['rest']

        # Add to storage.
        data.extend(js_obj)

        print(str(i) + '/' + str(number_requests) + ': ' + str(len(data)) + ' establishments collected.')

    return data


def dump_establishments(filename, establishments):

    # Write downloaded data to file.
    with open(filename, 'w') as f:
        json.dump(establishments, f)


def load_establishments(filename):
    with open(filename, 'r') as f:
        js_obj = json.load(f)

    return js_obj

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='download', action='store_const', const=True, default=False)
    args = parser.parse_args()

    dump_file = 'dump.json'

    if args.download:

        establishments = get_establishments()
        dump_establishments(dump_file, establishments)

        js_obj = load_establishments(dump_file)
        assert len(js_obj) == len(establishments)

    js_obj = load_establishments(dump_file)
    print('Loaded ' + str(len(js_obj)) + ' records from file.')

    pp(js_obj[0])

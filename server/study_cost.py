from import_gurunavi import load_venues


venues = load_venues('dump.json')


costs = []

for venue in venues:
    try:
        value = int(venue['budget'])
        costs.append(value)
    except ValueError:
        pass

with open('output.csv', 'w') as f:
    for cost in costs:
        f.write(str(cost)+'\n')

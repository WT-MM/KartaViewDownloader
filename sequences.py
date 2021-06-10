import osmnx
import requests


def getCoords(*args):
    #In form (x,y) where x = longitude and y = latitude
    query = ",".join(args)
    try:
        return [(n[1]['x'], n[1]['y']) for n in list(osmnx.graph_from_place(query).nodes(data=True))]
    except ValueError as err:
        print("ValueError: ", err)
        quit()

def pullSequences(coords):
    url = "http://openstreetcam.org/nearby-tracks"
    data = {'lat': coords[1], 'lng' : coords[0], 'distance' : '10'}

    r = requests.post(url=url, data=data)

    sequences = []
    osv = r.json()['osv']
    if(type(osv) is dict):
        for i in osv['sequences']:
            sequences.append(i['sequence_id'])

    return sequences

def getAllSequences(*args):
    uniqueSequences = set()
    for i in getCoords(*args):
        for j in pullSequences(i):
            uniqueSequences.add(j)
    return uniqueSequences

print(getAllSequences("Palo Alto", "California", "United States"))


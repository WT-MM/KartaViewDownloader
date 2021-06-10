import osmnx
import requests


def getCoords(*args):
    #In form (x,y) where x = longitude and y = latitude
    query = ",".join(args)
    try:
        return [(n[1]['x'], n[1]['y']) for n in list(osmnx.graph_from_place(query).nodes(data=True))]
    except ValueError as err:
        print("ValueError: ", err)
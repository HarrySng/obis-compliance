from .setup import *
from .helpers import *
from.generate_report import *

def check_coordinates_depth():
    crd = {}
    for col in ['decimalLatitude','decimalLongitude','minimumDepthInMeters','maximumDepthInMeters']:
        data = set(get_column('event', col))
        data = [x for x in data if str(x) != 'nan']
        data = list(map(float,data))
        crd[col] = [min(data), max(data)]
    write_coordinates_depth(crd)
    return
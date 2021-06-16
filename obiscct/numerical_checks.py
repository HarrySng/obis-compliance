from .setup import *
from .helpers import *
from.generate_report import *

def check_coordinates_depth():
    bounds = get_bounds()
    crd = {}
    msgs = ['']
    for col in ['decimalLatitude','decimalLongitude','minimumDepthInMeters','maximumDepthInMeters']:
        data = get_column('event', col)
        data = [x for x in data if str(x) != 'nan']
        data = list(map(float,data))
        crd[col] = [min(set(data)), max(set(data))] # Create a table to print min max
        # Now check bounds
        num_less_than_bounds = sum(d < bounds[col][0] for d in data)
        num_more_than_bounds = sum(d > bounds[col][1] for d in data)
        msgs.append('\nAccording to bounds defined in setup file for **{}** [{}, {}]:\n'.format(col, bounds[col][0], bounds[col][1]))
        if num_less_than_bounds < 1:
            msgs.append('* All values are within the minimum threshold.\n')
        else:
            msgs.append('* *Warning*! {} values are beyond the minimum threshold.\n'.format(num_less_than_bounds))    
        if num_more_than_bounds < 1:
            msgs.append('* All values are within the maximum threshold.\n')
        else:
            msgs.append('* *Warning*! {} values are beyond the maximum threshold.\n'.format(num_more_than_bounds))  
    write_coordinates_depth(crd)
    write_message(msgs)

    return
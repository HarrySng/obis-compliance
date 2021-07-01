from numpy import append
from .setup import *
from .helpers import *
from.generate_report import *

def check_coordinates_depth():
    """[summary]
    """
    
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

def check_wkt_centroid(f = 'event.csv', field = 'footprintWKT'):
    """[summary]

    Args:
        f (str, optional): [description]. Defaults to 'event.csv'.
        field (str, optional): [description]. Defaults to 'footprintWKT'.
    """

    msgs = []
    
    df = pd.read_csv(tmp_path + f)
    wkt_indices = df[df[field].notnull()].index.tolist()
    
    if len(wkt_indices) > 0:
        msgs.append('eventID | Centroid in File | Calculated Centroid\n')
        msgs.append(':---: | :---: | :---:\n')
    
    faulty_wkt_events = []
    
    for i in wkt_indices:
        wkt_string = df[field][i]
        
        try:
            if 'POLYGON' in wkt_string:
                wkt_fields = wkt_string.split('N')[1].split(',')
                
                coords = []
                for f in wkt_fields:
                    # Remove special characters, split by space
                    c = f.replace('(', '').replace(')', '').split(' ')
                    
                    if len(c) == 2:
                        coords.append(c)
                    else:
                        coords.append(c[1:3])
            
            centroid = calculate_centroid(coords)
            eventID = df['eventID'][i]
            existing_centroid = str(df['decimalLongitude'][i]) + ', ' + str(df['decimalLatitude'][i])
            
            if existing_centroid == ', ':
                existing_centroid = 'NA, NA'
            msgs.append('{} | {} | {}\n'.format(eventID, existing_centroid, str(centroid[0]) + ', ' + str(centroid[1])))
        
        except:
            faulty_wkt_events.append(df['eventID'][i])

    if len(faulty_wkt_events) > 0:
        msgs.append('\n**WARNING**: The footprintWKT field of the following eventIDs could not be parsed. Please check their format.\n')
        for id in faulty_wkt_events:
            msgs.append('* eventID: {}\n'.format(id))    
    
    write_message(msgs)

    return
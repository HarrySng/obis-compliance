from .setup import *
from .helpers import *
from.generate_report import *

def check_p06(f = 'extendedmeasurementorfact.csv'):

    df = pd.read_csv(tmp_path + f)
    p06 = df['measurementUnitID'].tolist()

    cache_records = [] # Do not send GET request if request for same record sent earlier
    records = {}

    for i in range(0, len(p06)):
        vocab = p06[i]
        if vocab in cache_records:
            continue
        else:
            resp = requests.get(vocab + '?_profile=skos&_mediatype=application/json')

            if resp.status_code != 200:
                records[vocab] = None
                continue
            record = json.loads(resp.text)[0]

            for k in record:
                if 'prefLabel' in k:
                    records[vocab] = record[k][0]['@value']

            cache_records.append(vocab)
    
    munit = df['measurementUnit'].tolist()
    

    """
    Mismatches could occur in several combinations
    A single term could have two different mismatch
    units so both need to be captured. On the other
    hand, the same kind of mismatch for a single term
    does not need to be captured repeatedly.
    """
    mismatches = []
    for i in range(0, len(p06)):
        vocab = p06[i]
        unit = munit[i]
        if records[vocab] is None:
            mismatches.append([vocab, unit, 'Term not found'])
        else: 
            if records[vocab] != unit:
                mismatches.append([vocab, unit, records[vocab]])
    
    df = pd.DataFrame(mismatches, columns = ['Term', 'Unit', 'prefLabel'])
    df = df.drop_duplicates() # This captures all unqiue combinations of mismatches

    msgs = ['### Measurement Unit ID Checks\n']
    msgs.append('Term | Measurement Unit in File | prefLabel on Server\n')
    msgs.append(':---: | :---: | :---:\n')
    for i, row in df.iterrows():
        msgs.append('{} | {} | {}\n'.format(row['Term'], row['Unit'], row['prefLabel']))
    msgs.append('\n---\n')
    write_message(msgs)

    return
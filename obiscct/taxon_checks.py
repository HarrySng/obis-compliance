from .setup import *
from .helpers import *
from .generate_report import *

def check_scientific_names(f = 'occurrence.csv'):
    
    
    df = pd.read_csv(tmp_path + f)
    sc_names = df['scientificName'].tolist()

    cache_records = {} # Do not send GET request if request for same record sent earlier
    missing_id = [] # Indices of scientific names which returned bad response for Aphia IDs
    mismatches = {
        'scientificNameID': [],
        'scientificNameAuthorship': [],
        'bibliographicCitation': []
    }
    true_records = {
        'scientificNameID': [],
        'scientificNameAuthorship': [],
        'bibliographicCitation': []
    }
    for i in range(0, len(sc_names)):
        sc_name = sc_names[i]
        if sc_name in cache_records.keys():
            aphia_record = cache_records[sc_name]
        else:
            url_aphia_id = 'https://www.marinespecies.org/rest/AphiaIDByName/' + sc_name + '?marine_only=true'
            resp = requests.get(url_aphia_id)

            if resp.status_code != 200:
                missing_id.append(i)
                continue
            
            aphia_id = resp.text

            url_aphia_record = 'https://www.marinespecies.org/rest/AphiaRecordByAphiaID/' + aphia_id
            resp = requests.get(url_aphia_record)

            if resp.status_code != 200:
                # Handle this
                continue

            aphia_record = json.loads(resp.text)
            cache_records[sc_name] = aphia_record

        # Implement checks
        if aphia_record['lsid'] != df['scientificNameID'][i]:
            mismatches['scientificNameID'].append(i)
        
        if aphia_record['citation'].split('Accessed')[0] != df['bibliographicCitation'][i].split('Accessed')[0]:
            mismatches['bibliographicCitation'].append(i)
        
        if isinstance(df['scientificNameAuthorship'][i], float): # nan values are floats
            if aphia_record['authority'] is not None:
                mismatches['scientificNameAuthorship'].append(i)
        else:
            if aphia_record['authority'] != df['scientificNameAuthorship'][i]:
                mismatches['scientificNameAuthorship'].append(i)
        
        true_records['scientificNameID'].append(aphia_record['lsid'])
        true_records['bibliographicCitation'].append(aphia_record['citation'])
        true_records['scientificNameAuthorship'].append(aphia_record['authority'])


    
    for k in mismatches:
        msgs = []
        if len(mismatches[k]) > 0:
            msgs.append('The {} field for the following records did not match the Aphia Record.\n\n'.format(k))
            msgs.append('occurrenceID | eventID | scientificName | {} In File | {} in Aphia Record\n'.format(k, k))
            msgs.append(':---: | :---: | :---: | :---: | :---:\n')
            for i in mismatches[k]:
                occurrenceID = df['occurrenceID'][i]
                eventID = df['eventID'][i]
                scientificName = df['scientificName'][i]
                true_record = true_records[k][i]
                msgs.append('{} | {} | {} | {} | {}\n'.format(occurrenceID,eventID,scientificName,df[k][i], true_record))
            msgs.append('\n---\n')
        write_message(msgs)
    
    return

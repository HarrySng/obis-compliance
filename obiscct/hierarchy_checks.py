from .setup import *
from .helpers import *
from.generate_report import *

def check_missing_ids(child, parent, ids):
    missing_ids = []
    for id in ids[child]:
        if id not in ids[parent]:
            missing_ids.append(id)
    return missing_ids

def check_parent_events():
    event_id = set(get_column('event', 'eventID'))
    parent_event_id = set(get_column('event', 'parentEventID'))
    parent_event_id = [x for x in parent_event_id if str(x) != 'nan'] # Remove nan parent ID for cruise level
    missing_ids = []
    for id in parent_event_id:
        if id not in event_id:
            missing_ids.append(id)
    msgs = []
    if len(missing_ids) < 1:
        msgs.append('\nAll **event** core records have a valid **parentEventID**.\n\n')
        write_message(msgs)
    return

def check_event_ids(col_name = 'eventID'):
    event_ids = {}
    for core in ['event', 'occurrence', 'extendedmeasurementorfact']:
        event_ids[core] =  set(get_column(core, col_name)) # Use set to only get unique. Use map to convert all to str
    for child in ['occurrence', 'extendedmeasurementorfact']:
        missing_ids = check_missing_ids(child, 'event', event_ids)
        msgs = []
        if len(missing_ids) < 1:
            msgs.append('\nAll **{}** core records have a valid **{}**.\n\n'.format(child, col_name))
            write_message(msgs)
    return

def check_occurrence_ids(col_name = 'occurrenceID'):
    occurrence_ids = {}
    for core in ['occurrence', 'extendedmeasurementorfact']:
        ids = set(get_column(core, col_name))
        ids = [x for x in ids if str(x) != 'nan'] # Remove nans
        occurrence_ids[core] = ids
    missing_ids = check_missing_ids('extendedmeasurementorfact','occurrence',occurrence_ids)
    msgs = []
    if len(missing_ids) < 1:
        msgs.append('\nAll **extendedmeasurementorfact** core records have a valid **occurrenceID**.\n\n')
        write_message(msgs)
    return
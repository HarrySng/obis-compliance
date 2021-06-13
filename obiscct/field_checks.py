from .setup import *
from .helpers import *
from.generate_report import *

def validate_required_fields(f):
    """
    """
    if "xml" in f:
        return
    core = f.split(".")[0] # Extract name without extension for use with dict objects in setup file
    df = pd.read_csv(tmp_path + f)
    req_fields = get_required_fields(core) # From setup file
    # req_fields is a dict with 4 keys. Each value is a list of required fields.
    missing_fields = {}
    for k in req_fields:
        missing_fields[k] = []
        fields = req_fields[k]
        if fields is None: # No required field
            continue
        for field in fields: # Iterate over each element of list
            na_index = df[df[field].isnull()].index.tolist()
            if len(na_index) > 0:
                missing_fields[k].append({field: na_index})
    
    write_missing_fields(core, missing_fields) # Send to generate_report

    return

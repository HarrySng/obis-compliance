from obiscct.setup import *
from obiscct.helpers import *
from obiscct.generate_report import *
from obiscct import file_checks
from obiscct import field_checks

def wrapper(file):

    create_report(file) # Initiate a file with header info
    
    # File level checks
    file_checks.extract_file(file)
    file_checks.names_and_counts() # Will raise exception and stop code execution if files incomplete
    for f in expected_files: # Iterate over each file
        file_checks.validate_header(f) # Validate headers. Function only checks csv files
        
    # Field level checks
    write_message(['## Validation of Required Fields\n'])
    for f in expected_files:
        field_checks.validate_required_fields(f)

    return

if __name__ == "__main__":
    wrapper()
    
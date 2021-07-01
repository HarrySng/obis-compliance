from obiscct.setup import *
from obiscct.helpers import *
from obiscct.generate_report import *
from obiscct import file_checks
from obiscct import field_checks
from obiscct import hierarchy_checks
from obiscct import date_checks
from obiscct import numerical_checks

def wrapper(file = 'obisdata.zip'): # Default for testing
    
    create_report(file) # Initiate a file with header info
    
    # File Level checks
    expected_files = get_expected_files()
    #file_checks.extract_file(file)
    file_checks.names_and_counts() # Will raise exception and stop code execution if files incomplete
    
    # File Header Checks
    write_message(['## Header Checks\n'])
    for f in expected_files: # Iterate over each file
        file_checks.validate_header(f) # Validate headers. Function only checks csv files
    
    # Field Level Checks
    write_message(['## Validation of Required Fields\n'])
    for f in expected_files:
        field_checks.validate_required_fields(f)
    
    # Hierarchy Checks
    write_message('\n---\n')
    write_message(['## Hierarchical ID Checks\n'])
    hierarchy_checks.check_parent_events()
    hierarchy_checks.check_event_ids()
    hierarchy_checks.check_occurrence_ids()
    
    # Numerical Checks
    write_message('\n---\n')
    write_message(['## Site Checks\n']) # Implemented in numerical_checks.py
    numerical_checks.check_coordinates_depth()
    write_message(['\n## FootprintWKT Centroid Checks\n'])
    numerical_checks.check_wkt_centroid()
    
    # Date Checks
    write_message('\n---\n')
    write_message(['## Date Checks\n']) # Implemented in date_checks.py
    for col in ['eventDate','modified']:
        date_checks.check_date_format(col)

    # Taxon Checks
    write_message('\n---\n')
    write_message(['## Taxonomic Checks\n']) # Implemented in taxon_checks.py
    
    return

if __name__ == "__main__":
    wrapper()
    
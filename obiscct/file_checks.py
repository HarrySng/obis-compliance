from .setup import *
from .helpers import *
from.generate_report import *

def extract_file(file):
    """[summary]

    Args:
        file ([type]): [description]
    """
    
    remove_all_files(tmp_path) # helper. Remove any existing files from tmp folder
    
    try:
        with ZipFile(in_path + file, 'r') as zf:
            zf.extractall(tmp_path) # Extract zip package into the tmp folder
    except OSError:
        print('Unable to open', file)
    except Exception as e:
        print("An error occurred", e.args)
    
    return

def names_and_counts():
    """[summary]

    Raises:
        Exception: [description]
    """

    files = os.listdir(tmp_path)
    expected_files = get_expected_files() # From setup file
    equal = collections.Counter(files) == collections.Counter(expected_files) # Check if two lists are equal irrespective of order
    msgs = ['']
    msgs.append('\n## File Checks\n')
    
    if equal:
        msgs.append('\nThe package contains all expected files.\n\n')
        write_message(msgs)
    
    if not equal:
        missing_files = np.setdiff1d(expected_files, files)
        msgs.append("\nThis package is missing the following files:\n")
        for mf in missing_files:
            msgs.append('\n* ' + mf)
        msgs.append('\n---\n')    
        msgs.append('**ERROR**: Further validation cannot be completed without the complete package.')
        write_message(msgs)
        raise Exception("OBIS package incomplete!")
    
    return

def validate_header(f):
    """[summary]

    Args:
        f ([type]): [description]

    Raises:
        Exception: [description]
    """

    if "xml" in f:
        return
    
    core = f.split(".")[0] # Extract name without extension for use with dict objects in setup file
    df = pd.read_csv(tmp_path + f)
    hdrs = list(df.columns)
    col_headers = get_headers(core)
    equal = collections.Counter(hdrs) == collections.Counter(col_headers)
    
    msgs = []
    if not equal:
        print("Error: " + f)
        raise Exception("Column headers for this file do not match the expected headers in setup file!")
    else:
        msgs.append('\nThe **{}** file contains all expected headers.\n\n'.format(f))
        write_message(msgs)
    
    return
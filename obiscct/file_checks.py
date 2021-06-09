from .setup import *
from .helpers import *
from.generate_report import *

def extract_file(file):
    """
    Takes a zip file as input argument.
    Cleans the /tmp/ directory.
    Extracts contents into /tmp/ directory.
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
    """
    After extract_file() unpacks zip into /tmp/
    This function checks if the list of files in directory
    matches the expected_file list defined in setup file.
    Raises exception if mismatch and stop code execution of wrapper.
    """
    files = os.listdir(tmp_path)
    equal = collections.Counter(files) == collections.Counter(expected_files) # Check if two lists are equal irrespective of order
    if not equal:
        print("The package should contain 5 files with exact names as following:", *expected_files,sep="\n")
        print("\n", "#" * 15, "\n")
        if len(files) == 0:
            raise Exception("No files found!")
        else:
            missing_files = np.setdiff1d(expected_files, files)
            print("This package is missing the following files:")
            print(*missing_files,sep="\n")
            print("\n")
            raise Exception("OBIS package incomplete!")
    return

def validate_header(f):
    """
    Takes a csv file name as input.
    Checks header against expected values in setup file.
    """
    if "xml" in f:
        return
    
    core = f.split(".")[0] # Extract name without extension for use with dict objects in setup file
    df = pd.read_csv(tmp_path + f)
    hdrs = list(df.columns)
    equal = collections.Counter(hdrs) == collections.Counter(col_headers[core])
    if not equal:
        print("Error: " + f)
        raise Exception("Column headers for this file do not match the expected headers in setup file!")
    return
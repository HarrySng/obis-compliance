from .setup import *
from .helpers import *

def extract_file(file):
    remove_all_files(tmp_path) # Remove any existing files from tmp folder
    try:
        with ZipFile(in_path + file, 'r') as zf:
            zf.extractall(tmp_path) # Extract zip package into the tmp folder
    except OSError:
        print('Unable to open', file)
    except Exception as e:
        print("An error occurred", e.args)

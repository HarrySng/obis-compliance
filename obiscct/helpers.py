from .setup import *

def remove_all_files(path):
    files = glob.glob(path + "*", recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Could not empty the tmp folder. Error: ", e.args)
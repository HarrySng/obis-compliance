from .setup import *

def remove_all_files(path):
    files = glob.glob(path + "*", recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Could not empty the tmp folder. Error: ", e.args)

def get_column(core, hdr):
    df = pd.read_csv(tmp_path + core + ".csv", dtype=str)
    col = df[hdr].tolist() # Extract column and convert to list
    return col

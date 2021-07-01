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

def calculate_centroid(coords):
    """[summary]

    Args:
        coords ([type]): [description]

    Returns:
        [type]: [description]
    """

    lons = []
    lats = []
    for c in coords:
        lons.append(float(c[0]))
        lats.append(float(c[1]))

    return [sum(lons)/len(lons), sum(lats)/len(lats)]

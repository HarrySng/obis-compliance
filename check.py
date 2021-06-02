from obiscct.setup import *
from obiscct import file_checks

def wrapper(file):
    file_checks.extract_file(file)
    return

if __name__ == "__main__":
    wrapper()
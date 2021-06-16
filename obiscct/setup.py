import os
import sys
import glob
import yaml
import collections
import numpy as np
import pandas as pd
from os import listdir
from zipfile import ZipFile
from datetime import datetime

in_path = './input/'
out_path = './output/'
tmp_path = './tmp/'

with open("setup.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as E:
        print(E)

def get_expected_files():
    expected_files = yaml_data[0]['expected_files']
    return expected_files

def get_headers(core):
    headers = yaml_data[1][core] # core is sent by validate_header function in file_checks
    return headers

def get_required_fields(core):
    required_fields = yaml_data[2][core]
    return required_fields


def get_bounds():
    bounds = {}
    for k in ['decimalLatitude', 'decimalLongitude']:
        bounds[k] = yaml_data[3][k]
    """
    Repeat depth into these two variables. 
    This is to get a single input from user.
    Keeping things simple for the user and handling it here.
    These keys will be called as is in numerical_checks.
    """
    bounds['minimumDepthInMeters'] = yaml_data[3]['DepthInMeters']
    bounds['maximumDepthInMeters'] = yaml_data[3]['DepthInMeters']
    return bounds
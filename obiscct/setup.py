import os
import sys
import glob
import collections
import numpy as np
import pandas as pd
from os import listdir
from zipfile import ZipFile
from datetime import datetime

in_path = './input/'
out_path = './output/'
tmp_path = './tmp/'

expected_files = ['event.csv', 'occurrence.csv', 'extendedmeasurementorfact.csv', 'eml.xml', 'meta.xml']

col_headers = {
    'event': ['eventID', 'parentEventID', 'eventRemarks', 'eventDate', 'modified', 'type', 'habitat', 'decimalLatitude', 'decimalLongitude', 'minimumDepthInMeters', 'maximumDepthInMeters', 'verbatimCoordinateSystem', 'geodeticDatum', 'footprintWKT'],
    'occurrence': ['occurrenceID', 'eventID', 'eventRemarks', 'type', 'basisOfRecord', 'recordedBy', 'occurrenceStatus', 'vernacularName', 'scientificName', 'identificationQualifier', 'scientificNameID', 'scientificNameAuthorship', 'nomenclaturalCode', 'taxonRank', 'behavior', 'associatedMedia', 'institutionCode', 'collectionCode', 'bibliographicCitation'],
    'extendedmeasurementorfact': ['eventID', 'occurrenceID', 'measurementID', 'measurementType', 'measurementTypeID', 'measurementValue', 'measurementValueID', 'measurementUnit', 'measurementUnitID', 'measurementMethod']
}

required_fields = {
    'event': {
        'obis': ['eventDate','decimalLatitude','decimalLongitude'],
        'cioos': ['eventID','modified','type','verbatimCoordinateSystem','geodeticDatum'],
        'onc': [],
        'rec': ['parentEventID','eventRemarks','minimumDepthInMeters','maximumDepthInMeters']
    },
    'occurrence': {
        'obis': ['occurrenceID','basisOfRecord','occurrenceStatus','scientificName','scientificNameID'],
        'cioos': ['eventID','type','recordedBy','institutionCode'],
        'onc': ['vernacularName','scientificNameAuthorship','nomenclaturalCode', 'taxonRank','associatedMedia','bibliographicCitation'],
        'rec': ['identificationQualifier']
    },
    'extendedmeasurementorfact': {
        'obis': [],
        'cioos': ['eventID','measurementID','measurementType','measurementValue'],
        'onc': [],
        'rec': []
    },
    'eml': {
        'obis': ['alternativeIdentifier','title','langauge','abstract','keyword','keywordThesaurus','geographicDescription','westBoundingCoordinate','eastBoundingCoordinate','northBoundingCoordinate','southBoundingCoordinate','maintenanceUpdateFrequency','contact','surName','organizationName','electronicMailAddress'],
        'cioos': [],
        'onc': [],
        'rec': []
    }
}

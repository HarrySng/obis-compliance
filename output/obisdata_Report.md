# OBIS Compliance Check Report

OBIS Package Name: **obisdata.zip**

Package uploaded at 2021-07-14 22:58:20 local time.

---
This report is generated using the obis-compliance package.
For more details, please go to the following link: https://github.com/HarrySng/obis-compliance

---

## File Checks

The package contains all expected files.

## Header Checks

The **event.csv** file contains all expected headers.


The **occurrence.csv** file contains all expected headers.


The **extendedmeasurementorfact.csv** file contains all expected headers.

## Validation of Required Fields

---
### Missing fields for the **event** core

Required by | Field | No. of missing values
:---: | :---: | :---:
obis | decimalLatitude | 4
obis | decimalLongitude | 4
rec | parentEventID | 1
rec | minimumDepthInMeters | 3
rec | maximumDepthInMeters | 3
* *Warning*! 1 record(s) is/are missing both coordinates and footprintWKT fields.

---
### Missing fields for the **occurrence** core

Required by | Field | No. of missing values
:---: | :---: | :---:
onc | scientificNameAuthorship | 7
onc | taxonRank | 1

---
### Missing fields for the **extendedmeasurementorfact** core

Required by | Field | No. of missing values
:---: | :---: | :---:
cioos | measurementID | 154

---
## Hierarchical ID Checks

All **event** core records have a valid **parentEventID**.


All **occurrence** core records have a valid **eventID**.


All **extendedmeasurementorfact** core records have a valid **eventID**.


All **extendedmeasurementorfact** core records have a valid **occurrenceID**.


---
## Site Checks
### Bounding Coordinates and Depth of the records.

&nbsp; | Latitude | Longitude | Minimum Depth (m) | Maximum Depth (m)
:---: | :---: | :---: | :---: | :---:
**Minimum** | 46.99999 | -130.0 | -0.6 | 84.9
**Maximum** | 48.69979 | 128.02909 | 2193.0 | 2661.7

According to bounds defined in setup file for **decimalLatitude** [45, 48]:
* All values are within the minimum threshold.
* *Warning*! 157 values are beyond the maximum threshold.

According to bounds defined in setup file for **decimalLongitude** [-128, -124]:
* *Warning*! 69 values are beyond the minimum threshold.
* *Warning*! 1 values are beyond the maximum threshold.

According to bounds defined in setup file for **minimumDepthInMeters** [0, 2500]:
* *Warning*! 2 values are beyond the minimum threshold.
* All values are within the maximum threshold.

According to bounds defined in setup file for **maximumDepthInMeters** [0, 2500]:
* All values are within the minimum threshold.
* *Warning*! 2 values are beyond the maximum threshold.

## FootprintWKT Centroid Checks
eventID | Centroid in File | Calculated Centroid
:---: | :---: | :---:
2741 | -128.02909, 47.85035 | -128.0290895, 47.850352
1950 | 128.02909, 47.85035 | -128.0290895, 47.850352
VS000106 | nan, nan | -128.0290895, 47.850352
VS000107 | nan, nan | -128.0290895, 47.850352
VS000108 | nan, nan | -128.0290895, 47.850352
1940 | -128.02909, 47.85035 | -128.0290895, 47.850352

**WARNING**: The footprintWKT field of the following eventIDs could not be parsed. Please check their format.
* eventID: 2731

---
## Date Checks

### Date Checks for 'eventDate' field.
* Earliest Date: 2018-07-21 00:00:00
* Latest Date: 2018-08-05 00:00:00

### Date Checks for 'modified' field.
* Earliest Date: 2018-07-29 18:11:27
* Latest Date: 2020-07-28 22:44:00

---
## Vocabulary Checks
### Measurement Unit ID Checks
Term | Measurement Unit in File | prefLabel on Server
:---: | :---: | :---:
http://vocab.nerc.ac.uk/collection/P06/current/UPAA/ | degrees Celcius | Degrees Celsius
http://vocab.nerc.ac.uk/collection/P06/current/UUUU/ | dimensionless | Dimensionless
http://vocab.nerc.ac.uk/collection/P06/current/UVAA/ | metres per second | Metres per second

---

---
## Taxonomic Checks
The scientificNameID field for the following records did not match the Aphia Record.

occurrenceID | eventID | scientificName | scientificNameID In File | scientificNameID in Aphia Record
:---: | :---: | :---: | :---: | :---:
826061 | 561921 | Pectis | urn:lsid:marinespecies.org:taxname:231550 | urn:lsid:marinespecies.org:taxname:1371

---
The scientificNameAuthorship field for the following records did not match the Aphia Record.

occurrenceID | eventID | scientificName | scientificNameAuthorship In File | scientificNameAuthorship in Aphia Record
:---: | :---: | :---: | :---: | :---:
825711 | 561631 | Dosidicus gigas | (dOrbigny [in 1834-1847], 1835) | Gill, 1893

---
The bibliographicCitation field for the following records did not match the Aphia Record.

occurrenceID | eventID | scientificName | bibliographicCitation In File | bibliographicCitation in Aphia Record
:---: | :---: | :---: | :---: | :---:
816441 | 552751 | Actinopterygii | WoRMS (2020). Actinopterygii. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=10194 on 2021-01-04 | WoRMS (2021). Actinopterygii. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=10194 on 2021-07-15
816581 | 552891 | Myctophidae | Froese, R. and D. Pauly. Editors. (2020). FishBase. Myctophidae Gill, 1893. Accessed through: World Register of Marine Species at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=125498 on 2021-01-04 | Froese, R. and D. Pauly. Editors. (2021). FishBase. Myctophidae Gill, 1893. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=125498 on 2021-07-15
14373320 | 5037810 | Pyrosoma | Madin, L. (2020). World List of Thaliacea. Pyrosoma Péron, 1804. Accessed through: World Register of Marine Species at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=137224 on 2021-01-04 | Madin, L. (2021). World List of Thaliacea. Pyrosoma Péron, 1804. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=137224 on 2021-07-15
826061 | 561921 | Pectis | Schuchert, P. (2021). World Hydrozoa Database. Voragonema Naumov, 1971. Accessed through: World Register of Marine Species at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=231550 on 2021-01-15 | Schuchert, P. (2021). World Hydrozoa Database. Siphonophorae. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1371 on 2021-07-15

---

# OBIS Compliance Check Report

OBIS Package Name: **obisdata.zip**

Package uploaded at 2021-06-16 15:23:57 local time.

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

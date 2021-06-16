# OBIS Compliance Check Tool

### Note: Under active development

## High level Design
* A single executable program.
* User defines custom requirements in setup.yaml file.
* Input: One .zip file (an OBIS package).
* Output: Report of all checks (pass/fail) + Additional Details.

## Checks

### File-level Checks
* Number of files in package.
* Names of files (will be checked against a default reference).
* Column headers (will be checked against a default reference).
* Number of records in each file (Unique events, Unique child occurrences and unique child EMOFs) (to print out in report).

### Hierarchical Relationship Checks
* Check all IDs (Event, Occurrence, EMOF etc.) and their cross-relationships. Look for non-existent IDs or broken relationships.

### Required Fields Checks
* Check existence (only existence, not the value) of required fields (at all levels - OBIS, CIOOS, ONC).

### Numerical Value Checks
* Check depths, coordinate values for incorrect values (coordinates on land, negative depths etc).

### Taxonomy Checks
* Taxon matching using the WoRMS API by AphiaID.

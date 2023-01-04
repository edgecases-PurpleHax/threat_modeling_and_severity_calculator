# Threat Modeling and Severity Calculator

## Threat Models used


- OWASP
- STRIDE
- CVSS

## What does it do?

### DREAD Calculator

- Use this selection to perform a DREAD Severity Rating. There is an option to write to a report at the end, it is a
  text file that can be used at the end of a threat analysis report.

### OWASP

- Use this selection to perform a OWASP Severity Rating. There is an option to write to a report at the end, it is a
  basic text file that can be used at the end of a threat analysis report.

### STRIDE

- Use this to create a severity rating based on **an already performed** STRIDE threat modeling session. This feature
  is just to provide the rating based on the identified threats. 
- Use -t/--threat-model to perform a STRIDE questionnaire (Walk through a threat model exercise using STRIDE)
  - Automatically writes a report, named \<date\>\_Feature_Name\_STRIDE\_SESSION.txt. 
  - See Examples files for Report Styling

### CVSS

- Use this selection to perform a CVSS rating. It is based on CVSS 3.0 and can have a report written at the end.

## How to use the calculator

- First Usage: python setup_project.py
  - This will create the needed Directories, create a virtual environment, activate the Virtual Environment, and install
    requirements.txt (Currently a blank file, but I have some plans for it)
- Using the calculator:

usage: main.py [-h] [-t] [-s] [-D] [-S] [-C] [-O]

Threat Modeling and Severity Calculator

options:
-h, --help show this help message and exit  
-t, --threat-model Use this to perform a threat model  
-s, --severity Use this to perform a severity rating. Use with -O/--OWASP, -S/--STRIDE, -C/--CVSS, or -D/--DREAD  
-D, --DREAD Use this with -s to perform DREAD Severity Rating  
-S, --STRIDE Use with this -s to perform STRIDE Severity Rating  
-C, --CVSS Use this with -s to perform CVSS Severity Rating  
-O, --OWASP Use this with -s to perform OWASP Severity Rating  

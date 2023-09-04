# Threat Modeling and Severity Calculator

## Threat Models used

- DREAD
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

## Installation
### Basic Installation Instructions
#### Linux/Mac
1. run python setup_project.py. This creates needed directories, a virtual environment, activates the virtual environment, and installs requirements.  
    - Considerations: If you have multiple versions of Python (ie python3 vs python2) make sure to edit setup_project.py to use python3
2. Follow usage instructions in How to use the calculator
#### Windows

1. run python setup_project.py. This creates needed directories, a virtual environment, activates the virtual environment, and installs requirements.  
    - Considerations: Same as Linux. Also, ensure that python is in your path
2. Follow usage instructions in How to use the calculator
## How to use the calculator

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

## Contributing
This project is tracked in Jira. Please follow these steps to ensure proper updates on Jira board. 
1. Each issue will have a ticket related to it. These tickets will be linked in either the ticket Title or the comments depending on who created the issue and when it was created. 
2. Make sure to use the branch that is linked to the ticket when working on contributions. 
3. When committing changes, include the ticket in the commit message, ex. "THREAT-2 Added contributions section to README.md"
4. For Pull Requests, please title the PR as "Ticket Number" "Action" "Issue Number", ex. "THREAT-2 closes #44". This will close the issue and update the ticket with the PR
5. Thank you in advance for contributing <3 


from Severity_Models.severity_models import *
from Threat_Modeling.STRIDE import *
import argparse
import sys


def parse_args():
    descripton = "Threat Modeling and Severity Calculator"
    parser = argparse.ArgumentParser(description=descripton)
    parser.add_argument("-t", "--threat-model", action="store_true",
                        help="Use to perform a threat model")
    parser.add_argument("-s", "--severity",
                        action="store_true",
                        help="Use to perform a severity rating. "
                             "Use with -O/--OWASP, -S/--STRIDE, -C/--CVSS, or -D/--DREAD")
    parser.add_argument("-D", "--DREAD", action="store_true",
                        help="Use with -s to perform DREAD Severity Rating")
    parser.add_argument("-S", "--STRIDE", action="store_true",
                        help="Use with -s to perform STRIDE Severity Rating")
    parser.add_argument("-C", "--CVSS", action="store_true",
                        help="Use with -s to perform CVSS Severity Rating")
    parser.add_argument("-O", "--OWASP", action="store_true",
                        help="Use with -s to perform OWASP Severity Rating")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if args.threat_model:
        feature = Stride()
        feature.write_report()
    if args.severity:
        next_vulnerability = "y"
        while next_vulnerability.lower()[0] == "y":
            if args.DREAD:
                print(DREAD.definition)
                print(DREAD.rating_def)
                vulnerabilty = Dread()
            if args.OWASP:
                print(Owasp.definition)
                print(Owasp.rating_def)
                vulnerabilty = Owasp()
            if args.STRIDE:
                print(Stride_Severity.definition)
                print(Stride_Severity.rating_def)
                vulnerabilty = Stride_Severity()
            if args.CVSS:
                print(Cvss.definition)
                print(Cvss.rating_def)
                vulnerabilty = Cvss()
            else:
                print("Use python main.py -h for help")
                sys.exit()
            next_vulnerability = input(
                "Would you like to Calculate another Vulnerability?")
    else:
        print("Use python main.py -h for help")
        sys.exit()

from Severity_Models.severity_models import *


if __name__ == "__main__":
    model = input("Which model would you like to use?\r\n1. DREAD\r\n2.OWASP\r\n3.STRIDE\r\n4.CVSS\r\n")
    next_vulnerability = "y"
    while next_vulnerability == "y":
        try:
            if int(model) == 1:
                print(Dread.definition)
                print(Dread.rating_def)
                threat = Dread()
            if int(model) == 2:
                print(Owasp.definition)
                print(Owasp.rating_def)
                threat = Owasp()
            if int(model) == 3:
                print(Stride.definition)
                print(Stride.rating_def)
                threat = Stride()
            if int(model) == 4:
                print(Cvss.definition)
                print(Cvss.rating_def)
                threat = Cvss()
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Program failed: {e}")
        print(threat.rating)
        next_vulnerability = input("Would you like to rate another vulnerability? ")[0].lower()
    print("[-] Exiting")

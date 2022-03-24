import os
import sys

path = "./Reports/"

if not os.path.exists(path):
    print("[+] Creating Reports Directory")
    os.mkdir(path)
    print("[+] Creating Reports/Severity_Reports Directory")
    os.mkdir(path + "Severity_Reports")
    print("[+] Creating Reports/Threat_Model_Reports")
    os.mkdir(path + "Threat_Model_Reports")
else:
    print("[-] Report Directory Previously Created")

if not os.path.exists("venv"):
    print("Creating Virtual Environment")
    os.system("python -m venv venv")
else:
    print("[-] Virtual environment previously created")
print("[+] Activating Virtual Environment.")
this_os = input("Is this a\r\n1. Linux\r\n2. Mac\r\n3. Windows \r\nmachine?\r\n")
try:
    if this_os == "1":
        os.system("source venv/bin/activate")
        print("Run deactivate to exit Virtual Environment")
    if this_os == "2":
        os.system("source venv/bin/activate")
        print("Run deactivate to exit Virtual Environment")
    if this_os == "3":
        os.system(".\\venv\\scripts\\activate.bat")
        print("Run venv\\Scripts\\deactivate.bat to exit Virtual Environment")
except Exception as e:
    print(e)

print("[+] Complete. Exiting")

sys.exit()

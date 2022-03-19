import time


class Dread:
    definition = """
Damage potential: How great can the damage be?
Reproducibility: How easy is it to get a potential attack to work?
Exploitability: How much effort and expertise is required to mount an attack?
Affected Users: If the threat were exploited and became an attack, how many users would be affected?
Discoverability: How likely is it to discover the threat? (Should always be assumed to be max score)"""
    rating_def = """
1: Informational
2: Low
3: Medium
4: High
5: Critical"""

    def __init__(self):
        self.rating = self.get_rating()
        self.report = input("Write to report? ")
        if self.report[0].lower() == "y":
            self.write_report()

    def write_report(self):
        with open(f'{time.strftime("%Y-%m-%d")}_threat_report.txt', 'a+') as f:
            payload = f'-----------------------------\r\n' \
                      f'- Vulnerability name: {self.name}\r\n' \
                      f'- Damage Rating: {self.damage}\r\n' \
                      f'- Explanation: {self.damage_explanation}\r\n' \
                      f'- Reproducibility Rating: {self.reproducibility}\r\n' \
                      f'- Explanation: {self.reproducbility_explanation}\r\n' \
                      f'- Exploitability rating: {self.exploitability}\r\n' \
                      f'- Explanation: {self.exploitability_explanation}\r\n' \
                      f'- Affected Users Rating: {self.affectedusers}\r\n' \
                      f'- Explanation: {self.affectedusers_explanation}\r\n' \
                      f'- Discoverabilty Rating: {self.discoverability}\r\n' \
                      f'- Explanation: {self.discoverability_explanation}\r\n' \
                      f'- {self.rating}\r\n' \
                      f'-----------------------------'
            f.write(payload)
        f.close()
        return True

    def get_name(self):
        name = input("What is the name of the vulnerability/finding?\r\n")
        return name

    def get_explanation(self):
        explanation = input("What is the explanation for this rating?\r\n")
        return explanation

    def get_rating(self):
        input("Rating Threat with DREAD Model. Enter 1-5 for severity ratings for the following questions. Press "
              "enter to continue")
        try:
            self.name = self.get_name()
            self.damage = int(input("What is the damage potential? "))
            self.damage_explanation = self.get_explanation()
            self.reproducibility = int(input("What is the reproducibility rating? "))
            self.reproducbility_explanation = self.get_explanation()
            self.exploitability = int(input("What is the exploitability rating? "))
            self.exploitability_explanation = self.get_explanation()
            self.affectedusers = int(input("What is the Affected Users rating? "))
            self.affectedusers_explanation = self.get_explanation()
            self.discoverability = int(input("What is the discoverability rating? (Use 5 if not sure) "))
            self.discoverability_explanation = self.get_explanation()
            rating = (
                                 self.damage + self.reproducibility + self.exploitability + self.affectedusers + self.discoverability) / 5
            if int(round(rating, 0)) == 1:
                return "This threat is rated as: Informational"
            if int(round(rating, 0)) == 2:
                return "This threat is rated as: Low"
            if int(round(rating, 0)) == 3:
                return "This threat is rated as: Medium"
            if int(round(rating, 0)) == 4:
                return "This threat is rated as: High"
            if int(round(rating, 0)) == 5:
                return "This threat is rated as: Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Program failed: {e}")


class Owasp:
    definition = """
Useful for overall impact to both technical and business functions"""
    rating_def = """
1: Informational
2: Low
3: Medium
4: High
5: Critical"""

    def __init__(self):
        self.rating = self.get_rating()

    def get_rating(self):
        input("Rating Threat with OWASP Model. Enter 1-5 for severity ratings for the following questions.")
        try:
            print("Step 1: Threat Agent Factors")
            skill_level = int(input("What is the technical skill level of the threat agents? "))
            motive = int(input("How motivated is the group of threat agents? "))
            opportunity = int(input("What resources and opportunities are required for this group of threat agents? "))
            size = int(input("How large is the group of threat agents? "))
            print("Step 2: Vulnerability Factors")
            discoverability = int(
                input("How easy is it for this group of threat agents to discover this vulnerability? "))
            exploitability = int(input("How easy is it to exploit this vulnerability? "))
            awareness = int(input("How well known is this vulnerability to the threat agents? "))
            detection = int(input("How likely is the exploit to be detected? "))
            likelihood = (
                                 skill_level + motive + opportunity + size + discoverability + exploitability + awareness + detection) / 8
            print("Step 3: Technical Impact Factors")
            confidentiality = int(input("How much data could be disclosed and how sensitive is it? "))
            integrity = int(input("How much data could be corrupted and how damaged is it? "))
            availability = int(input("How much service loss could occur and how vital is it? "))
            accountability = int(input("Are the threat agents actions traceable to an individual? "))
            technical = (confidentiality + availability + integrity + accountability) / 4
            print("Step 4: Business Impact Factors")
            financial = int(input("How much financial damage would result from an exploit? "))
            reputation = int(input("Would an exploit result in reputation damage? "))
            compliance = int(input("How much exposure does non-compliance introduce? "))
            privacy = int(input("How much PII could be disclosed? "))
            bussiness = (financial + reputation + compliance + privacy) / 4
            rating = (likelihood + technical + bussiness) / 3
            if int(round(rating, 0)) == 1:
                return "This threat is rated as: Informational"
            if int(round(rating, 0)) == 2:
                return "This threat is rated as: Low"
            if int(round(rating, 0)) == 3:
                return "This threat is rated as: Medium"
            if int(round(rating, 0)) == 4:
                return "This threat is rated as: High"
            if int(round(rating, 0)) == 5:
                return "This threat is rated as: Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Program failed: {e}")


class Stride:
    definition = """
You must have performed a threat modeling exercise to use this method.
Spoofing: Severity of overall spoofing attacks identified?
Tampering: Severity of overall tampering attacks identified?
Repudiation: Severity of overall repudiation attacks identified?
Information Disclosure: Severity of overall information disclosure identified?
Denial of Service: Severity of overall DoS attacks identified
Escalation of Privileges: Severity of overall escalation of privileges paths identified"""
    rating_def = """
1: Informational
2: Low
3: Medium
4: High
5: Critical"""

    def __init__(self):
        self.rating = self.get_rating()

    def get_rating(self):
        input("Rating Threat with STRIDE Model. Enter 1-5 for severity ratings for the following questions. Press "
              "enter to continue")
        try:
            spoofing = int(input("What is the potential damage if identified spoofing occurs? "))
            tampering = int(input("What is the potential damage if identified tampering occurs? "))
            repudiation = int(input("What is the potential damage if identified repudiation attacks occur? "))
            information = int(input("What is the sensitivity of the information disclosed? "))
            dos = int(input("What is the potential service loss if denial of service occurs? "))
            eop = int(input("What is the risk of elevation of privileges? "))
            rating = (spoofing + tampering + repudiation + information + dos + eop) / 6
            if int(round(rating, 0)) == 1:
                return "This threat is rated as: Informational"
            if int(round(rating, 0)) == 2:
                return "This threat is rated as: Low"
            if int(round(rating, 0)) == 3:
                return "This threat is rated as: Medium"
            if int(round(rating, 0)) == 4:
                return "This threat is rated as: High"
            if int(round(rating, 0)) == 5:
                return "This threat is rated as: Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Program failed: {e}")


class Cvss:
    definition = """
Useful for overall impact to both technical and business functions"""
    rating_def = """
1: Informational
2: Low
3: Medium
4: High
5: Critical"""

    def __init__(self):
        self.base = self.get_rating()
        self.temporal = self.get_temporal()
        self.environmental = self.get_environmental()
        self.rating = f'Base: {self.base}\r\nTemporal: {self.temporal}\r\nEnvironmental: {self.environmental}'

    def get_rating(self):
        input("Rating Threat with CVSS Model. Follow prompts for the following questions. Press "
              "enter to continue")
        try:
            attack_vector = int(input(
                "Enter the attack vector:\r\n1. Physical\r\n2. Local\r\n3. Adjacent Network\r\n4. Network (Internet)\r\n"))
            complexity = int(input("Enter the Attack complexity:\r\n1. High\r\n2. Low\r\n"))
            if complexity == 2:
                complexity == 5
            privs = int(input("Enter the privileges required:\r\n1. High privs\r\n2. Low privs\r\n3. None\r\n"))
            if privs == 3:
                privs = 5
            if privs == 2:
                privs == 3
            user = int(input("Is user action required?\r\n1. Required\r\n2. None\r\n"))
            if user == 2:
                user == 3
            scope = int(input("Is scope changed? \r\n1. Changed\r\n2. Unchanged\r\n"))
            if scope == 2:
                scope == 3
            confidentiality = int(
                input("What is the impact to data confidentialitiy?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if confidentiality == 3:
                confidentiality = 4
            integrity = int(input("What is the impact to data integrity?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if integrity == 3:
                integrity = 5
            availability = int(input("What is the impact to availability?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if availability == 3:
                availability = 5
            rating = (
                             attack_vector + complexity + privs + user + scope + confidentiality + integrity + availability) / 8
            if int(round(rating, 0)) == 1:
                return "Informational"
            if int(round(rating, 0)) == 2:
                return "Low"
            if int(round(rating, 0)) == 3:
                return "Medium"
            if int(round(rating, 0)) == 4:
                return "High"
            if int(round(rating, 0)) == 5:
                return "Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Something went wrong while creating the Base Score: {e}")

    def get_temporal(self):
        print("Getting Temporal Rating")
        base = self.base
        try:
            if base == "Informational":
                base_score = 1
            if base == "Low":
                base_score = 2
            if base == "Medium":
                base_score = 3
            if base == "High":
                base_score = 4
            if base == "Critical":
                base_score = 5
            exploit = int(input(
                "Enter level of exploit code maturity\r\n2. No Exploit\r\n4. Proof of concept\r\n5. Funcitonal Exploit exists\r\n"))
            remediation = int(input(
                "Enter remediation level: \r\n2. Official Fix\r\n3. Temporary Fix\r\n4. Workaround\r\n5. Unavailable\r\n"))
            report = int(input("Enter Report Confidence: \r\n2. Unknown\r\n3. Reasonable\r\n5. Confirmed\r\n"))
            temporal = (exploit + remediation + report) / 3
            rating = (base_score + temporal) / 2
            if int(round(rating, 0)) == 1:
                return "Informational"
            if int(round(rating, 0)) == 2:
                return "Low"
            if int(round(rating, 0)) == 3:
                return "Medium"
            if int(round(rating, 0)) == 4:
                return "High"
            if int(round(rating, 0)) == 5:
                return "Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Something went wrong while creating the Temporal Score: {e}")

    def get_environmental(self):
        print("Getting Environmental Rating")
        try:
            if self.base == "Informational":
                base_score = 1
            if self.base == "Low":
                base_score = 2
            if self.base == "Medium":
                base_score = 3
            if self.base == "High":
                base_score = 4
            if self.base == "Critical":
                base_score = 5
            attack_vector = int(input(
                "Enter the attack vector:\r\n1. Physical\r\n2. Local\r\n3. Adjacent Network\r\n4. Network (Internet)\r\n"))
            complexity = int(input("Enter the Attack complexity:\r\n1. High\r\n2. Low"))
            if complexity == 2:
                complexity == 5
            privs = int(input("Enter the privileges required:\r\n1. High privs\r\n2. Low privs\r\n3. None\r\n"))
            if privs == 3:
                privs = 5
            if privs == 2:
                privs == 3
            user = int(input("Is user action required?\r\n1. Required\r\n2. None\r\n"))
            if user == 2:
                user == 3
            scope = int(input("Is scope changed? \r\n1. Changed\r\n2. Unchanged\r\n"))
            if scope == 2:
                scope == 3
            confidentiality = int(
                input("What is the impact to data confidentialitiy?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if confidentiality == 3:
                confidentiality = 4
            integrity = int(input("What is the impact to data integrity?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if integrity == 3:
                integrity = 5
            availability = int(input("What is the impact to availability?\r\n1. None\r\n2. Low\r\n3. High\r\n"))
            if availability == 3:
                availability = 5
            rating = (
                             attack_vector + complexity + privs + user + scope + confidentiality + integrity + availability) / 8
            if int(round(rating, 0)) == 1:
                return "Informational"
            if int(round(rating, 0)) == 2:
                return "Low"
            if int(round(rating, 0)) == 3:
                return "Medium"
            if int(round(rating, 0)) == 4:
                return "High"
            if int(round(rating, 0)) == 5:
                return "Critical"
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Something went wrong while creating the Environmental Score: {e}")


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

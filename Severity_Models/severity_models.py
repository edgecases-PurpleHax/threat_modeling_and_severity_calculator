import os.path
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
        directory = "Reports/Severity_Reports"
        filename = f'{time.strftime("%Y-%m-%d")}_threat_report_DREAD_method.txt'
        with open(f"{os.path.join(directory, filename)}", "a+") as f:
            payload = (
                f"-----------------------------\r\n"
                f"- Vulnerability name: {self.name}\r\n"
                f"- Damage Rating: {self.damage}\r\n"
                f"- Explanation: {self.damage_explanation}\r\n"
                f"- Reproducibility Rating: {self.reproducibility}\r\n"
                f"- Explanation: {self.reproducbility_explanation}\r\n"
                f"- Exploitability rating: {self.exploitability}\r\n"
                f"- Explanation: {self.exploitability_explanation}\r\n"
                f"- Affected Users Rating: {self.affectedusers}\r\n"
                f"- Explanation: {self.affectedusers_explanation}\r\n"
                f"- Discoverability Rating: {self.discoverability}\r\n"
                f"- Explanation: {self.discoverability_explanation}\r\n"
                f"- {self.rating}\r\n"
                f"-----------------------------"
            )
            f.write(payload)
        f.close()
        return True

    @staticmethod
    def get_name():
        name = input("What is the name of the vulnerability/finding?\r\n")
        return name

    @staticmethod
    def get_explanation():
        explanation = input("What is the explanation for this rating?\r\n")
        return explanation

    def get_rating(self):
        input(
            "Rating Threat with DREAD Model. Enter 1-5 for severity ratings for the following questions. Press "
            "enter to continue"
        )
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
            self.discoverability = int(
                input("What is the discoverability rating? (Use 5 if not sure) ")
            )
            self.discoverability_explanation = self.get_explanation()
            rating = (
                self.damage
                + self.reproducibility
                + self.exploitability
                + self.affectedusers
                + self.discoverability
            ) / 5
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
        self.report = input("Write to report? ")
        if self.report[0].lower() == "y":
            self.write_report()

    @staticmethod
    def get_name():
        name = input("What is the name of the vulnerability/finding?\r\n")
        return name

    @staticmethod
    def get_explanation():
        explanation = input("What is the explanation for this rating?\r\n")
        return explanation

    def write_report(self):
        directory = "Reports/Severity_Reports"
        filename = f'{time.strftime("%Y-%m-%d")}_threat_report_OWASP_method.txt'
        with open(f"{os.path.join(directory, filename)}", "a+") as f:
            payload = (
                f"-----------------------------\r\n"
                f"Vulnerability name: {self.name}\r\n"
                f"Likelihood rating: {self.likelihood}\r\n"
                f"Likelihood factor analysis:\r\n"
                f"    Skill Level: {self.skill_level_explanation}\r\n"
                f"    Motive: {self.motive_explanation}\r\n"
                f"    Opportunity: {self.opportunity_explanation}\r\n"
                f"    Size: {self.size_explanation}\r\n"
                f"    Discoverability: {self.discoverability_explanation}\r\n"
                f"    Exploitability: {self.exploitability_explanation}\r\n"
                f"    Awareness: {self.awareness_explanation}\r\n"
                f"    Detection: {self.detection_explanation}\r\n"
                f"Technical Impact rating: {self.technical}\r\n"
                f"Technical Impact analysis:\r\n"
                f"    Confidentiality: {self.confidentiality_explanation}\r\n"
                f"    Integrity: {self.integrity_explanation}\r\n"
                f"    Availability: {self.availability_explanation}\r\n"
                f"    Accountability: {self.accountability_explanation}\r\n"
                f"    Motive: {self.motive_explanation}\r\n"
                f"    Opportunity: {self.opportunity_explanation}\r\n"
                f"Business Impact rating: {self.business}\r\n"
                f"Business Impact analysis:\r\n"
                f"    Financial: {self.financial_explanation}\r\n"
                f"    Reputation: {self.reputation_explanation}\r\n"
                f"    Compliance: {self.compliance_explanation}\r\n"
                f"    Privacy: {self.privacy_explanation}\r\n"
                f"Overall Rating: {self.rating}\r\n"
                f"-----------------------------"
            )
            f.write(payload)
        f.close()

    def get_rating(self):
        input(
            "Rating Threat with OWASP Model. Enter 1-5 for severity ratings for the following questions."
        )
        try:
            self.name = self.get_name()
            print("Step 1: Threat Agent Factors")
            self.skill_level = int(
                input("What is the technical skill level of the threat agents? ")
            )
            self.skill_level_explanation = self.get_explanation()
            self.motive = int(input("How motivated is the group of threat agents? "))
            self.motive_explanation = self.get_explanation()
            self.opportunity = int(
                input(
                    "What resources and opportunities are required for this group of threat agents? "
                )
            )
            self.opportunity_explanation = self.get_explanation()
            self.size = int(input("How large is the group of threat agents? "))
            self.size_explanation = self.get_explanation()
            print("Step 2: Vulnerability Factors")
            self.discoverability = int(
                input(
                    "How easy is it for this group of threat agents to discover this vulnerability? "
                )
            )
            self.discoverability_explanation = self.get_explanation()
            self.exploitability = int(
                input("How easy is it to exploit this vulnerability? ")
            )
            self.exploitability_explanation = self.get_explanation()
            self.awareness = int(
                input("How well known is this vulnerability to the threat agents? ")
            )
            self.awareness_explanation = self.get_explanation()
            self.detection = int(input("How likely is the exploit to be detected? "))
            self.detection_explanation = self.get_explanation()
            self.likelihood = (
                self.skill_level
                + self.motive
                + self.opportunity
                + self.size
                + self.discoverability
                + self.exploitability
                + self.awareness
                + self.detection
            ) / 8
            print("Step 3: Technical Impact Factors")
            self.confidentiality = int(
                input("How much data could be disclosed and how sensitive is it? ")
            )
            self.confidentiality_explanation = self.get_explanation()
            self.integrity = int(
                input("How much data could be corrupted and how damaged is it? ")
            )
            self.integrity_explanation = self.get_explanation()
            self.availability = int(
                input("How much service loss could occur and how vital is it? ")
            )
            self.availability_explanation = self.get_explanation()
            self.accountability = int(
                input("Are the threat agents actions traceable to an individual? ")
            )
            self.accountability_explanation = self.get_explanation()
            self.technical = (
                self.confidentiality
                + self.availability
                + self.integrity
                + self.accountability
            ) / 4
            print("Step 4: Business Impact Factors")
            self.financial = int(
                input("How much financial damage would result from an exploit? ")
            )
            self.financial_explanation = self.get_explanation()
            self.reputation = int(
                input("Would an exploit result in reputation damage? ")
            )
            self.reputation_explanation = self.get_explanation()
            self.compliance = int(
                input("How much exposure does non-compliance introduce? ")
            )
            self.compliance_explanation = self.get_explanation()
            self.privacy = int(input("How much PII could be disclosed? "))
            self.privacy_explanation = self.get_explanation()
            self.business = (
                self.financial + self.reputation + self.compliance + self.privacy
            ) / 4
            rating = (self.likelihood + self.technical + self.business) / 3
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


class Stride_Severity:
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
        self.report = input("Write to report? ")
        if self.report[0].lower() == "y":
            self.write_report()

    @staticmethod
    def get_name():
        name = input("What is the name of the vulnerability/finding?\r\n")
        return name

    @staticmethod
    def get_explanation():
        explanation = input("What is the explanation for this rating?\r\n")
        return explanation

    def write_report(self):
        directory = "Reports/Severity_Reports"
        filename = (
            f'{time.strftime("%Y-%m-%d")}_threat_report_STRIDE_SEVERITY_method.txt'
        )
        with open(f"{os.path.join(directory, filename)}", "a+") as f:
            payload = (
                f"-----------------------------\r\n"
                f"Vulnerability name: {self.name}\r\n"
                f"Spoofing Rating: {self.spoofing}\r\n"
                f"Spoofing Analysis: {self.spoofing_explanation}\r\n"
                f"Tampering Rating: {self.tampering}"
                f"Tampering Analysis: {self.tampering_explanation}\r\n"
                f"Repudiation Rating: {self.repudiation}\r\n"
                f"Repudiation Analysis: {self.repudiation_explanation}\r\n"
                f"Information Disclosure Rating: {self.information}\r\n"
                f"Information Disclosure Analysis: {self.information_explanation}\r\n"
                f"Denial of Service Rating: {self.dos}\r\n"
                f"Denial of Service Analysis: {self.dos_explanation}\r\n"
                f"Escalation of Privileges Rating: {self.eop}\r\n"
                f"Escalation of Privileges Analysis: {self.eop_explanation}\r\n"
                f"Overall Rating: {self.rating}\r\n"
                f"-----------------------------"
            )
            f.write(payload)
        f.close()

    def get_rating(self):
        input(
            "Rating Threat with STRIDE Model. Enter 1-5 for severity ratings for the following questions. Press "
            "enter to continue"
        )
        self.name = self.get_name()
        try:
            self.spoofing = int(
                input("What is the potential damage if identified spoofing occurs? ")
            )
            self.spoofing_explanation = self.get_explanation()
            self.tampering = int(
                input("What is the potential damage if identified tampering occurs? ")
            )
            self.tampering_explanation = self.get_explanation()
            self.repudiation = int(
                input(
                    "What is the potential damage if identified repudiation attacks occur? "
                )
            )
            self.repudiation_explanation = self.get_explanation()
            self.information = int(
                input("What is the sensitivity of the information disclosed? ")
            )
            self.information_explanation = self.get_explanation()
            self.dos = int(
                input(
                    "What is the potential service loss if denial of service occurs? "
                )
            )
            self.dos_explanation = self.get_explanation()
            self.eop = int(input("What is the risk of elevation of privileges? "))
            self.eop_explanation = self.get_explanation()
            rating = (
                self.spoofing
                + self.tampering
                + self.repudiation
                + self.information
                + self.dos
                + self.eop
            ) / 6
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
    mapping = {
        "attack vector": {
            1: "Physical",
            2: "Local",
            3: "Adjacent Network",
            4: "Network (Internet)",
        },
        "complexity": {1: "High", 2: "Low"},
        "privileges": {
            1: "High Level of Privileges",
            2: "Low Level of Privileges",
            3: "No privileges required",
        },
        "user": {1: "User Action Required", 2: "No User Action Required"},
        "scope": {1: "Changed", 2: "Unchanged"},
        "confidentiality": {
            1: "None",
            2: "Low",
            3: "High",
        },
        "integrity": {1: "None", 2: "Low", 3: "High"},
        "availability": {1: "None", 2: "Low", 3: "High"},
        "exploit": {
            2: "No Exploit",
            4: "Proof of concept",
            5: "Funcitonal Exploit exists",
        },
        "remediation": {
            2: "Official Fix",
            3: "Temporary Fix",
            4: "Workaround",
            5: "Unavailable",
        },
        "report confidence": {2: "Unknown", 3: "Reasonable", 5: "Confirmed"},
    }

    def __init__(self):
        self.base = self.get_rating()
        self.temporal = self.get_temporal()
        self.environmental = self.get_environmental()
        self.rating = f"Base: {self.base}\r\nTemporal: {self.temporal}\r\nEnvironmental: {self.environmental}"
        self.report = input("Write to report? ")
        if self.report[0].lower() == "y":
            self.write_report()

    @staticmethod
    def get_name():
        name = input("What is the name of the vulnerability/finding?\r\n")
        return name

    @staticmethod
    def get_explanation():
        explanation = input("What is the explanation for this rating?\r\n")
        return explanation

    def write_report(self):
        directory = "Reports/Severity_Reports"
        filename = f'{time.strftime("%Y-%m-%d")}_threat_report_CVSS_method.txt'
        with open(f"{os.path.join(directory, filename)}", "a+") as f:
            payload = (
                f"-----------------------------\r\n"
                f"Vulnerability name: {self.name}\r\n"
                f"Base Rating: {self.base}\r\n"
                f"    Attack Vector: {self.attack_vector}\r\n"
                f"    Complexity: {self.complexity}\r\n"
                f"    Required Privileges: {self.privs}\r\n"
                f"    Required User Interaction: {self.user}\r\n"
                f"    Scope Modification: {self.scope}\r\n"
                f"    Impact to Confidentiality: {self.confidentiality}\r\n"
                f"    Impact to Integrity: {self.integrity}\r\n"
                f"    Impact to Availability: {self.availability}\r\n"
                f"Temporal Rating: {self.temporal}\r\n"
                f"    Exploit Modifier: {self.exploit}\r\n"
                f"    Available Remediation Modifier: {self.remediation}\r\n"
                f"    Report Confidence Modifier: {self.report_confidence}\r\n"
                f"    Report Confidence Analysis: {self.report_confidence_analysis}\r\n"
                f"Environmental Rating (Base score modified by Environment): {self.environmental}\r\n"
                f"    Attack Vector: {self.attack_vector_env}\r\n"
                f"    Complexity: {self.complexity_env}\r\n"
                f"    Required Privileges: {self.privs_env}\r\n"
                f"    Required User Interaction: {self.user_env}\r\n"
                f"    Scope Modification: {self.scope_env}\r\n"
                f"    Impact to Confidentiality: {self.confidentiality_env}\r\n"
                f"    Impact to Integrity: {self.integrity_env}\r\n"
                f"    Impact to Availability: {self.availability_env}\r\n"
                f"-----------------------------"
            )
            f.write(payload)
        f.close()

    def get_rating(self):
        input(
            "Rating Threat with CVSS Model. Follow prompts for the following questions. Press "
            "enter to continue"
        )
        try:
            mapping = self.mapping
            self.name = self.get_name()
            attack_vector = int(
                input(
                    "Enter the attack vector:\r\n1. Physical\r\n2. Local\r\n3. Adjacent Network\r\n"
                    "4. Network (Internet)\r\n"
                )
            )
            self.attack_vector = mapping["attack vector"][attack_vector]
            complexity = int(
                input("Enter the Attack complexity:\r\n1. High\r\n2. Low\r\n")
            )
            self.complexity = mapping["complexity"][complexity]
            if complexity == 2:
                complexity == 5
            privs = int(
                input(
                    "Enter the privileges required:\r\n1. High privs\r\n2. Low privs\r\n3. None\r\n"
                )
            )
            self.privs = mapping["privileges"][privs]
            if privs == 3:
                privs = 5
            if privs == 2:
                privs == 3
            user = int(input("Is user action required?\r\n1. Required\r\n2. None\r\n"))
            self.user = mapping["user"][user]
            if user == 2:
                user == 3
            scope = int(input("Is scope changed? \r\n1. Changed\r\n2. Unchanged\r\n"))
            self.scope = mapping["scope"][scope]
            if scope == 2:
                scope == 3
            confidentiality = int(
                input(
                    "What is the impact to data confidentiality?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.confidentiality = mapping["confidentiality"][confidentiality]
            if confidentiality == 3:
                confidentiality = 4
            integrity = int(
                input(
                    "What is the impact to data integrity?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.integrity = mapping["integrity"][integrity]
            if integrity == 3:
                integrity = 5
            availability = int(
                input(
                    "What is the impact to availability?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.availability = mapping["availability"][availability]
            if availability == 3:
                availability = 5
            rating = (
                attack_vector
                + complexity
                + privs
                + user
                + scope
                + confidentiality
                + integrity
                + availability
            ) / 8
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
        mapping = self.mapping
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
            exploit = int(
                input(
                    "Enter level of exploit code maturity\r\n"
                    "2. No Exploit\r\n"
                    "4. Proof of concept\r\n"
                    "5. Funcitonal Exploit exists\r\n"
                )
            )
            self.exploit = mapping["exploit"][exploit]
            remediation = int(
                input(
                    "Enter remediation level: \r\n"
                    "2. Official Fix\r\n"
                    "3. Temporary Fix\r\n"
                    "4. Workaround\r\n"
                    "5. Unavailable\r\n"
                )
            )
            self.remediation = mapping["remediation"][remediation]

            report = int(
                input(
                    "Enter Report Confidence: \r\n2. Unknown\r\n3. Reasonable\r\n5. Confirmed\r\n"
                )
            )
            self.report_confidence = mapping["report confidence"][report]
            self.report_confidence_analysis = self.get_explanation()
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
            mapping = self.mapping
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
            attack_vector = int(
                input(
                    "Enter the attack vector:\r\n1. Physical\r\n2. Local\r\n3. Adjacent Network\r\n"
                    "4. Network (Internet)\r\n"
                )
            )
            self.attack_vector_env = mapping["attack vector"][attack_vector]
            complexity = int(
                input("Enter the Attack complexity:\r\n1. High\r\n2. Low\r\n")
            )
            self.complexity_env = mapping["complexity"][complexity]
            if complexity == 2:
                complexity == 5
            privs = int(
                input(
                    "Enter the privileges required:\r\n1. High privs\r\n2. Low privs\r\n3. None\r\n"
                )
            )
            self.privs_env = mapping["privileges"][privs]
            if privs == 3:
                privs = 5
            if privs == 2:
                privs == 3
            user = int(input("Is user action required?\r\n1. Required\r\n2. None\r\n"))
            self.user_env = mapping["user"][user]
            if user == 2:
                user == 3
            scope = int(input("Is scope changed? \r\n1. Changed\r\n2. Unchanged\r\n"))
            self.scope_env = mapping["scope"][scope]
            if scope == 2:
                scope == 3
            confidentiality = int(
                input(
                    "What is the impact to data confidentiality?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.confidentiality_env = mapping["confidentiality"][confidentiality]
            if confidentiality == 3:
                confidentiality = 4
            integrity = int(
                input(
                    "What is the impact to data integrity?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.integrity_env = mapping["integrity"][integrity]
            if integrity == 3:
                integrity = 5
            availability = int(
                input(
                    "What is the impact to availability?\r\n1. None\r\n2. Low\r\n3. High\r\n"
                )
            )
            self.availability_env = mapping["availability"][availability]
            if availability == 3:
                availability = 5
            rating = (
                attack_vector
                + complexity
                + privs
                + user
                + scope
                + confidentiality
                + integrity
                + availability
            ) / 8
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

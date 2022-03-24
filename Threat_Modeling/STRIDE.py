import os
import time


class Stride:

    def __init__(self):
        self.feature_name = input("What feature are you threat modeling?\r\n")
        self.spoofing = self.spoofing_questions()
        self.tampering = self.tampering_questions()
        self.repudiation = self.repudiation_questions()
        self.info_disclosure = self.info_disclosure_questions()
        self.denial = self.denial_of_service_questions()
        self.esc_of_privs = self.esc_of_privs_questions()

    @staticmethod
    def spoofing_questions():
        spoofing = {"IP": {}, "ARP": {}, "DNS": {}}
        ip_spoofing_next = "y"
        dns_spoofing_next = "y"
        arp_spoofing_next = "y"
        print("IP Spoofing\r\n")
        while ip_spoofing_next.lower()[0] != "n":
            ip_spoofing_question = input(
                "What opportunities are there to spoof IP addresses?\r\n")
            ip_spoofing_explanation = input(
                "Describe how this spoofing threat would be accomplished: \r\n"
            )
            spoofing["IP"][ip_spoofing_question] = ip_spoofing_explanation
            ip_spoofing_next = input(
                "Would you like to enter another IP spoofing threat?\r\n")
        while dns_spoofing_next.lower()[0] != "n":
            dns_spoofing_question = input(
                "What opportunities are there to spoof DNS?\r\n")
            dns_spoofing_explanation = input(
                "Describe how this spoofing threat would be accomplished: \r\n"
            )
            spoofing["DNS"][dns_spoofing_question] = dns_spoofing_explanation
            dns_spoofing_next = input(
                "Would you like to enter another DNS spoofing threat?\r\n")
        while arp_spoofing_next.lower()[0] != "n":
            arp_spoofing_question = input(
                "What opportunities are there to spoof ARP?\r\n")
            arp_spoofing_explanation = input(
                "Describe how this spoofing threat would be accomplished: \r\n"
            )
            spoofing["ARP"][arp_spoofing_question] = arp_spoofing_explanation
            arp_spoofing_next = input(
                "Would you like to enter another ARP spoofing threat?\r\n")
        return spoofing

    @staticmethod
    def tampering_questions():
        tampering = {"Token": {}, "Request": {}}
        token_next = "y"
        request_next = "y"
        while token_next.lower()[0] != "n":
            token_question = input(
                "What opportunities are there to tamper with tokens?\r\n")
            token_explanation = input(
                "Describe how this tampering threat would be accomplished:\r\n"
            )
            tampering["Token"][token_question] = token_explanation
            token_next = input(
                "Would you like to enter another Token Tampering Threat?\r\n")
        while request_next.lower()[0] != "n":
            request_question = input(
                "What opportunities are there to tamper with requests?\r\n")
            request_explanation = input(
                "Describe how this tampering threat would be accomplished:\r\n"
            )
            tampering["Request"][request_question] = request_explanation
            request_next = input(
                "Would you like to enter another Request Tampering Threat?\r\n"
            )
        return tampering

    @staticmethod
    def repudiation_questions():
        repudiation = {"Logging": {}}
        logging_next = "y"
        while logging_next.lower()[0] != "n":
            logging_question = input("Define Repudiation threat: \r\n")
            logging_explanation = input(
                "Describe how this repudiation threat would be accomplished: \r\n"
            )
            repudiation["Logging"][logging_question] = logging_explanation
            logging_next = input(
                "Would you like to enter another Repudiation threat?\r\n")
        return repudiation

    @staticmethod
    def info_disclosure_questions():
        information_disclosure = {
            "Sensitive_Docs": {},
            "Application_Info": {},
            "Backend_Service_Disclosure": {},
        }
        sens_docs_next = "y"
        app_info_next = "y"
        backend_info_next = "y"
        while sens_docs_next.lower()[0] != "n":
            sens_docs_question = input(
                "Are there any Sensitive Documents (Enter each Document? \r\n")
            sens_docs_explanation = input(
                "Describe how these Documents could be exposed: \r\n")
            information_disclosure["Sensitive_Docs"][
                sens_docs_question] = sens_docs_explanation
            sens_docs_next = input(
                "Would you like to enter another Sensitive Document?\r\n")
        while app_info_next.lower()[0] != "n":
            app_info_question = input(
                "Is there any Sensitive Application information? (Such as Version, etc): \r\n"
            )
            app_info_explanation = input(
                "Describe how this information could be used maliciously: \r\n"
            )
            information_disclosure["Application_Info"][
                app_info_question] = app_info_explanation
            app_info_next = input(
                "Would you like to enter more Application Information?\r\n")
        while backend_info_next.lower()[0] != "n":
            backend_question = input(
                "Is there any Sensitive Backend information? (Such as Version, etc) \r\n"
            )
            backend_explanation = input(
                "Describe how this information could be used maliciously: \r\n"
            )
            information_disclosure["Backend_Service_Disclosure"][
                backend_question] = backend_explanation
            backend_info_next = input(
                "Would you like to enter more Backend Information?\r\n")
        return information_disclosure

    @staticmethod
    def denial_of_service_questions():
        dos = {"System_DOS": {}, "User_DOS": {}, "Network_DOS": {}}
        system_dos_next = "y"
        user_dos_next = "y"
        network_dos_next = "y"
        while system_dos_next.lower()[0] != "n":
            system_dos_question = input(
                "How can an attacker deny service to the System? (Application, etc)? \r\n"
            )
            system_dos_explanation = input(
                "How would this be accomplished? \r\n")
            dos["System_DOS"][system_dos_question] = system_dos_explanation
            system_dos_next = input(
                "Would you like to enter more another System DoS?\r\n")
        while user_dos_next.lower()[0] != "n":
            user_dos_question = input(
                "How can an attacker deny service to the User? (Application, etc)? \r\n"
            )
            user_dos_explanation = input(
                "How would this be accomplished? \r\n")
            dos["User_DOS"][user_dos_question] = user_dos_explanation
            user_dos_next = input(
                "Would you like to enter another User DoS?\r\n")
        while network_dos_next.lower()[0] != "n":
            network_dos_question = input(
                "How can an attacker deny service to the Network? (Application, etc)? \r\n"
            )
            network_dos_explanation = input(
                "How would this be accomplished? \r\n")
            dos["Network_DOS"][network_dos_question] = network_dos_explanation
            network_dos_next = input(
                "Would you like to enter another Network DoS?\r\n")
        return dos

    @staticmethod
    def esc_of_privs_questions():
        eop = {"Application_Privs": {}, "Backend_Privs": {}}
        app_pr_next = "y"
        backend_pr_next = "y"
        while app_pr_next.lower()[0] != "n":
            app_pr_question = input(
                "How can an attacker Escalate Application Privileges (Laterally, etc)? \r\n"
            )
            app_pr_explanation = input("How would this be accomplished? \r\n")
            eop["Application_Privs"][app_pr_question] = app_pr_explanation
            app_pr_next = input(
                "Would you like to enter another Application Escalation of Privileges?\r\n"
            )
        while backend_pr_next.lower()[0] != "n":
            backend_pr_question = input(
                "How can an attacker Escalate Backend Privileges? (Laterally, etc)? \r\n"
            )
            backend_pr_explanation = input(
                "How would this be accomplished? \r\n")
            eop["Backend_Privs"][backend_pr_question] = backend_pr_explanation
            backend_pr_next = input(
                "Would you like to enter another Backend Escalation of Privileges?\r\n"
            )
        return eop

    def write_report(self):
        directory = "Reports/Threat_Model_Reports"
        filename = f'{time.strftime("%Y-%m-%d")}_{self.feature_name.replace(" ", "_")}_STRIDE_Report.txt'
        with open(f"{os.path.join(directory, filename)}", "a+") as f:
            f.writelines(f"{self.feature_name} STRIDE Report\r\n")
            f.writelines(f"Spoofing: \r\n")
            for i in self.spoofing.keys():
                for threat in self.spoofing[i].keys():
                    f.writelines(
                        f"     Threat: {threat}\r\n     Description: {self.spoofing[i][threat]}\r\n"
                    )
            f.writelines("Tampering: \r\n")
            for i in self.tampering.keys():
                for threat in self.tampering[i].keys():
                    f.writelines(
                        f"     Threat: {threat}\r\n     Description: {self.tampering[i][threat]}\r\n"
                    )
            f.writelines("Repudiation: \r\n")
            for i in self.repudiation.keys():
                for threat in self.repudiation[i].keys():
                    f.writelines(
                        f"     Threat: {threat}\r\n     Description: {self.repudiation[i][threat]}\r\n"
                    )
            f.writelines("Information Disclosure: \r\n")
            for i in self.info_disclosure.keys():
                for threat in self.info_disclosure[i].keys():
                    f.writelines(
                        f"     "
                        f"Threat: Disclosure of {threat}\r\n     Description: {self.info_disclosure[i][threat]}\r\n"
                    )
            f.writelines("Denial of Service:\r\n")
            for i in self.denial.keys():
                for threat in self.denial[i].keys():
                    f.writelines(
                        f"Threat: Disclosure of {threat}\r\n     Description: {self.denial[i][threat]}\r\n"
                    )
            f.writelines("Elevation of Privileges:\r\n")
            for i in self.esc_of_privs.keys():
                for threat in self.esc_of_privs[i].keys():
                    f.writelines(
                        f"Threat: {threat}\r\n     Description: {self.esc_of_privs[i][threat]}\r\n"
                    )


if __name__ == "__main__":
    test = Stride()
    test.write_report()

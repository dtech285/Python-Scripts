import os, sys
from investigate import launch_web, validate_ip
from port import validate_port
from hash import validate_hash
from url_inv import validate_url


class Menu:

    '''Display a menu and respond to choices when run.'''
    def __init__(self):

        self.choices = {
            "1": self.ip_address,
            "2": self.file_hash,
            "3": self.port_number,
            "4": self.request_url,
            "5": self.inv_domain,
            "6": self.whois,
            "7": self.quit
            }

    def display_menu(self):
        os.system('cls')
        print("""
        INVESTIGATION MENU

            1. IP Address
            2. File Hash
            3. Port Number
            4. URL
            5. domain
            6. Whois
            7. Quit
        """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("\n\tEnter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def ip_address(self):
        IpAddr = input("\n\tEnter an IP Address: ")
        validate_ip(IpAddr)

    def file_hash(self):
        file_hash = input("\n\tEnter a file hash: ")
        validate_hash(file_hash)

    def port_number(self):
        PortNumber = input("\n\tEnter a port number: ")
        validate_port(PortNumber)

    def request_url(self):
        RequestURL = input("\n\tEnter request URL: ")
        validate_url(RequestURL)

    def inv_domain(self):
        domain = input("\n\tEnter Domain: ")
        # validate_domain()

    def whois(self):
        whois = input("\n\tEnter Address or Domain: ")
        # validate input
        # call function

    def quit(self):
        #print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()

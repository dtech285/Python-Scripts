# Severity dictionary
import sys, argparse
from HealthSouthCalc import severity_calc
import re

# Global variables
email_criticality = []
email_dict = {}
dcs5 = ""
criticality = {}

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hv', help='hash value') # not used
    parser.add_argument('-a', help='IP address') # not used
    parser.add_argument('-p', help='Port Number')
    parser.add_argument('-f', help='Flex String 1')
    parser.add_argument('-d', help='Device Custom String 5')

    args = parser.parse_args()

    return args

def format_output(email_criticality):
    """ takes the list and converts to a dictionary
    to format the output"""
    global email_dict
    global criticality
    for x in email_criticality:
        x = str(x)
        x = x.strip()
        x = x.split(":")
        email_dict[x[0]] = x[1]

    # Print the criticality section
    for k, v in email_dict.items():
        print(k + "\t\t" + v)

    if "True" in criticality.values():
        print("==========================================================")
        try:
            print(dcs5[1])
        except IndexError as e:
            print("No critcal values listed in the logs")
            print("This occurs in older use cases where the critical value is not included in Device Custom String 5.")
    print("==========================================================")
    print(" Analysts: Manually add IMPACT value to Incident Rating if any of the below are 'True'")
    print("==========================================================")
    print(" Impacts > 100 users - \tADD 3 to Incident Rating")
    print(" Single user with '_a' or '_da' account - \tADD 3 to Incident Rating")
    print("==========================================================")


def regex_check(regex, device_custom_string5):

    if re.search(regex, device_custom_string5):
        match = re.search(regex, device_custom_string5)

        return match.group(0)

def criticality_calc(device_custom_string5):
    global email_criticality
    global dcs5
    global criticality
    #print(device_custom_string5) # FOR TESTING REMOVE
    dcs5 = device_custom_string5.split("Critical Values if any true:")

    #criticality = {}
    regex_dict = {'privileged_regex': 'Privileged User: .*(True|False).*',
                'data_center_regex': 'Data Center IP Check: .*(True|False).*',
                'public_asset_regex': 'Public Asset Check:  .*(True|False).*',
                'critical_asset_regex': 'Critical Asset Check: .*(True|False).*',
            }

    for key, regex in regex_dict.items():

        get_crit = regex_check(regex, device_custom_string5) # store regex reslult
        email_criticality.append(get_crit) # add the result to list
        crit_key = get_crit.split(":")
        value  = crit_key[1].split("-")
        crit_key = str(crit_key[0])
        value = str(value[0])
        value = value.strip()
        criticality[crit_key] = value # store the key, value in dictionary

    if criticality['Privileged User'] == "True":
        privileged_use = 6
    else:
        privileged_user = 0

    if criticality['Data Center IP Check'] == "True":
        data_center = 7
    else:
        data_center = 0

    if criticality['Public Asset Check'] == "True":
        public_asset = 8
    else:
        public_asset = 0

    if criticality['Critical Asset Check'] == "True":
        critical_asset = 10
    else:
        critical_asset = 0

    # add all criticality categories to get the criticality value
    criticality_value = privileged_user + data_center + public_asset + critical_asset

    if criticality_value == 0:

        criticality_value = criticality_value + 5

    return criticality_value


def main():
    severity = 0
    criticality = 0
    impact = 0
    # for email
    global email_dict
    global email_criticality

    parameters = get_parser()
    device_custom_string5 = parameters.d

    # Form the use_case string
    use_case = parameters.f
    use_case = use_case.split("--")

    del use_case[0]
    use_case = str(use_case)
    use_case = use_case.strip()
    use_case = use_case.replace('[', "")
    use_case = use_case.replace(']', "")
    use_case = use_case.replace('\'', "")
    use_case = use_case.strip()

    severity = severity_calc(use_case)
    # test severity_calc
    if severity == None:
        print("==========================================================")
        print("Analysts: The use case was not found. The Incident Rating must be calculated manually")
        print("1. Calculate the severity value using the runbook")
        print("2. Add the severity value to the 'INCIDENT RATING' below")
        print("==========================================================")
        severity = 0

    # calculate the criticality value
    criticality_value = criticality_calc(device_custom_string5)
    incident_rating = severity + criticality_value + impact

    print("INCIDENT RATING = {}".format(incident_rating))

    # Reorder the list
    email_criticality[0], email_criticality[1], email_criticality[3] = email_criticality[1], email_criticality[3], email_criticality[0]

    # print criticality check
    format_output(email_criticality)


if __name__== '__main__':
    main()

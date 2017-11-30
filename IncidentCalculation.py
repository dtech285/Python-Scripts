#!/usr/bin/env python3

# Incident Rating = Severity + Criticality + Impact
#Severity = ("Anonymous Logon from the internet": "7", "Bluecoat - Botnet Activity Detected": "5",
#    "Bluecoat - Botnet Outbreak Detected": "5")


#def CalculateSeverity():


def CalculateCriticality(PrivilegedUser, DataCenterIPCheck, PublicAssetCheck, CriticalAssetCheck):

    print("PrivilegedUser = ", PrivilegedUser.upper())
    print("DataCenterIPCheck = ", DataCenterIPCheck.upper())
    print("PublicAssetCheck = ", PublicAssetCheck.upper())
    print("CriticalAssetCheck = ", CriticalAssetCheck.upper())

    if PrivilegedUser.upper() == "Y":
        PrivilegedUserValue = 6
    else:
        PrivilegedUserValue = 0

    if DataCenterIPCheck.upper() == "Y":
        DataCenterIPCheckValue = 7
    else:
        DataCenterIPCheckValue = 0

    if PublicAssetCheck.upper() == "Y":
        PublicAssetCheckValue = 8
    else:
        PublicAssetCheckValue = 0

    if CriticalAssetCheck.upper() == "Y":
        CriticalAssetCheckValue = 10
    else:
        CriticalAssetCheckValue = 0

    Criticality = PrivilegedUserValue + DataCenterIPCheckValue + PublicAssetCheckValue + CriticalAssetCheckValue

    return Criticality


#def CalculateImpact():


#def CalculateIncidentRating():



def main():

# Get use case input
# Get

    print("==============================================")
    print("=    HEALTHSOUTH INCIDENT RATING CALCULATOR  =")
    print("==============================================\n\n\n")

    print("Calculate Criticalitiy\n")

    PrivilegedUser = input("Privileged User: Y/N: ")
    DataCenterIPCheck = input("Data Center IP Check: Y/N: ")
    PublicAssetCheck = input("Public Asset Check: Y/N: ")
    CriticalAssetCheck = input("Critical Asset Check: Y/N: ")

    Criticality = CalculateCriticality(PrivilegedUser, DataCenterIPCheck, PublicAssetCheck, CriticalAssetCheck)

    print(Criticality)

    print("\n\nCalculate Severity\n\n")



if __name__== '__main__':
    main()

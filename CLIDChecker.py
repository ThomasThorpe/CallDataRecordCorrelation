#Categorise Numbers into real or not
import  datetime, csv
from AreaCodes import AreaCodes
#AreaCodes is a dictionary of AreaCodes to Geographical location

#Geographic Area Codes
#Can be lengths 3,4,5,6
def CheckCLID(CLID):
    if (CLID[:2] in ["01","02"]) and (len(CLID) == 10 or len(CLID) ==  11):
        #Geographical Numbers
        if CLID[:6] in AreaCodes:
            return True
        elif CLID[:5] in AreaCodes:
            return True
        elif CLID[:4] in AreaCodes:
            if CLID[:4] in ["0113","0114","0115","0116","0117","0118","0121","0131","0141","0151","0161"]:
                for i in range (4960000,4961000):
                    if CLID[4:] == str(i):
                        #Fictious Number Range
                        return False
            if CLID[:4] == "0191":
                for i in range(4980000,4981000):
                    if CLID[4:] == str(i):
                        #Fictious Number Range
                        return False
            return True
        elif CLID[:3] in AreaCodes:
            if CLID[:3] == "020":
                for i in range(79460000,79461000):
                    if CLID[3:] == str(i):
                        #Fictious Number Range
                        return False
            if CLID[:3] == "028":
                for i in range(96496000,96497000):
                    if CLID[3:] == str(i):
                        #Fictious Number Range
                        return False
            if CLID[:3] == "029":
                for i in range(20180000,20181000):
                    if CLID[3:] == str(i):
                        #Fictious Number Range
                        return False
            return True
        else:
            return False
    if len(CLID) == 11:
        if CLID[:3] == "030":
            for i in range(69990000,69991000):
                if CLID[3:] == str(i):
                    #Fictious Number Range for UK-Wide
                    return False
            #Non-Geographic Number: Public sector and not-for-profit bodies
            return False
        if CLID[:3] == "033":
            #Non-Geographic Number
            return True
        if CLID[:3] == "034":
            #Non-Geographic Number: migrating numbers from 084 numbers
            return True
        if CLID[:3] == "037":
            #Non-Geographic Number: migrating numbers from 087 numbers
            return True
    if len(CLID) == 10 or len(CLID) == 11:
        if CLID[:3] == "055":
            #Corporate Number
            return True
        if CLID[:3] == "056":
            #Location Independent Electronic Communications Service
            return False
    if len(CLID) == 11:
        if CLID[:3] == "070":
            #Personal Number
            return False
        if CLID[:3] == "076":
            if CLID[:5] == "07624":
                #Radiopaging Service (Isle of Man)
                return False
            else:
                #Radiopaging Service
                return False
        if ((CLID[:2] == "07") and (CLID[2] in ["1","2","3","4","5","7","8","9"])):
            for i in range(700900000,700901000):
                if CLID[2:] == str(i):
                    #Fictious Number Range
                    return False
            #Mobile Services
            return True
    if len(CLID) == 10 and CLID[:4] == "0800":
        #Non-Geographic Number that is no longer available for allocation
        return False
    if len(CLID) == 11:
        if CLID[:3] == "080":
            for i in range(81570000,81571000):
                if CLID[3:] == str(i):
                    #Ficitious Number Range for freephone
                    return False
            #Non-Geographic Number (Free to caller)
            return True
        if CLID[:3] == "082":
            #Non-Geographic Number (Internet for schools)
            return False
        if CLID[:4] in ["0843","0844","0845"]:
            #Non-Geographic Number
            return True
        if CLID[:4] in ["0870","0871","0872","0873"]:
            #Non-Geographic Number
            return True
        if CLID[:3] in ["090","091"]:
            if CLID[:4] in ["0908","0909"]:
                for i in range(8790000,8791000):
                    if CLID[4:] == str(i):
                        #Ficitious Number Range for premium rate services
                        return False
                #Sexual Entertainment Services no longer available for allocation
                return False
            else:
                #Non-Geographical Number
                return True
        if CLID[:3] == "098":
            #Sexual Entertainment Services
            return False
    if ((CLID in ["116000","116006","116111","116117","116123"]) or (len(CLID)==6 and CLID[:3] == "118")):
        #Type B Access Codes
        return False
    if len(CLID) == 5:
        for i in range(124,141):
            if CLID[:3] == str(i):
                #Type B Access Codes
                return False
        if CLID[:3] in ["143","144","145","146","148","149"]:
            #Type B Access Codes
            return False
        for i in range(160,170):
            if CLID[:3] == str(i):
                #Type B Access Codes
                return False
        for i in range(181,190):
            if CLID[:3] == str(i):
                #Type B Access Codes
                return False
    if len(CLID) < 11:
        try:
            if CLID[0] in ["2","3","4","5","6","7","8","9"]:
                #Telex Service Number
                return False
        except IndexError:
            #Nothing
            return False
    if len(CLID) == 6:
        for i in range(504000,504800):
            if CLID == str(i):
                #Non-Geographic Number Portability Codes
                return False
        for i in range(504800,504900):
            if CLID == str(i):
                #Personal Number Portability Codes
                return False
        for i in range(505000,505800):
            if CLID == str(i):
                #Non-Geographic Number Portability Transit Codes
                return False
        for i in range(505800,505900):
            if CLID == str(i):
                #Personal Number Portability Transit Codes
                return False
        for i in range(510000,600000):
            if CLID == str(i):
                #Geographic Number Portability Codes
                return False
    if len(CLID) == 4:
        for i in range(7603,7623):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
        for i in range(7630,7640):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
        for i in range(7650,7654):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
        for i in range(7655,7659):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
        if CLID == "7680":
            #Mobile Number Portability Codes
            return False
        for i in range(7682,7693):
            if CLID == str(i):
                #obile Number Portability Codes
                return False
        for i in range(7694,7699):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
        for i in range(7991,7999):
            if CLID == str(i):
                #Mobile Number Portability Codes
                return False
    if len(CLID) == 5:
        for i in range(0,1024):
            if CLID == str(i).zfill(5):
                #National Signalling Point Codes
                return False
        for i in range(12288,16384):
            if CLID == str(i):
                #print("National Signalling Point Codes
                return False
        if CLID[4] in ["0","1","2","3","4","5","6","7"]:
            #International Signalling Point Codes designated by Ofcom
            return False
        for i in range(23400,23500):
            if CLID == str(i):
                #Mobile Network Codes
                return False
        for i in range(23500,23600):
            if CLID == str(i):
                #Mobile Network Codes
                return False
    if len(CLID) == 6:
        for i in range(1,1000):
            if CLID[:3] == str(i).zfill(3):
                #Partial Calling Line Identity Codes
                return False
    if len(CLID) == 4:
        for i in range(7000,7090):
            if CLID == str(i):
                #Targeted Transit Codes
                return False
        for i in range(8000,8890):
            if CLID == str(i):
                #Carrier Pre-Selection Codes
                return False
        for i in range(8900,9000):
            if CLID == str(i):
                #Carrier Pre-Selection Codes
                return False
    if len(CLID) == 10:
        if CLID[:5] == "08979":
            #Inserted Network Numbers for Calling Line Identification
            return False
        for i in range(89930,90000):
            if CLID[:6] == str(i).zfill(6):
                #print("Inbound Routing Codes
                return False
    if len(CLID) == 4:
        #X25 Data Network Identification Codes
        return False
    if len(CLID) == 3:
        #Communications Provider Identification Codes
        return False
    for char in CLID:
        if char not in ["1","2","3","4","5","6","7","8","9","0"]:
            #Reseller Identification Codes
            return False
    #Nothing
    return False

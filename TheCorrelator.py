import csv,datetime,sys

#CONST
dateTimeFormat = "%Y%m%d%H%M%S"
endDateTimeWindow = 3
callRedirectionWindow = [0,3]
roamingCallbackWindow = [10,20]
thresholdCLID = 5
thresholdAccessCode = 10

def SaveCDR(data,name):
    with open(name+".csv","w",newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerows(data)

def ReadCDR(filename):
    CDR = []
    with open(filename+".csv","r",newline="") as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        for record in reader:
            CDR.append(record)
    return CDR

def FilterEndDateTime(endDateTime1, endDateTime2):
    if endDateTime1 > endDateTime2:
        difference = endDateTime1 - endDateTime2
    else:
        difference = endDateTime2 - endDateTime1
    if difference.seconds <= endDateTimeWindow:
        return True
    else:
        return False

def GetCallType(type1,type2):
    if (type1 == "MO") and (type2 == "MO"):
        return False
    elif (type1 == "MO") and (type2 == "MT"):
        return "CR"
    elif (type1 == "MT") and (type2 == "MO"):
        return "CR"
    elif (type1 == "MT") and (type2 == "MT"):
        return "RC"
    else:
        raise ValueError("Call type(s) are not valid")

def FilterStartDateTime(mechanism,startDateTime1,startDateTime2):
    if startDateTime1 > startDateTime2:
        difference = startDateTime1 - startDateTime2
    else:
        difference = startDateTime2 - startDateTime1
    if mechanism == "RC":
        if (difference.seconds >= roamingCallbackWindow[0]) and (difference.seconds <= roamingCallbackWindow[1]):
            return True
        else:
            return False
    elif mechanism == "CR":
        if (difference.seconds >= callRedirectionWindow[0]) and (difference.seconds <= callRedirectionWindow[1]):
            return True
        else:
            return False
    else:
        raise ValueError("Mechanism not valid")

def TimingHeuristicFilter(CDR1,CDR2):
    pairs = []
    for record1 in CDR1:
        for record2 in CDR2:
            endDateTime1 = datetime.datetime.strptime(record1[2], dateTimeFormat)
            endDateTime2 = datetime.datetime.strptime(record2[2], dateTimeFormat)
            if FilterEndDateTime(endDateTime1,endDateTime2):
                mechanism = GetCallType(record1[3],record2[3])
                if mechanism in ["CR","RC"]:
                    startDateTime1 = datetime.datetime.strptime(record1[1], dateTimeFormat)
                    startDateTime2 = datetime.datetime.strptime(record2[1], dateTimeFormat)
                    if FilterStartDateTime(mechanism,startDateTime1,startDateTime2):
                        pairs.append((record1,record2,mechanism))
    return pairs

def main():
    filename1 = sys.argv[1]
    if filename1[-4:] == ".csv":
        filename1 = filename1[:-4]
    filename2 = sys.argv[2]
    if filename2[-4:] == ".csv":
        filename2 = filename2[:-4]
    CDR1 = ReadCDR(filename1)
    CDR2 = ReadCDR(filename2)
    timingResults = TimingHeuristicFilter(CDR1,CDR2)
    numCR = 0
    numRC = 0
    results = []
    ID = 0
    for r in timingResults:
        x = [str(ID)] + r[0] + r[1]
        print(x)
        ID += 1
        results.append(x)
        if r[2] == "CR":
            numCR += 1
        elif r[2] == "RC":
            numRC += 1
        else:
            raise ValueError("Mechanism not valid after timing heuistic filter")
    numCorrelated = numCR + numRC
    propCR = numCR / max(len(CDR1),len(CDR2))
    propRC = numRC / max(len(CDR1),len(CDR2))
    propCorrelated = numCorrelated / max(len(CDR1),len(CDR2))
    print("The number of correlated calls using Call Redirection found was: {0}".format(numCR))
    print("And as a proportion this was: {0}".format(propCR))
    print("The number of correlated calls using Roaming Callback found was: {0}".format(numRC))
    print("And as a proportion this was: {0}".format(propRC))
    print("The number of correlated calls in total found was: {0}".format(numCorrelated))
    print("And as a proportion  this was: {0}".format(propCorrelated))
    print("The records found have been saved in: {0}".format(filename1 + "RESULTS"))
    SaveCDR(results,filename1+"RESULTS")

if __name__ == "__main__":
    main()

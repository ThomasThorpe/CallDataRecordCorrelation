import csv,datetime,sys

dateTimeFormat = "%Y%m%d%H%M%S"

def SaveCDR(data,name):
    with open(name+".csv","w",newline="") as csvfile:
        writer = csv.writer(csvfile,delimiter=",")
        writer.writerows(data)

def ReadCDR(filename):
    CDRRaw = []
    with open(filename+".csv","r",newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for record in reader:
            CDRRaw.append(record)
    return CDRRaw

def ParseO2CDR(CDRRaw):
    ID = 0
    CDR = []
    for record in CDRRaw:
        if record[0] not in ("MT","MO"):
            continue
        else:
            #assign ID
            r = []
            r.append(ID)
            ID += 1
            #parse startDateTime
            startDate = record[1] #dd/mm/yyyy
            startDate = startDate[6:] + startDate[3:5] + startDate[:2]
            startTime = record[2] #hh:mm:ss
            startTime = startTime[:2] + startTime[3:5] + startTime[6:]
            startDateTime = startDate + startTime
            r.append(startDateTime)
            #parse endDateTime
            startDateTime = datetime.datetime.strptime(startDateTime,dateTimeFormat)
            duration = record[3] #hh:mm:ss
            seconds = int(duration[6:])
            minutes = int(duration[3:5])
            hours = int(duration[:2])
            duration = datetime.timedelta(seconds=seconds,minutes=minutes,hours=hours)
            endDateTime = startDateTime + duration
            endDateTime = endDateTime.strftime(dateTimeFormat)
            r.append(endDateTime)
            #parse call type
            callType = record[0]
            r.append(callType)
            #parse calling number
            calling = record[6]
            if calling[:3] == "+44":
                calling = "0" + calling[3:]
            if (len(calling) != 10) and (len(calling) != 11):
                calling = calling.zfill(11)
            r.append(calling)
            #parse called number
            called = record[10]
            if called[:3] == "+44":
                called = "0" + called[3:]
            if (len(called) != 10) and (len(called) != 11):
                called = called.zfill(11)
            r.append(called)
            CDR.append(r)
    return CDR

def ParseVodafoneCDR(CDRRaw):
    ID = 0
    CDR = []
    for record in CDRRaw:
        if record[0] not in ("MT","MO"):
            continue
        else:
            #assign ID
            r = []
            r.append(ID)
            ID += 1
            #parse startDateTime
            startDateTime = record[2]
            if len(startDateTime) == 19:
                startDateTime = startDateTime[6:10] + startDateTime[3:5] + startDateTime[:2] + startDateTime[11:13] + startDateTime[14:16] + startDateTime[17:19]
            elif len(startDateTime) == 16:
                startDateTime = startDateTime[6:10] + startDateTime[3:5] + startDateTime[:2] + startDateTime[11:13] + startDateTime[14:16] + "00"
            r.append(startDateTime)
            #parse endDateTime
            startDateTime = datetime.datetime.strptime(startDateTime,dateTimeFormat)
            duration = record[4]
            duration = datetime.timedelta(seconds=int(duration))
            endDateTime = startDateTime + duration
            endDateTime = endDateTime.strftime(dateTimeFormat)
            r.append(endDateTime)
            #parse call type
            callType = record[0]
            r.append(callType)
            #parse calling number
            calling = record[5]
            if calling[:3] == "+44":
                calling = "0" + calling[3:]
            if (len(calling) != 10) and (len(calling) != 11):
                calling = calling.zfill(11)
            r.append(calling)
            #parse called number
            called = record[6]
            if called[:3] == "+44":
                called = "0" + called[3:]
            if (len(called) != 10) and (len(called) != 11):
                called = called.zfill(11)
            r.append(called)
            CDR.append(r)
    return CDR

def ParseEECDR(CDRRaw):
    ID = 0
    CDR = []
    for record in CDRRaw:
        if record[0] == "Start Date":
            continue
        else:
            #assign ID
            r = []
            r.append(ID)
            ID += 1
            #parse startDateTime
            startDate = record[0]
            startTime = record[1]
            startDateTime = startDate[6:] + startDate[3:5] + startDate[:2] + startTime[:2] + startTime[3:5] + startTime[6:8]
            r.append(startDateTime)
            #parse endDateTime
            endDate = record[2]
            endTime = record[3]
            endDateTime = endDate[6:] + endDate[3:5] + endDate[:2] + endTime[:2] + endTime[3:5] + endTime[6:8]
            r.append(endDateTime)
            #parse call type
            callType = record[7]
            r.append(callType)
            #parse calling number
            calling = record[4]
            if calling[:3] == "+44":
                calling = "0" + calling[3:]
            if (len(calling) != 10) and (len(calling) != 11):
                calling = calling.zfill(11)
            r.append(calling)
            #parse called number
            called = record[5]
            if called[:3] == "+44":
                called = "0" + called[3:]
            if (len(called) != 10) and (len(called) != 11):
                called = called.zfill(11)
            r.append(called)
            CDR.append(r)
    return CDR

def ParseH3GCDR(CDRRaw):
    ID = 0
    CDR = []
    for record in CDRRaw:
        if record[0] == "Date and Time of Call":
            continue
        else:
            #assign ID
            r = []
            r.append(ID)
            ID += 1
            #parse startDateTime
            startDateTime = record[0]
            if len(startDateTime) == 19: #dd/mm/yyyy hh:mm:ss
                startDateTime = startDateTime[6:10] + startDateTime[3:5] + startDateTime[:2] + startDateTime[11:13] + startDateTime[14:16] + startDateTime[17:19]
            elif len(startDateTime) == 16: #dd/mm/yyyy hh:mm
                startDateTime = startDateTime[6:10] + startDateTime[3:5] + startDateTime[:2] + startDateTime[11:13] + startDateTime[14:16] + "00"
            else:
                raise ValueError("startDateTime not in correct format")
            r.append(startDateTime)
            startDateTime = datetime.datetime.strptime(startDateTime,dateTimeFormat)
            #parse endDateTime
            duration = record[8]
            duration = datetime.timedelta(seconds=int(duration))
            endDateTime = startDateTime + duration
            endDateTime = endDateTime.strftime(dateTimeFormat)
            r.append(endDateTime)
            #parse call type
            callType = record[7]
            r.append(callType)
            #parse calling number
            calling = record[1]
            if calling[:3] == "+44":
                calling = "0" + calling[3:]
            if (len(calling) != 10) and (len(calling) != 11):
                calling = calling.zfill(11)
            r.append(calling)
            #parse called number
            called = record[3]
            if called[:3] == "+44":
                called = "0" + called[3:]
            if (len(called) != 10) and (len(called) != 11):
                called = called.zfill(11)
            r.append(called)
            CDR.append(r)
    return CDR

def MergeH3G(CDR1,CDR2):
    #CDRs from H3G parser, no ID or class labels
    CDR = []
    t = datetime.datetime(2100,1,1)
    index = -1
    ID = 0
    while (len(CDR1) != 0) or (len(CDR2) != 0):
        #print("starting loop")
        if len(CDR1) != 0:
            #print("CDR1 not empty, for loop time")
            for i in range(len(CDR1)):
                end = datetime.datetime.strptime(CDR1[i][2],dateTimeFormat)
                if end < t:
                    t = end
                    index = (i,1)
        if len(CDR2) != 0:
            #print("CDR2 not empty, for loop time")
            for i in range(len(CDR2)):
                end = datetime.datetime.strptime(CDR2[i][2],dateTimeFormat)
                if end < t:
                    t = end
                    index = (i,2)
        if index[1] == 1:
            r = CDR1.pop(index[0])
            CDR.append([ID] + r[1:])
            ID += 1
            t = datetime.datetime(2100,1,1)
        else:
            r = CDR2.pop(index[0])
            CDR.append([ID] + r[1:])
            ID += 1
            t = datetime.datetime(2100,1,1)
        #print(CDR)
    return CDR

def IdentifyProvider(parameters):
    if len(parameters) == 1:
        filename = parameters[0]
        if filename[-4:] == ".csv":
            filename = filename[:-4]
        CDR1 = ReadCDR(filename)
        CDR2 = None
    elif len(parameters) == 2:
        filename = parameters[0]
        if filename[-4:] == ".csv":
            filename = filename[:-4]
        filename2 = parameters[1]
        if filename2[-4:] == ".csv":
            filename2 = filename2[:-4]
        CDR1 = ReadCDR(filename)
        CDR2 = ReadCDR(filename2)
    if CDR1[0][0] == "Start Date":
        CDR = ParseEECDR(CDR1) #EE
        SaveCDR(CDR,filename+"PARSED")
    elif CDR1[0][0] == "Date and Time of Call" and CDR2[0][0] == "Date and Time of Call":
        CDRt1 = ParseH3GCDR(CDR1) #H3G
        CDRt2 = ParseH3GCDR(CDR2)
        CDR = MergeH3G(CDRt1,CDRt2)
        SaveCDR(CDR,filename+"PARSED")
    elif CDR1[0][0] == "Record":
        CDR = ParseO2CDR(CDR1) #O2
        SaveCDR(CDR,filename+"PARSED")
    elif CDR1[0][0] == "Event - Tariff":
        CDR = ParseVodafoneCDR(CDR1) #Vodafone
        SaveCDR(CDR,filename+"PARSED")
    else:
        print("There is no headers to detect the mobile network")
        print("1. EE")
        print("2. H3G")
        print("3. O2")
        print("4. Vodafone")
        x = int(input("Please select an option above: "))
        if x == 1:
            CDR = ParseEECDR(CDR1)
            SaveCDR(CDR,filename+"PARSED")
        elif x == 2:
            if len(parameters) != 2:
                raise ValueError("Two files are required for H3G, both incoming and outgoing")
            else:
                CDRt1 = ParseH3GCDR(CDR1)
                CDRt2 = ParseH3GCDR(CDR2)
                CDR = MergeH3G(CDRt1,CDRt2)
                SaveCDR(CDR,filename+"PARSED")
        elif x == 3:
            CDR = ParseO2CDR(CDR1)
            SaveCDR(CDR,filename+"PARSED")
        elif x == 4:
            CDR = ParseVodafoneCDR(CDR1)
            SaveCDR(CDR,filename+"PARSED")
        else:
            raise ValueError("That is not a valid option!")

def main():
    IdentifyProvider(sys.argv[1:3])

if __name__ == "__main__":
    main()

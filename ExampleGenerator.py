import csv, datetime,random,math
from CLIDChecker import CheckCLID
from AreaCodes import AreaCodes

#CONST
dateTimeFormat = "%Y%m%d%H%M%S"

def SaveCDR(data,name):
    with open(name+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)

#Returns two test CDRs between spoofer and nonspoofer
#[ID,startdatetime,enddatetime,type,calling,called,ClassLabel]
def CreatePairCDRsSpooferNonSpoofer(size,gap,propNormal,propCR,propRC,propAccess,num1=None,num2=None):
    CDR1 = []
    CDR2 = []
    normalSize = int(math.floor(size * propNormal))
    CRSize = int(math.floor(size * propCR))
    RCSize = int(math.floor(size * propRC))
    accessSize = int(math.floor(size * propAccess))
    timeBootStrap = datetime.datetime.today()
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        num2 = MobileNumber()
    #Generate all normal record pairs without times
    normalPool = []
    for i in range(0,normalSize):
        tmp = random.randint(0,2)
        if tmp == 0: #normal outgoing call using Call Redirection
            x = SpooferNonSpooferCR1(num1)
            r1 = x[0]
        elif tmp == 1: #normal outgoing call using Roaming Callback
            x = SpooferNonSpooferRC1(num1)
            r1 = x[0]
        else: #normal incoming call
            x = NonSpooferSpoofer1(num2=num1)
            r1 = x[1]
        y = NonSpooferNonSpoofer1(num2)
        r2 = y[0]
        normalPool.append((r1,r2))
    #Generate all Call Redirection pairs without times
    CRPool = []
    for i in range(0,CRSize):
        CRPool.append(SpooferNonSpooferCR1(num1,num2))
    #Generate all Roaming Callback pairs without times
    RCPool = []
    for i in range(0,RCSize):
        RCPool.append(SpooferNonSpooferRC1(num1,num2))
    #Generate all calls from non-spoofer to spoofer
    accessPool = []
    for i in range(0,accessSize):
        z = NonSpooferSpoofer1(num2,num1)
        x = (z[1],z[0])
        accessPool.append(x)
    #make sure correct size due to rounding
    while (len(normalPool) + len(CRPool) + len(RCPool) + len(accessPool)) < size:
        x = SpooferNonSpooferCR1(num1)
        r1 = x[0]
        y = SpooferNonSpooferCR1(num2)
        r2 = y[0]
        normalPool.append((r1,r2))
    #Shuffle calls into CDRs and assign timestamps
    t1 = datetime.datetime.strftime(timeBootStrap,dateTimeFormat)
    for i in range(0,size):
        tmp = random.randint(0,3)
        if tmp == 0: #pick normal call, else CR, else RC, else Access
            if len(normalPool) != 0:
                x = normalPool.pop()
                tmp = AddTimeSpooferNonSpooferNormal(t1,gap,x)
                r1 = tmp[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = tmp[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = tmp[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(CRPool) != 0:
                x = CRPool.pop()
                z = SpooferNonSpooferCR2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(RCPool) != 0:
                x = RCPool.pop()
                z = SpooferNonSpooferRC2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = accessPool.pop()
                z = NonSpooferSpoofer2(t1,gap,x[1],x[0])
                r1 = z[1]
                r1 = [str(i)] + r1 + ["3"]
                r2 = z[0]
                r2 = [str(i)] + r2 + ["3"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
        elif tmp == 1: #pick CR, else RC, else Access, else normal call
            if len(CRPool) != 0:
                x = CRPool.pop()
                z = SpooferNonSpooferCR2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(RCPool) != 0:
                x = RCPool.pop()
                z = SpooferNonSpooferRC2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(accessPool) != 0:
                x = accessPool.pop()
                z = NonSpooferSpoofer2(t1,gap,x[1],x[0])
                r1 = z[1]
                r1 = [str(i)] + r1 + ["3"]
                r2 = z[0]
                r2 = [str(i)] + r2 + ["3"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = normalPool.pop()
                tmp = AddTimeSpooferNonSpooferNormal(t1,gap,x)
                r1 = tmp[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = tmp[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = tmp[2]
                CDR1.append(r1)
                CDR2.append(r2)
        elif tmp == 2: #pick RC, else Access, else normal call, else CR
            if len(RCPool) != 0:
                x = RCPool.pop()
                z = SpooferNonSpooferRC2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(accessPool) != 0:
                x = accessPool.pop()
                z = NonSpooferSpoofer2(t1,gap,x[1],x[0])
                r1 = z[1]
                r1 = [str(i)] + r1 + ["3"]
                r2 = z[0]
                r2 = [str(i)] + r2 + ["3"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(normalPool) != 0:
                x = normalPool.pop()
                tmp = AddTimeSpooferNonSpooferNormal(t1,gap,x)
                r1 = tmp[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = tmp[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = tmp[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = CRPool.pop()
                z = SpooferNonSpooferCR2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
        else: #pick Access, else normal call, else CR, else RC
            if len(accessPool) != 0:
                x = accessPool.pop()
                z = NonSpooferSpoofer2(t1,gap,x[1],x[0])
                r1 = z[1]
                r1 = [str(i)] + r1 + ["3"]
                r2 = z[0]
                r2 = [str(i)] + r2 + ["3"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(normalPool) != 0:
                x = normalPool.pop()
                tmp = AddTimeSpooferNonSpooferNormal(t1,gap,x)
                r1 = tmp[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = tmp[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = tmp[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(CRPool) != 0:
                x = CRPool.pop()
                z = SpooferNonSpooferCR2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = RCPool.pop()
                z = SpooferNonSpooferRC2(t1,gap,x[0],x[1])
                r1 = z[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = z[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = z[2]
                CDR1.append(r1)
                CDR2.append(r2)
    return (CDR1,CDR2)

#Returns two test CDRs between two spoofers
#[ID,startdatetime,enddatetime,type,calling,called,ClassLabel]
def CreatePairCDRsSpooferSpoofer(size,gap,propNormal,propCR,propRC,num1=None,num2=None):
    CDR1 = []
    CDR2 = []
    normalSize = int(math.floor(size * propNormal))
    CRSize = int(math.floor(size * propCR))
    RCSize = int(math.floor(size * propRC))
    timeBootStrap = datetime.datetime.today()
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        num2 = MobileNumber()
    #Generate all normal record pairs without times
    normalPool = []
    for i in range(0,normalSize):
        tmp = random.randint(0,2)
        if tmp == 0: #normal outgoing call using Call Redirection
            x = SpooferNonSpooferCR1(num1)
            r1 = x[0]
        elif tmp == 1: #normal outgoing call using Roaming Callback
            x = SpooferNonSpooferRC1(num1)
            r1 = x[0]
        else: #normal incoming call
            x = NonSpooferSpoofer1(num2=num1)
            r1 = x[1]
        tmp = random.randint(0,2)
        if tmp == 0: #normal outgoing call using Call Redirection
            y = SpooferNonSpooferRC1(num2)
            r2 = y[0]
        elif tmp == 1: #normal outgoing call using Roaming Calback
            y = SpooferNonSpooferRC1(num2)
            r2 = y[0]
        else: #normal incoming call
            y = NonSpooferSpoofer1(num2=num2)
            r2 = y[1]
        normalPool.append((r1,r2))
    #Generate all correlated Call Redirection pairs without times
    CRPool = []
    for i in range(0,CRSize):
        CRPool.append(SpooferSpooferCR1(num1,num2))
    #Generate all correlated Roaming Callback pairs without times
    RCPool = []
    for i in range(0,RCSize):
        RCPool.append(SpooferSpooferRC1(num1,num2))
    #make sure correct size due to rounding
    while (len(normalPool) + len(CRPool) + len(RCPool)) < size:
        x = SpooferNonSpooferCR1(num1)
        r1 = x[0]
        y = SpooferNonSpooferCR1(num2)
        r2 = y[0]
        normalPool.append((r1,r2))
    #Shuffle calls into CDRs and assign timestamps
    t1 = datetime.datetime.strftime(timeBootStrap,dateTimeFormat)
    for i in range(0,size):
        tmp = random.randint(0,2)
        if tmp == 0: #pick normal call, else CR, else RC
            if len(normalPool) != 0:
                x = normalPool.pop()
                records = AddTimeSpooferSpooferNormal(t1,gap,x)
                r1 = records[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(CRPool) != 0:
                x = CRPool.pop()
                records = SpooferSpooferCR2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = RCPool.pop()
                records = SpooferSpooferRC2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
        elif tmp == 1: #pick CR, else RC, else normal
            if len(CRPool) != 0:
                x = CRPool.pop()
                records = SpooferSpooferCR2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(RCPool) != 0:
                x = RCPool.pop()
                records = SpooferSpooferRC2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = normalPool.pop()
                records = AddTimeSpooferSpooferNormal(t1,gap,x)
                r1 = records[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
        else: #pick RC, else normal, else CR
            if len(RCPool) != 0:
                x = RCPool.pop()
                records = SpooferSpooferRC2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["2"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["2"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            elif len(normalPool) != 0:
                x = normalPool.pop()
                records = AddTimeSpooferSpooferNormal(t1,gap,x)
                r1 = records[0]
                r1 = [str(i)] + r1 + ["0"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["0"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
            else:
                x = CRPool.pop()
                records = SpooferSpooferCR2(t1,gap,x[0],x[1])
                r1 = records[0]
                r1 = [str(i)] + r1 + ["1"]
                r2 = records[1]
                r2 = [str(i)] + r2 + ["1"]
                t1 = records[2]
                CDR1.append(r1)
                CDR2.append(r2)
    return (CDR1,CDR2)

def AddTimeSpooferNonSpooferNormal(t1,gap,x):
    t1 = datetime.datetime.strptime(t1,dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    r1 = x[0]
    r2 = x[1]
    start1 = t1 + gap
    end1 = start1 + datetime.timedelta(seconds=random.randint(1,210))
    start2 = start1 + datetime.timedelta(seconds=random.randint(5,210))
    end2 = start2 + datetime.timedelta(seconds=random.randint(1,210))
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    start1 = start1.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

def AddTimeSpooferSpooferNormal(t1,gap,x):
    t1 = datetime.datetime.strptime(t1,dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    r1 = x[0]
    r2 = x[1]
    start1 = t1 + gap
    end1 = start1 + datetime.timedelta(seconds=random.randint(1,210))
    start2 = start1 + datetime.timedelta(seconds=random.randint(5,210))
    end2 = start2 + datetime.timedelta(seconds=random.randint(1,210))
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    start1 = start1.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    r1 = [start1,end1] + r1 
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Return two records for a Spoofer calling a NonSpoofer using the Call Redirection Mechanism
#record 1 is the spoofer
#WITHOUT TIMESTAMPS
def SpooferNonSpooferCR1(num1=None,num2=None):
    #Generate call types
    type1 = "MO"
    type2 = "MT"
    #Generate two numbers and fake CLID
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        if random.randint(0,1) == 0: #called a landline
            num2 = GeographicalNumber()
        else: #called a mobile
            num2 = MobileNumber()
    fake1 = FakeNumber()
    fake2 = FakeNumber()
    #Generate records
    r1 = [type1,num1,fake1]
    r2 = [type2,fake2,num2]
    return (r1,r2)

#ADDING TIMESTAMPS
def SpooferNonSpooferCR2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #generate starting and ending times
    start1 = t1 + gap
    start2 = start1 + datetime.timedelta(seconds = random.randint(0,2))
    end1 = start1 + datetime.timedelta(seconds = random.randint(3,210))
    end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode  back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Returns two records for a Spoofer calling a nonSpoofer using the Roaming Callback Mechanism
#record 1 is the spoofer
#WITHOUT TIMESTAMPTS
def SpooferNonSpooferRC1(num1=None,num2=None):
    #Generate call types
    type1 = "MT"
    type2 = "MT"
    #Genereate two numbers and two fake CLIDs
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        if random.randint(0,1) == 0: #called a landline
            num2 = GeographicalNumber()
        else:
            num2 = MobileNumber()
    fake1 = FakeNumber()
    fake2 = FakeNumber()
    #Generate records
    r1 = [type1,fake1,num1]
    r2 = [type2,fake2,num2]
    return (r1,r2)

#WITH TIMESTAMPS
def SpooferNonSpooferRC2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #generate startings and ending times
    start1 = t1 + gap
    start2 = start1 + datetime.timedelta(seconds = random.randint(10,15))
    end1 = start1 + datetime.timedelta(seconds = random.randint(16,210))
    end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode  back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Returns two records for a NonSpoofer calling a spoofer using access code
#record 1 is the nonspoofer
#WITHOUT TIMESTAMPS
def NonSpooferSpoofer1(num1=None,num2=None):
    #Generate Call Types
    type1 = "MO"
    type2 = "MT"
    #Generate two numbers and access code (random for now) and fake CLID
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        num2 = MobileNumber()
    access = GeographicalNumber()
    fake = FakeNumber()
    #Generate records
    r1 = [type1,num1,access]
    r2 = [type2,fake,num2]
    return (r1,r2)

#WITH TIMESTAMPS
def NonSpooferSpoofer2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #Generate startings and ending times
    start1 = t1 + gap
    start2 = start1 + datetime.timedelta(seconds = random.randint(0,2))
    end1 = start1 + datetime.timedelta(seconds = random.randint(3,210))
    end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode  back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Returns two records for a Call Redirection mechanism between two spoofers
#WITHOUT TIMESTAMPS
def SpooferSpooferCR1(num1=None,num2=None,types=None):
    #Generate call types
    if types == None:
        if random.randint(0,1) == 0:
            type1 = "MO"
            type2 = "MT"
        else:
            type1 = "MT"
            type2 = "MO"
    else:
        type1 = types[0]
        type2 = types[1]
    #Generate two numbers and the access code and fake CLID
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        num2 = MobileNumber()
    access = GeographicalNumber()
    fake = FakeNumber()
    #generate records
    if type1 == "MO":
        r1 = [type1,num1,access]
        r2 = [type2,fake,num2]
    else:
        r1 = [type1,fake,num1]
        r2 = [type2,num2,access]
    return (r1,r2)

#WITH TIMESTAMPS
def SpooferSpooferCR2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #Generate starting times and ending times
    if r1[0] == "MO":
        start1 = t1 + gap
        start2 = start1 + datetime.timedelta(seconds = random.randint(0,2))
        end1 = start1 + datetime.timedelta(seconds = random.randint(3,210))
        end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    else:
        start2 = t1 + gap
        start1 = start2 + datetime.timedelta(seconds = random.randint(0,2))
        end2 = start2 + datetime.timedelta(seconds = random.randint(3,210))
        end1 = end2 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode  back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Returns two records for a Roaming Callback mechanism between two spoofers
#WITHOUT TIMESTAMPS
def SpooferSpooferRC1(num1=None,num2=None):
    #Generate call types
    type1 = "MT"
    type2 = "MT"
    #Generate two real random numbers and two random fake numbers which are used in spoofing
    if num1 == None:
        num1 = MobileNumber()
    if num2 == None:
        num2 = MobileNumber()
    fake1 = FakeNumber()
    fake2 = FakeNumber()
    #Generate records
    r1 = [type1,fake1,num1]
    r2 = [type2,fake2,num2]
    return (r1,r2)

#WITH TIMESTAMPS
def SpooferSpooferRC2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #Generate starting times and ending times
    if random.randint(0,1) == 0:
        start1 = t1 + gap
        start2 = start1 + datetime.timedelta(seconds = random.randint(10,15))
        end1 = start1 + datetime.timedelta(seconds = random.randint(16,210))
        end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    else:
        start2 = t1 + gap
        start1 = start2 + datetime.timedelta(seconds = random.randint(10,15))
        end2 = start2 + datetime.timedelta(seconds = random.randint(16,210))
        end1 = end2 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

#Returns two records for a normal call between two non-spoofers
#WITHOUT TIMESTAMPS
def NonSpooferNonSpoofer1(num1=None,num2=None,types=None):
    #Generate call types if needed
    if types == None:
        tmp = random.randint(0,99)
        if tmp < 49: #normal call
            type1 = "MO"
            type2 = "MT"
        elif tmp < 99: #normal call
            type1 = "MT"
            type2 = "MO"
        else: #small chance of roaming callback
            type1 = "MT"
            type2 = "MT"
    else:
        type1 = types[0]
        type2 = types[1]
    #Generate two random numbers that have called each other
    if num1 == None:
        if random.randint(0,1) == 0: #num1 is a landline number
            num1 = GeographicalNumber()
        else: #num1 is a mobile number
            num1 = MobileNumber()
    if num2 == None:
        if random.randint(0,1) == 0: #num2 is a landline number
            num2 = GeographicalNumber()
        else: #num2 is a mobile number
            num2 = MobileNumber()
    #generate records
    if type1 == "MO" and type2 == "MT":
        r1 = [type1,num1,num2]
        r2 = [type2,num1,num2]
    elif type1 == "MT" and type2 == "MO":
        r1 = [type1,num2,num1]
        r2 = [type2,num2,num1]
    elif type1 == "MT" and type2 == "MT":
        gatewayNum = GeographicalNumber()
        r1 = [type1,gatewayNum,num1]
        r2 = [type2,gatewayNum,num2]
    return (r1,r2)

#WITH TIMESTAMPS
def NonSpooferNonSpoofer2(t1,gap,r1,r2):
    t1 = datetime.datetime.strptime(t1, dateTimeFormat)
    gap = gap + random.randint(0,15)
    gap = datetime.timedelta(seconds=gap)
    #Generate starting times and ending times
    if r1[0]  == "MO" and r2[0] == "MT":
        start1 = t1 + gap
        start2 = start1 + datetime.timedelta(seconds = random.randint(0,2))
        end1 = start1 + datetime.timedelta(seconds = random.randint(3,210))
        end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    elif r1[0] == "MT" and r2[0] == "MO":
        start2 = t1 + gap
        start1 = start2 + datetime.timedelta(seconds = random.randint(0,2))
        end2 = start2 + datetime.timedelta(seconds = random.randint(3,210))
        end1 = end2 + datetime.timedelta(seconds = random.randint(0,2))
    else:
        start1 = t1 + gap
        start2 = start1 + datetime.timedelta(seconds = random.randint(0,2))
        end1 = start1 + datetime.timedelta(seconds = random.randint(3,210))
        end2 = end1 + datetime.timedelta(seconds = random.randint(0,2))
    #update ending time
    if end2 > end1:
        t1 = end2.strftime(dateTimeFormat)
    else:
        t1 = end1.strftime(dateTimeFormat)
    #Encode  back to strings
    start1 = start1.strftime(dateTimeFormat)
    start2 = start2.strftime(dateTimeFormat)
    end1 = end1.strftime(dateTimeFormat)
    end2 = end2.strftime(dateTimeFormat)
    #generate records
    r1 = [start1,end1] + r1
    r2 = [start2,end2] + r2
    return (r1,r2,t1)

def FakeNumber(tmp=None):
    if (tmp == None) or (tmp not in [0,1,2,3,4]):
        tmp = random.randint(0,5)
    if tmp == 0: #mobile number pool
        f = True
        while f:
            x = MobileNumber()
            if x != -1:
                f = False
    elif tmp == 1: #geographical number pool
        f = True
        while f:
            x = GeographicalNumber()
            if x != -1:
                f = False
    elif tmp == 2: #fake looking area codes
        x = random.choice(["021","022","025","026","027","01238","01421","01762"])
        if len(x) == 3:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,9999999)).zfill(7)
            else: #11 digit number
                x = x + str(random.randint(0,99999999)).zfill(8)
        else:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,99999)).zfill(5)
            else: #11 digit number
                x = x + str(random.randint(0,999999)).zfill(6)
    elif tmp == 3: #lazy numbers
        n = str(random.randint(0,9)) * 10
        x = "0" + n
    else: #wrong lengths
        n = random.randint(1,9)
        ns = "9" * n
        x = str(random.randint(0,int(ns))).zfill(n)
    return x

def GeographicalNumber():
    f = True
    while f:
        x = str(random.choice(list(AreaCodes)))
        if len(x) == 6:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,9999)).zfill(4)
            else: #11 digit number
                x = x + str(random.randint(0,99999)).zfill(5)
        elif len(x) == 5:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,99999)).zfill(5)
            else: #11 digit number
                x = x + str(random.randint(0,999999)).zfill(6)
        elif len(x) == 4:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,999999)).zfill(6)
            else: #11 digit number
                x = x + str(random.randint(0,9999999)).zfill(7)
        elif len(x) == 3:
            if random.randint(0,1) == 0: #10 digit number
                x = x + str(random.randint(0,9999999)).zfill(7)
            else: #11 digit number
                x = x + str(random.randint(0,99999999)).zfill(8)
        else:
            raise ValueError("Area code length wasn't in range[3,6]")
        if CheckCLID(x) == True:
            f = False
    return x

def MobileNumber():
    f = True
    while f:
        x = "0" + str(7) + str(random.choice([1,2,3,4,5,7,8,9]))
        x = x + str(random.randint(0,99999999)).zfill(8)
        if CheckCLID(x) == True:
            f = False
    return x

#I would recommend directly calling the CDR generator with parameters
#Leaving this running will create a LOT of data if left to finish
def main():
    ID = 0
    for size in [10,100,1000,10000]:
        for gap in [15,30,45,60]:
            x = []
            for i in range(0,71,10):
                x.append(i/100)
            for propNormal in x:
                remainder = 1 - propNormal
                y = []
                for i in range(0,71,10):
                    y.append(i/100)
                for i in range(len(y)):
                    y[i] = y[i] * remainder
                for propCR in y:
                    propRC = 1 - propCR - propNormal
                    r = CreatePairCDRsSpooferSpoofer(size,gap,propNormal,propCR,propRC)
                    CDR1 = r[0]
                    CDR2 = r[1]
                    propNormal = round(propNormal,5)
                    propCR = round(propCR,5)
                    propRC = round(propRC,5)
                    SaveCDR(CDR1,"{0}A-S-S-{1}-{2}-{3}-{4}-{5}".format(ID,size,gap,propNormal,propCR,propRC))
                    SaveCDR(CDR2,"{0}B-S-S-{1}-{2}-{3}-{4}-{5}".format(ID,size,gap,propNormal,propCR,propRC))
                    print("ID: {0}".format(ID))
                    ID += 1
    for size in [10,100,1000,10000]:
        for gap in [15,30,45,60]:
            x = []
            for i in range(0,71,10):
                x.append(i/100)
            for propNormal in x:
                remainder = 1 - propNormal
                y = []
                for i in range(0,71,10):
                    y.append(i/100)
                for i in range(len(y)):
                    y[i] = y[i] * remainder
                for propCR in y:
                    remainder = 1 - propNormal - propCR
                    z = []
                    for i in range(0,71,10):
                        z.append(i/100)
                    for i in range(len(z)):
                        z[i] = z[i] * remainder
                    for propRC in z:
                        propAccess = 1 - propNormal - propCR - propRC
                        r = CreatePairCDRsSpooferNonSpoofer(size,gap,propNormal,propCR,propRC,propAccess)
                        CDR1 = r[0]
                        CDR2 = r[1]
                        propNormal = round(propNormal,5)
                        propCR = round(propCR,5)
                        propRC = round(propRC,5)
                        propAccess = round(propAccess,5)
                        SaveCDR(CDR1,"{0}A-S-NS-{1}-{2}-{3}-{4}-{5}-{6}".format(ID,size,gap,propNormal,propCR,propRC,propAccess))
                        SaveCDR(CDR2,"{0}B-S-NS-{1}-{2}-{3}-{4}-{5}-{6}".format(ID,size,gap,propNormal,propCR,propRC,propAccess))
                        print("ID: {0}".format(ID))
                        ID += 1

if __name__ == "__main__":
	main()

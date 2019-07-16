import unittest,math,datetime
from CLIDChecker import CheckCLID
import ExampleGenerator as e

dateTimeFormat = "%Y%m%d%H%M%S"

class TestExampleGenerator(unittest.TestCase):
    def test_MobileNumber(self):
        self.assertTrue(CheckCLID(e.MobileNumber()))
    
    def test_GeographicalNumber(self):
        self.assertTrue(CheckCLID(e.GeographicalNumber()))
    
    def test_FakeNumber(self):
        for i in range(0,6):
            with self.subTest(i=i):
                x = e.FakeNumber(i)
                for j in range(len(x)):
                    with self.subTest(j=j):
                        self.assertIn(x[j],["0","1","2","3","4","5","6","7","8","9"])
    
    def test_NonSpooferNonSpoofer1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,5):
            with self.subTest(i=i):
                if i == 0: #test without parameters
                    x = e.NonSpooferNonSpoofer1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[1]))
                            elif j == 6:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                if r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] != r2[2]))
                                else: 
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                elif i == 1: #test with num1 being provided
                    x = e.NonSpooferNonSpoofer1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[1]))
                            elif j == 6:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                if r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] != r2[2]))
                                else: 
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                            elif j == 9:
                                if r1[0] == "MO" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == num1) and (r2[1] == num1))
                                elif r1[0] == "MT" and r2[0] == "MO":
                                    self.assertTrue((r1[2] == num1) and (r2[2] == num1))
                                elif r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue(r1[2] == num1)
                elif i == 2: #test with num2 being provided
                    x = e.NonSpooferNonSpoofer1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[1]))
                            elif j == 6:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                if r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] != r2[2]))
                                else: 
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                            elif j == 9:
                                if r1[0] == "MO" and r2[0] == "MT":
                                    self.assertTrue((r2[2] == num2) and (r1[2] == num2))
                                elif r1[0] == "MT" and r2[0] == "MO":
                                    self.assertTrue((r1[1] == num2) and (r2[1] == num2))
                                elif r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue(r2[2] == num2)
                elif i == 3: #test with num1 and num2 being provided
                    x = e.NonSpooferNonSpoofer1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[1]))
                            elif j == 6:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                if r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] != r2[2]))
                                else: 
                                    self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                            elif j == 9:
                                if r1[0] == "MO" and r2[0] == "MT":
                                    self.assertTrue((r1[1] == num1) and (r1[2] == num2) and (r2[1] == num1) and (r2[2] == num2))
                                elif r1[0] == "MT" and r2[0] == "MO":
                                    self.assertTrue((r1[1] == num2) and (r1[2] == num1) and (r2[1] == num2) and (r2[2] == num1))
                                elif r1[0] == "MT" and r2[0] == "MT":
                                    self.assertTrue((r1[2] == num1) and (r2[2] == num2))
                elif i == 4:#test numbers are in correct places when given each pair of call types
                    for j in range(0,3):
                        with self.subTest(j=j):
                            if j == 0:
                                x = e.NonSpooferNonSpoofer1(num1=num1,num2=num2,types=("MO","MT"))
                                r1, r2 = x[0], x[1]
                                self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                            elif j == 1:
                                x = e.NonSpooferNonSpoofer1(num1=num1,num2=num2,types=("MT","MO"))
                                r1, r2 = x[0], x[1]
                                self.assertTrue((r1[1] == r2[1]) and (r1[2] == r2[2]))
                            elif j == 2:
                                x = e.NonSpooferNonSpoofer1(num1=num1,num2=num2,types=("MT","MT"))
                                r1, r2 = x[0], x[1]
                                self.assertTrue((r1[1] == r2[1]) and (r1[2] != r2[2]))

                    
    def test_NonSpooferNonSpoofer2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        for i in range(0,3):
            with self.subTest(i=i):
                if i == 0: #test with call types MO,MT
                    x = e.NonSpooferNonSpoofer1(types=("MO","MT"))
                    r1, r2 = x[0], x[1]
                    x = e.NonSpooferNonSpoofer2(t1,gap,r1,r2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,12):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(x) == 3)
                            elif j == 1:
                                self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                            elif j == 2:
                                self.assertTrue(len(r1) == 5)
                            elif j == 3:
                                self.assertTrue(len(r2) == 5)
                            elif j == 4:
                                self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) ==datetime.datetime)
                            elif j == 5:
                                self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 6:
                                self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 7:
                                self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 8:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                t2 = datetime.datetime.strptime(t1,dateTimeFormat)
                                gap2 = datetime.timedelta(seconds = gap)
                                self.assertTrue(start1 >= (t2 + gap2))
                            elif j == 9:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                                self.assertTrue(end1 > start1)
                            elif j == 10:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                self.assertTrue(start2 >= start1)
                            elif j == 11:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                                self.assertTrue(end2 > start2)
                elif i == 1: #test with call types MT,MO
                    x = e.NonSpooferNonSpoofer1(types=("MT","MO"))
                    r1, r2 = x[0], x[1]
                    x = e.NonSpooferNonSpoofer2(t1,gap,r1,r2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,12):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(x) == 3)
                            elif j == 1:
                                self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                            elif j == 2:
                                self.assertTrue(len(r1) == 5)
                            elif j == 3:
                                self.assertTrue(len(r2) == 5)
                            elif j == 4:
                                self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) ==datetime.datetime)
                            elif j == 5:
                                self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 6:
                                self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 7:
                                self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 8:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                t2 = datetime.datetime.strptime(t1,dateTimeFormat)
                                gap2 = datetime.timedelta(seconds = gap)
                                self.assertTrue(start2 >= (t2 + gap2))
                            elif j == 9:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                                self.assertTrue(end1 > start1)
                            elif j == 10:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                self.assertTrue(start1 >= start2)
                            elif j == 11:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                                self.assertTrue(end2 > start2)
                elif i == 2: #test with call types MT,MT
                    x = e.NonSpooferNonSpoofer1(types=("MT","MT"))
                    r1, r2 = x[0], x[1]
                    x = e.NonSpooferNonSpoofer2(t1,gap,r1,r2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,12):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(x) == 3)
                            elif j == 1:
                                self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                            elif j == 2:
                                self.assertTrue(len(r1) == 5)
                            elif j == 3:
                                self.assertTrue(len(r2) == 5)
                            elif j == 4:
                                self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) ==datetime.datetime)
                            elif j == 5:
                                self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 6:
                                self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 7:
                                self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 8:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                t2 = datetime.datetime.strptime(t1,dateTimeFormat)
                                gap2 = datetime.timedelta(seconds = gap)
                                self.assertTrue(start1 >= (t2 + gap2))
                            elif j == 9:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                                self.assertTrue(end1 > start1)
                            elif j == 10:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                self.assertTrue(start2 >= start1)
                            elif j == 11:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                                self.assertTrue(end2 > start2) 

    def test_SpooferSpooferRC1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,4):
            with self.subTest(i=i):
                if i == 0: #test without parameters
                    x = e.SpooferSpooferRC1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,8):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                self.assertFalse(r1[1] == None)
                            elif j == 7:
                                self.assertFalse(r2[1] == None)
                elif i == 1: #test with providing num1
                    x = e.SpooferSpooferRC1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r1[2] == num1)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[1] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif i == 2: #test with providing num2
                    x = e.SpooferSpooferRC1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[1] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif  i == 3: #test with providing both num1 and num2
                    x = e.SpooferSpooferRC1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(r1[2] == num1)
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                self.assertFalse(r1[1] == None)
                            elif j == 9:
                                self.assertFalse(r2[1] == None)
 
    def test_SpooferSpooferRC2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        x = e.SpooferSpooferRC1()
        r1, r2 = x[0], x[1]
        x = e.SpooferSpooferRC2(t1,gap,r1,r2)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
                elif i == 10:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    if start1 > start2:
                        delta = start1 - start2
                    else:
                        delta = start2 - start1
                    self.assertTrue((delta.seconds >= 10) and (delta.seconds <= 15))

    def test_SpooferSpooferCR1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,5):
            with self.subTest(i=i):
                if i == 0: #test without parameters
                    x = e.SpooferSpooferCR1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,8):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                if r1[0] == "MO":
                                    self.assertTrue(CheckCLID(r1[1]))
                                else:
                                    self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                if r2[0] == "MO":
                                    self.assertTrue(CheckCLID(r2[1]))
                                else:
                                    self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                if r1[0] == "MO":
                                    self.assertFalse(r1[2] == None)
                                else:
                                    self.assertFalse(r1[1] == None)
                            elif j == 7:
                                if r2[0] == "MO":
                                    self.assertFalse(r2[2] == None)
                                else:
                                    self.assertFalse(r2[1] == None)
                elif i == 1: #test with providing num1
                    x = e.SpooferSpooferCR1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                if r1[0] == "MO":
                                    self.assertTrue(CheckCLID(r1[1]))
                                else:
                                    self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                if r2[0] == "MO":
                                    self.assertTrue(CheckCLID(r2[1]))
                                else:
                                    self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                if r1[0] == "MO":
                                    self.assertTrue(r1[1] == num1)
                                else:
                                    self.assertTrue(r1[2] == num1)
                            elif j == 7:
                                if r1[0] == "MO":
                                    self.assertFalse(r1[2] == None)
                                else:
                                    self.assertFalse(r1[1] == None)
                            elif j == 8:
                                if r2[0] == "MO":
                                    self.assertFalse(r2[2] == None)
                                else:
                                    self.assertFalse(r2[1] == None)
                elif i == 2: #test with providing num2
                    x = e.SpooferSpooferCR1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                if r1[0] == "MO":
                                    self.assertTrue(CheckCLID(r1[1]))
                                else:
                                    self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                if r2[0] == "MO":
                                    self.assertTrue(CheckCLID(r2[1]))
                                else:
                                    self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                if r2[0] == "MO":
                                    self.assertTrue(r2[1] == num2)
                                else:
                                    self.assertTrue(r2[2] == num2)
                            elif j == 7:
                                if r1[0] == "MO":
                                    self.assertFalse(r1[2] == None)
                                else:
                                    self.assertFalse(r1[1] == None)
                            elif j == 8:
                                if r2[0] == "MO":
                                    self.assertFalse(r2[2] == None)
                                else:
                                    self.assertFalse(r2[1] == None) 
                elif i == 3: #test with providing both num1 and num2
                    x = e.SpooferSpooferCR1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertIn(r1[0],["MT","MO"])
                            elif j == 3:
                                self.assertIn(r2[0],["MT","MO"])
                            elif j == 4:
                                if r1[0] == "MO":
                                    self.assertTrue(CheckCLID(r1[1]))
                                else:
                                    self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                if r2[0] == "MO":
                                    self.assertTrue(CheckCLID(r2[1]))
                                else:
                                    self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                if r1[0] == "MO":
                                    self.assertTrue(r1[1] == num1)
                                else:
                                    self.assertTrue(r1[2] == num1)
                            elif j == 7:
                                if r2[0] == "MO":
                                    self.assertTrue(r2[1] == num2)
                                else:
                                    self.assertTrue(r2[2] == num2)
                            elif j == 7:
                                if r1[0] == "MO":
                                    self.assertFalse(r1[2] == None)
                                else:
                                    self.assertFalse(r1[1] == None)
                            elif j == 8:
                                if r2[0] == "MO":
                                    self.assertFalse(r2[2] == None)
                                else:
                                    self.assertFalse(r2[1] == None)
                    
                elif i == 4: #test numbers are in correct places when given each pair of call types
                    for j in range(0,2):
                        with self.subTest(j=j):
                            if j == 0:
                                x = e.SpooferSpooferCR1(num1=num1,num2=num2,types=("MO","MT"))
                                r1, r2 = x[0], x[1]
                                self.assertTrue((r1[1] == num1) and (r2[2] == num2))
                            elif j == 1:
                                x = e.SpooferSpooferCR1(num1=num1,num2=num2,types=("MT","MO"))
                                r1, r2 = x[0], x[1]
                                self.assertTrue((r1[2] == num1) and (r2[1] == num2))
    
    def test_SpooferSpooferCR2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        for i in range(0,2):
            with self.subTest(i=i):
                if i == 0: #test with MO,MT
                    x = e.SpooferSpooferCR1(types=("MO","MT"))
                    r1, r2 = x[0], x[1]
                    x = e.SpooferSpooferCR2(t1,gap,r1,r2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,12):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(x) == 3)
                            elif j == 1:
                                self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                            elif j == 2:
                                self.assertTrue(len(r1) == 5)
                            elif j == 3:
                                self.assertTrue(len(r2) == 5)
                            elif j == 4:
                                self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 5:
                                self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 6:
                                self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 7:
                                self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 8:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                                self.assertTrue(end1 > start1)
                            elif j == 9:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                                self.assertTrue(end2 > start2)
                            elif j == 10:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                self.assertTrue(start2 >= start1)
                            elif j == 11:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                delta = start2 - start1
                                self.assertTrue((delta.seconds >= 0) and (delta.seconds <= 3))
                elif i == 1: #test with MT,MO
                    x = e.SpooferSpooferCR1(types=("MT","MO"))
                    r1, r2 = x[0], x[1]
                    x = e.SpooferSpooferCR2(t1,gap,r1,r2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,12):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(x) == 3)
                            elif j == 1:
                                self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                            elif j == 2:
                                self.assertTrue(len(r1) == 5)
                            elif j == 3:
                                self.assertTrue(len(r2) == 5)
                            elif j == 4:
                                self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 5:
                                self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 6:
                                self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                            elif j == 7:
                                self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                            elif j == 8:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                                self.assertTrue(end1 > start1)
                            elif j == 9:
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                                self.assertTrue(end2 > start2)
                            elif j == 10:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                self.assertTrue(start1 >= start2)
                            elif j == 1:
                                start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                                start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                                delta = start1 - start2
                                self.assertTrue((delta.seconds >= 0) and (delta.seconds <= 3))
    
    def test_NonSpooferSpoofer1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,4):
            with self.subTest(i=i):
                if i == 0: #test without parameters provided
                    x = e.NonSpooferSpoofer1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,8):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                self.assertFalse(r1[2] == None)
                            elif j == 7:
                                self.assertFalse(r2[1] == None)
                elif i == 1: #test with providing num1
                    x = e.NonSpooferSpoofer1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r1[1] == num1)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[2] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif i == 2: #test with providing num2
                    x = e.NonSpooferSpoofer1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[2] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif i == 3: #test with providing both num1 and num2
                    x = e.NonSpooferSpoofer1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(r1[1] == num1)
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                self.assertFalse(r1[2] == None)
                            elif j == 9:
                                self.assertFalse(r2[1] == None)

    def test_NonSpooferSpoofer2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        x = e.NonSpooferSpoofer1()
        r1, r2 = x[0], x[1]
        x = e.NonSpooferSpoofer2(t1,gap,r1,r2)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
                elif i == 10:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    delta = start2 - start1
                    self.assertTrue((delta.seconds >= 0) and (delta.seconds <= 3))
    
    def test_SpooferNonSpooferCR1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,4):
            with self.subTest(i=i):
                if i == 0: #test without parameters provided
                    x = e.SpooferNonSpooferCR1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,8):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                self.assertFalse(r1[2] == None)
                            elif j == 7:
                                self.assertFalse(r2[1] == None)
                elif i == 1: #test with providing num1
                    x = e.SpooferNonSpooferCR1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r1[1] == num1)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[2] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif i == 2: #test with providing num2
                    x = e.SpooferNonSpooferCR1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[2] == None)
                            elif j == 8:
                                self.assertFalse(r2[1] == None)
                elif i == 3: #test with providing both num1 and num2
                    x = e.SpooferNonSpooferCR1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MO")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[1]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(r1[1] == num1)
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                self.assertFalse(r1[2] == None)
                            elif j == 9:
                                self.assertFalse(r2[1] == None)
    
    def test_SpooferNonSpooferCR2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        x = e.SpooferNonSpooferCR1()
        r1, r2 = x[0], x[1]
        x = e.SpooferNonSpooferCR2(t1,gap,r1,r2)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
                elif i == 10:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    delta = start2 - start1
                    self.assertTrue((delta.seconds >= 0) and (delta.seconds <= 3))
    
    def test_SpooferNonSpooferRC1(self):
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        for i in range(0,4):
            with self.subTest(i=i):
                if i == 0: #test without parameters provided
                    x = e.SpooferNonSpooferRC1()
                    r1, r2 = x[0], x[1]
                    for j in range(0,8):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 6:
                                self.assertFalse(r1[1] == None)
                            elif j == 7:
                                self.assertFalse(r1[1] == None)
                elif i == 1: #test with providing num1
                    x = e.SpooferNonSpooferRC1(num1=num1)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r1[2] == num1)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[1] == None)
                            elif j == 8:
                                self.assertFalse(r1[1] == None)
                elif i == 2: #test with providing num2
                    x = e.SpooferNonSpooferRC1(num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,9):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 7:
                                self.assertFalse(r1[1] == None)
                            elif j == 8:
                                self.assertFalse(r1[1] == None)
                elif i == 3: #test with providing both num1 and num2
                    x = e.SpooferNonSpooferRC1(num1=num1,num2=num2)
                    r1, r2 = x[0], x[1]
                    for j in range(0,10):
                        with self.subTest(j=j):
                            if j == 0:
                                self.assertTrue(len(r1) == 3)
                            elif j == 1:
                                self.assertTrue(len(r2) == 3)
                            elif j == 2:
                                self.assertTrue(r1[0] == "MT")
                            elif j == 3:
                                self.assertTrue(r2[0] == "MT")
                            elif j == 4:
                                self.assertTrue(CheckCLID(r1[2]))
                            elif j == 5:
                                self.assertTrue(r2[2] == num2)
                            elif j == 6:
                                self.assertTrue(r1[2] == num1)
                            elif j == 7:
                                self.assertTrue(CheckCLID(r2[2]))
                            elif j == 8:
                                self.assertFalse(r1[1] == None)
                            elif j == 9:
                                self.assertFalse(r1[1] == None)

    def test_SpooferNonSpooferRC2(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        x = e.SpooferNonSpooferRC1()
        r1, r2 = x[0], x[1]
        x = e.SpooferNonSpooferRC2(t1,gap,r1,r2)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
                elif i == 10:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    delta = start2 - start1
                    self.assertTrue((delta.seconds >= 10) and (delta.seconds <= 15))
    
    def test_AddTimeSpooferSpooferNormal(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        x = e.SpooferNonSpooferCR1(num1=num1)
        r1 = x[0]
        y = e.SpooferNonSpooferRC1(num2)
        r2 = y[0]
        x = (r1,r2)
        x = e.AddTimeSpooferSpooferNormal(t1,gap,x)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
    
    def test_AddTimeSpooferNonSpooferNormal(self):
        t1 = datetime.datetime.today()
        t1 = t1.strftime(dateTimeFormat)
        gap = 15
        num1 = e.MobileNumber()
        num2 = e.MobileNumber()
        x = e.SpooferNonSpooferCR1(num1=num1)
        r1 = x[0]
        y = e.SpooferNonSpooferRC1(num2)
        r2 = y[0]
        x = (r1,r2)
        x = e.AddTimeSpooferNonSpooferNormal(t1,gap,x)
        r1, r2 = x[0], x[1]
        for i in range(0,11):
            with self.subTest(i=i):
                if i == 0:
                    self.assertTrue(len(x) == 3)
                elif i == 1:
                    self.assertTrue(type(datetime.datetime.strptime(x[2],dateTimeFormat)) == datetime.datetime)
                elif i == 2:
                    self.assertTrue(len(r1) == 5)
                elif i == 3:
                    self.assertTrue(len(r2) == 5)
                elif i == 4:
                    self.assertTrue(type(datetime.datetime.strptime(r1[0],dateTimeFormat)) == datetime.datetime)
                elif i == 5:
                    self.assertTrue(type(datetime.datetime.strptime(r1[1],dateTimeFormat)) == datetime.datetime)
                elif i == 6:
                    self.assertTrue(type(datetime.datetime.strptime(r2[0],dateTimeFormat)) == datetime.datetime)
                elif i == 7:
                    self.assertTrue(type(datetime.datetime.strptime(r2[1],dateTimeFormat)) == datetime.datetime)
                elif i == 8:
                    start1 = datetime.datetime.strptime(r1[0],dateTimeFormat)
                    end1 = datetime.datetime.strptime(r1[1],dateTimeFormat)
                    self.assertTrue(end1 > start1)
                elif i == 9:
                    start2 = datetime.datetime.strptime(r2[0],dateTimeFormat)
                    end2 = datetime.datetime.strptime(r2[1],dateTimeFormat)
                    self.assertTrue(end2 > start2)
    
    def test_CreatePairCDRsSpooferSpoofer(self):
        for size in [10]:
            for gap in [15]:
                x = []
                for i in range(0,76,25):
                    x.append(i/100)
                for propNormal in x:
                    y = []
                    for j in range(0,76,25):
                        y.append(j/100)
                    for i in range(len(y)):
                        y[i] = y[i] * (1 - propNormal)
                    for propCR in y:
                        propRC = 1 - propCR - propNormal
                        for k in range(0,10):
                            with self.subTest(size=size,gap=gap,propNormal=propNormal,propCR=propCR,propRC=propRC,k=k):
                                num1 = e.MobileNumber()
                                num2 = e.MobileNumber()
                                r = e.CreatePairCDRsSpooferSpoofer(size,gap,propNormal,propCR,propRC,num1=num1,num2=num2)
                                CDR1 = r[0]
                                CDR2 = r[1]
                                if k == 0: #ensure sizes are correct
                                    self.assertTrue((len(CDR1) == size) and (len(CDR2) == size))
                                elif k == 1: #ensure in correct order and of right gaps for CDR1
                                    end1 = datetime.datetime.strptime(CDR1[0][2],dateTimeFormat)
                                    end2 = datetime.datetime.strptime(CDR2[0][2],dateTimeFormat)
                                    results = []
                                    if end2 > end1:
                                        time = end2
                                    else:
                                        time = end1
                                    for l in range(1,size):
                                        start1 = datetime.datetime.strptime(CDR1[l][1],dateTimeFormat)
                                        start2 = datetime.datetime.strptime(CDR2[l][1],dateTimeFormat)
                                        end1 = datetime.datetime.strptime(CDR1[l][2],dateTimeFormat)
                                        end2 = datetime.datetime.strptime(CDR2[l][2],dateTimeFormat)
                                        if start1 > start2:
                                            if start2 >= (time + datetime.timedelta(seconds=gap)):
                                                results.append(True)
                                            else:
                                                results.append(False)
                                        else:
                                            if start1 >= (time + datetime.timedelta(seconds=gap)):
                                                results.append(True)
                                            else:
                                                results.append(False)
                                        if end1 > end2:
                                            time = end1
                                        else:
                                            time = end2
                                    f = True
                                    for i in range(len(results)):
                                        if results[i] == False:
                                            f = False
                                    self.assertTrue(f)
                                elif k == 2: #ensure correct number of normal calls in CDR1
                                    t = 0
                                    for l in range(len(CDR1)):
                                        if CDR1[l][6] == "0":
                                            t += 1
                                    normalSize = math.floor(size * propNormal)
                                    self.assertTrue((t == normalSize) or (t in range(normalSize,normalSize+5)),msg="{0} | {1}".format(t,normalSize))
                                elif k == 3: #ensure correct number of normal calls in CDR2
                                    t = 0
                                    for l in range(len(CDR2)):
                                        if CDR2[l][6] == "0":
                                            t += 1
                                    normalSize = math.floor(size * propNormal)
                                    self.assertTrue((t == normalSize) or (t in range(normalSize,normalSize+5)),msg="{0} | {1}".format(t,normalSize))
                                elif k == 4: #ensure correct number of CR Calls in CDR1
                                    t = 0
                                    for l in range(len(CDR1)):
                                        if CDR1[l][6] == "1":
                                            t += 1
                                    CRSize = math.floor(size * propCR)
                                    self.assertTrue(t == CRSize,msg=t)
                                elif k == 5: #ensure correct number of CR calls in CDR2
                                    t = 0
                                    for l in range(len(CDR2)):
                                        if CDR2[l][6] == "1":
                                            t += 1
                                    CRSize = math.floor(size * propCR)
                                    self.assertTrue(t == CRSize,msg=t)
                                elif k == 6: #ensure correct number of RC calls in CDR1
                                    t = 0
                                    for l in range(len(CDR1)):
                                        if CDR1[l][6] == "2":
                                            t += 1
                                    RCSize = math.floor(size * propRC)
                                    self.assertTrue(t == RCSize,msg=t)
                                elif k == 7: #ensure correct number of RC calls in CDR2
                                    t = 0
                                    for l in range(len(CDR2)):
                                        if CDR2[l][6] == "2":
                                            t += 1
                                    RCSize = math.floor(size * propRC)
                                    self.assertTrue(t == RCSize,msg=t)
                                elif k == 8: #verify num1 position is correct position
                                    f = True
                                    for record in CDR1:
                                        if record[3] == "MT":
                                            if record[5] != num1:
                                                f = False
                                        else:
                                            if record[4] != num1:
                                                f = False
                                    self.assertTrue(f)
                                elif k == 9: #verify num2 position is correct
                                    f = True
                                    for record in CDR2:
                                        if record[3] == "MT":
                                            if record[5] != num2:
                                                f = False
                                        else:
                                            if record[4] != num2:
                                                f = False
                                    self.assertTrue(f)
    
    def test_CreatePairCDRsSpooferNonSpoofer(self):
        for size in [10]:
            for gap in [15]:
                x = []
                for i in range(0,76,25):
                    x.append(i/100)
                for propNormal in x:
                    remainder = 1 - propNormal
                    y = []
                    for j in range(0,76,25):
                        y.append(j/100)
                    for i in range(len(y)):
                        y[i] = y[i] * remainder
                    for propCR in y:
                        remainder = 1 - propNormal - propCR
                        z = []
                        for k in  range(0,76,25):
                            z.append(k/100)
                        for i in range(len(z)):
                            z[i] = z[i] * remainder
                        for propRC in z:
                            propAccess = 1 - propNormal - propCR - propRC
                            for k in range(0,9):
                                with self.subTest(size=size,gap=gap,propNormal=propNormal,propCR=propCR,propRC=propRC,propAccess=propAccess,k=k):
                                    num1 = e.MobileNumber()
                                    num2 = e.MobileNumber()
                                    r = e.CreatePairCDRsSpooferNonSpoofer(size,gap,propNormal,propCR,propRC,propAccess,num1=num1,num2=num2)
                                    CDR1 = r[0]
                                    CDR2 = r[1]
                                    if k == 0: #ensure sizes are correct
                                        self.assertTrue((len(CDR1) == size) and (len(CDR2) == size),msg="{0} | {1}".format(len(CDR1),len(CDR2)))
                                    elif k == 1: #ensure in correct order and of right gaps
                                        end1 = datetime.datetime.strptime(CDR1[0][2],dateTimeFormat)
                                        end2 = datetime.datetime.strptime(CDR2[0][2],dateTimeFormat)
                                        results = []
                                        if end2 > end1:
                                            time = end2
                                        else:
                                            time = end1
                                        for l in range(1,size):
                                            start1 = datetime.datetime.strptime(CDR1[l][1],dateTimeFormat)
                                            start2 = datetime.datetime.strptime(CDR2[l][1],dateTimeFormat)
                                            end1 = datetime.datetime.strptime(CDR1[l][2],dateTimeFormat)
                                            end2 = datetime.datetime.strptime(CDR2[l][2],dateTimeFormat)
                                            if start1 > start2:
                                                if start2 >= (time + datetime.timedelta(seconds=gap)):
                                                    results.append(True)
                                                else:
                                                    results.append(False)
                                            else:
                                                if start1 >= (time + datetime.timedelta(seconds=gap)):
                                                    results.append(True)
                                                else:
                                                    results.append(False)
                                            if end1 > end2:
                                                time = end1
                                            else:
                                                time = end2
                                        f = True
                                        for i in range(len(results)):
                                            if results[i] == False:
                                                f = False
                                        self.assertTrue(f)
                                    elif k == 2: #ensure correct number of normal calls in CDR1
                                        t = 0
                                        for l in range(len(CDR1)):
                                            if CDR1[l][6] == "0":
                                                t += 1
                                        normalSize = math.floor(size * propNormal)
                                        self.assertTrue((t == normalSize) or (t in range(normalSize,normalSize+5)))
                                    elif k == 3: #ensure correct number of normal calls in CDR2
                                        t = 0
                                        for l in range(len(CDR2)):
                                            if CDR2[l][6] == "0":
                                                t += 1
                                        normalSize = math.floor(size * propNormal)
                                        self.assertTrue((t == normalSize) or (t in range(normalSize,normalSize+5)))
                                    elif k == 4: #ensure correct number of CR calls in CDR1
                                        t = 0
                                        for l in range(len(CDR1)):
                                            if CDR1[l][6] == "1":
                                                t += 1
                                        CRSize = math.floor(size * propCR)
                                        self.assertTrue(t == CRSize,msg="{0} | {1}".format(t,CRSize))
                                    elif k == 5: #ensure correct number of CR calls in CDR2
                                        t = 0
                                        for l in range(len(CDR2)):
                                            if CDR2[l][6] == "1":
                                                t += 1
                                        CRSize = math.floor(size * propCR)
                                        self.assertTrue(t == CRSize,msg="{0} | {1}".format(t,CRSize))
                                    elif k == 6: #ensure correct number of RC calls in CDR1
                                        t = 0
                                        for l in range(len(CDR1)):
                                            if CDR1[l][6] == "2":
                                                t += 1
                                        RCSize = math.floor(size * propRC)
                                        self.assertTrue(t == RCSize,msg="{0} | {1}".format(t,RCSize))
                                    elif k == 7: #ensure correct number of RC calls in CDR2
                                        t = 0
                                        for l in range(len(CDR2)):
                                            if CDR2[l][6] == "2":
                                                t += 1
                                        RCSize = math.floor(size * propRC)
                                        self.assertTrue(t == RCSize,msg="{0} | {1}".format(t,RCSize))
                                    elif k == 8: #ensure correct number of Access calls in CDR1
                                        t = 0
                                        for l in range(len(CDR1)):
                                            if CDR1[l][6] == "3":
                                                t += 1
                                        accessSize = math.floor(size * propAccess)
                                        self.assertTrue(t == accessSize,msg="{0} | {1}".format(t,accessSize))
                                    elif k == 9: #ensure correct number of Access calls in CDR2
                                        t = 0
                                        for l in range(len(CDR2)):
                                            if CDR2[l][6] == "3":
                                                t += 1
                                        accessSize = math.floor(size * propAccess)
                                        self.assertTrye(t == accessSize,msg="{0} | {1}".format(t,accessSize))
                                    elif k == 10: #verify num1 position is correct for all records
                                        f = True
                                        for record in CDR1:
                                            if record[3] == "MT":
                                                if record[5] != num1:
                                                    f = False
                                            else:
                                                if record[4] != num1:
                                                    f = False
                                        self.assertTrue(f)
                                    elif k == 11: #verify num2 position is correct for all records
                                        f = True
                                        for record in CDR2:
                                            if record[3] == "MT":
                                                if record[5] != num2:
                                                    f = False
                                            else:
                                                if record[4] != num2:
                                                    f = False
                                        self.assertTrue(f)

if __name__ == "__main__":
    unittest.main()

import unittest,datetime,csv
import TheCorrelator as e

class TestTheCorrelator(unittest.TestCase):
    def test_TimingHeuristicFilter(self):
        inputs = []
        for i in range(1,3):
            CDR1 = []
            with open(str(i)+"A.csv","r",newline="") as csvfile:
                reader = csv.reader(csvfile,delimiter=",")
                for record in reader:
                    CDR1.append(record)
            CDR2 = []
            with open(str(i)+"B.csv","r",newline="") as csvfile:
                reader = csv.reader(csvfile,delimiter=",")
                for record in reader:
                    CDR2.append(record)
            inputs.append((CDR1,CDR2))
        for CDRs in inputs:
            CDR1 = CDRs[0]
            CDR2 = CDRs[1]
            timingResults = e.TimingHeuristicFilter(CDR1,CDR2)
            trueCR = 0
            trueRC = 0
            for i in range(len(CDR1)):
                if CDR1[i][-1] == "1":
                    trueCR += 1
                elif CDR1[i][-1] == "2":
                    trueRC += 1
                elif CDR1[i][-1] == "3":
                    trueCR += 1
            numCR = 0
            numRC = 0
            for r in timingResults:
                if r[2] == "CR":
                    numCR += 1
                elif r[2] == "RC":
                    numRC += 1
            for i in range(0,10):
                with self.subTest(i=i):
                    if i == 0: #check number of RC is correct
                        self.assertTrue(numRC == trueRC,msg="{0} | {1} | {2}".format(numRC,trueRC,len(CDR1)))
                    elif i == 1: #check number of RC/Access is correct
                        self.assertTrue(numCR == trueCR,msg="{0} | {1} | {2}".format(numCR,trueCR,len(CDR2)))

if __name__ == "__main__":
    unittest.main()

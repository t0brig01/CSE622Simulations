import sys
import numpy as np
import matplotlib.pyplot as plt 
import random

class Pair:
    def __init__(self, student1, student2):
        self.student1 = student1
        self.student2 = student2

class Student:
    timesHeard = 0
    def __init__(self,knowsRumor):
        self.knowsRumor = knowsRumor
        if(self.knowsRumor):
            self.timesHeard = 1
        else:
            self.timesHeard = 0
    def spreadRumor(self):
        if (self.knowsRumor):
            flip = random.randint(0, 1)
            if(flip == 1):
                return 1
            else:
                return 0
        return 0
    def __str__(self):
        return "Times heard: {0} \t Knows Rumor: {1}".format(self.timesHeard,self.knowsRumor)

#for graphing purposes
known = []
notKnown = []
done = []



minutes = int(sys.argv[1])
if (minutes is None):
    raise Exception("Input N and Minutes. Example: python rumors.py 100 100")

def runSim(N):
    students = []
    lastKnown = 0
    lastKnownCount = 0
    for x in range(N-1):
        students.append(Student(False))
    students.append(Student(True)) #The one student that wants to start a rumor

    for minute in range(minutes):
        #AND BEGIN
        
        #pair students
        pairs = []
        while (len(students) != 0):
            stu1 = random.choice(students)
            students.remove(stu1)
            stu2 = random.choice(students)
            students.remove(stu2)

            pairs.append(Pair(stu1,stu2))

        #Talk and spread rumors
        for pair in pairs:
            if (pair.student1.timesHeard < 2):
                pair.student2.timesHeard += pair.student1.spreadRumor()
            if(pair.student2.timesHeard < 2):
                pair.student1.timesHeard += pair.student2.spreadRumor()

        newList = []
        for pair in pairs:
            newList.append(pair.student1)
            newList.append(pair.student2)
        students = newList

        noneCount = 0
        knownCount = 0
        doneCount = 0
        errorCount = 0
        for x in students:
            if x.timesHeard == 0:
                noneCount = noneCount + 1
            elif x.timesHeard == 1:
                knownCount = knownCount + 1
            elif x.timesHeard >= 2:
                doneCount = doneCount + 1
            else:
                errorCount = errorCount + errorCount
        # print("-------------Minute {0} done-------------".format(minute))
        # print("Students that don't know rumor: {0}".format(noneCount))
        # print("Students that heard rumor once: {0}".format(knownCount))
        # print("Students that heard rumor twice (done spreading): {0}".format(doneCount))
        notKnown.append(noneCount)
        known.append(knownCount)
        done.append(doneCount)
        if(lastKnown == knownCount):
            lastKnownCount += 1
        elif(lastKnown < knownCount):
            lastKnown = knownCount
            lastKnownCount = 0
        if(noneCount == 0):
            print("Rumor fully spread at end of minute {0}. Exiting...".format(minute))
            break
        if(lastKnownCount == 100):
            print("Number of known remained same for past 10 minutes. Currently minute {0}. Exiting...".format(minute))
            break
    return float((knownCount + doneCount)/N)

def runSimPercents(expected):
    students = []
    for x in range(10000-1):
        students.append(Student(False))
    students.append(Student(True)) #The one student that wants to start a rumor
    minute = 0
    percent = 0
    while (expected != percent):
        #AND BEGIN
        
        #pair students
        pairs = []
        while (len(students) != 0):
            stu1 = random.choice(students)
            students.remove(stu1)
            stu2 = random.choice(students)
            students.remove(stu2)

            pairs.append(Pair(stu1,stu2))

        #Talk and spread rumors
        for pair in pairs:
            if (pair.student1.timesHeard < 2):
                pair.student2.timesHeard += pair.student1.spreadRumor()
            if(pair.student2.timesHeard < 2):
                pair.student1.timesHeard += pair.student2.spreadRumor()

        newList = []
        for pair in pairs:
            newList.append(pair.student1)
            newList.append(pair.student2)
        students = newList

        noneCount = 0
        knownCount = 0
        doneCount = 0
        errorCount = 0
        for x in students:
            if x.timesHeard == 0:
                noneCount = noneCount + 1
            elif x.timesHeard == 1:
                knownCount = knownCount + 1
            elif x.timesHeard >= 2:
                doneCount = doneCount + 1
            else:
                errorCount = errorCount + errorCount
        print("-------------Minute {0} done-------------".format(minute))
        print("Students that don't know rumor: {0}".format(noneCount))
        print("Students that heard rumor once: {0}".format(knownCount))
        print("Students that heard rumor twice (done spreading): {0}".format(doneCount))
        notKnown.append(noneCount)
        known.append(knownCount)
        done.append(doneCount)
        minute += 1
        percent = float((knownCount + doneCount)/10000)

    return minute

# averageKnown100 = []
# averageKnown1000 = []
# averageKnown10000 = []

# for x in range(10):
#     averageKnown100.append(runSim(100))
#     averageKnown1000.append(runSim(1000))
#     averageKnown10000.append(runSim(10000))
#     print("Run {0} done".format(x))

# print("Average N=100: %.3f%%" % (((sum(averageKnown100)/10))*100))
# print("Average N=1000: %.3f%%" % (((sum(averageKnown1000)/10))*100))
# print("Average N=10000: %.3f%%" % (((sum(averageKnown10000)/10))*100))


tenPercentTime = runSimPercents(.1)
fiftyPercentTime = runSimPercents(.5)
print("For N=10000")
print("Average time 10% known: {0}".format(tenPercentTime))
print("Average time 50% known: {0}".format(fiftyPercentTime))

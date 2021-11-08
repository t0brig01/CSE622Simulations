import numpy as np
import random
import time
import copy
import matplotlib.pyplot as plt 

random.seed(time.clock())

waitTimes = [[0,4,6,7],
            [4,0,2,3],
            [6,2,0,2],
            [7,2,1,0]]

class Elevator:
    peopleRiding = []
    currectLocation = 0
    destination = None
    waitTime = 0

class Building:
    peopleWaiting = []
    walked = []
    arrived = []
    def __init__(self, elevator):
        self.elevator = elevator

class Person:
    waitTime = 0
    timeGotOnElevator = 0
    tryWalk = False
    def __init__(self, destination):
        self.destination = destination

def runSim():
    record = []
    elevator = Elevator()
    building = Building(elevator)
    waiting830 = 0
    waiting845 = 0
    walkedTo2 = 0
    walkedTo3 = 0
    walkedTo4 = 0
    for quarterMinute in range(240):
        if quarterMinute == 119:
            waiting830 = len(building.peopleWaiting)
        if quarterMinute == 179:
            waiting845 = len(building.peopleWaiting)
        if len(building.peopleWaiting) > 0:
            for x in building.peopleWaiting:
                x.waitTime += 1
        if (quarterMinute % 4 == 0):
            for _ in range(6):
                building.peopleWaiting.append(Person(random.randint(1,3)))
        if building.elevator.currectLocation == 0:
            for x in building.peopleWaiting:
                if building.elevator.waitTime == 0:
                    if len(building.elevator.peopleRiding) == 12:
                        if x.tryWalk == False:
                            if x.destination == 1:
                                if random.random() < .5:
                                    building.walked.append(x)
                                    walkedTo2 += 1
                            elif x.destination == 2:
                                if random.random() < .3:
                                    building.walked.append(x)
                                    walkedTo3 += 1
                            elif x.destination == 3:
                                if random.random() < .1:
                                    building.walked.append(x)
                                    walkedTo4 += 1
                            x.tryWalk == True
                    else:
                        x.timeGotOnElevator = quarterMinute
                        building.elevator.peopleRiding.append(x)
                for x in building.elevator.peopleRiding:
                    if x in building.peopleWaiting:
                        building.peopleWaiting.remove(x)
                for x in building.walked:
                    if x in building.peopleWaiting:
                        building.peopleWaiting.remove(x)
        if building.elevator.waitTime == 0:
            if building.elevator.destination == None:
                if len(building.elevator.peopleRiding) == 0:
                    building.elevator.destination = 0
                    building.elevator.waitTime = waitTimes[building.elevator.currectLocation][0]
                else:
                    nextFloor = 10000
                    for person in building.elevator.peopleRiding:
                        nextFloor = min(person.destination,nextFloor)
                    building.elevator.destination = nextFloor 
                    building.elevator.waitTime = waitTimes[building.elevator.currectLocation][building.elevator.destination]
                    for x in building.elevator.peopleRiding:
                        x.waitTime = waitTimes[building.elevator.currectLocation][building.elevator.destination]
            else:
                building.elevator.currectLocation = building.elevator.destination
                building.elevator.destination = None
                for x in building.elevator.peopleRiding:
                    if x.destination == building.elevator.currectLocation:
                        building.arrived.append(x)
                for x in building.arrived:
                    if x in building.elevator.peopleRiding:
                        building.elevator.peopleRiding.remove(x)
                building.elevator.waitTime = 2
                for x in building.elevator.peopleRiding:
                    x.waitTime += 2


        record.append(copy.deepcopy(building))
        # f.write("Time {0}:{1}".format(int(quarterMinute/4),(15*(quarterMinute%4))))
        # f.write("People waiting: {0}".format(len(building.peopleWaiting)))
        # # f.write("People on elevator: {0}".format(len(building.elevator.peopleRiding)))
        # # f.write("Elevator waitTime: {0}".format(building.elevator.waitTime))
        # f.write("Arrived: {0} \t Walked: {1}".format(len(building.arrived),len(building.walked)))
        building.elevator.waitTime -= 1
    return record, waiting830, waiting845, walkedTo2, walkedTo3, walkedTo4
        

def runSumWithOutputs(epochs):
    print("Outputing to output.txt file")
    f = open("output.txt","w")
    avgWaitTime = []
    secondFloor = []
    thirdFloor = []
    fourthFloor = []
    inLine830 = []
    inLine845 = []
    inLine9 = []
    lastPersonTime = []
    for x in range(epochs):
        print("Run {0}".format(x+1))
        f.write("Run {0}\n".format(x+1))
        record, waiting830, waiting845, walkedTo2, walkedTo3, walkedTo4 = runSim()
        waitTotal = 0
        for x in record[-1].arrived:
            waitTotal += x.waitTime

        f.write("Average wait time: {0}\n".format(waitTotal/len(record[-1].arrived)))
        f.write("Walked to 2nd floor: {0}\n".format(walkedTo2))
        f.write("Walked to 3rd floor: {0}\n".format(walkedTo3))
        f.write("Walked to 4th floor: {0}\n".format(walkedTo4))
        if len(record[-1].elevator.peopleRiding) == 0:
            f.write("No workers on at 9:00 AM\n")
            lastPersonTime.append("No workers")
        else:
            maxTime = 0
            for x in record[-1].elevator.peopleRiding:
                if x.timeGotOnElevator > maxTime:
                    maxTime = x.timeGotOnElevator
            f.write("Time last worker got on: 8:{0}:{1} AM\n".format(int(maxTime/4),(15*(maxTime%4))))
            lastPersonTime.append("8:{0}:{1} AM".format(int(maxTime/4),(15*(maxTime%4))))
        f.write("Workers in line at 8:30 AM: {0}\n".format(waiting830))
        f.write("Workers in line at 8:45 AM: {0}\n".format(waiting845))
        f.write("Workers in line at 9:00 AM: {0}\n\n".format(len(record[239].peopleWaiting)))

        avgWaitTime.append(waitTotal/len(record[-1].arrived))
        secondFloor.append(walkedTo2)
        thirdFloor.append(walkedTo3)
        fourthFloor.append(walkedTo4)
        inLine830.append(waiting830)
        inLine845.append(waiting845)
        inLine9.append(len(record[239].peopleWaiting))

    print("Done")
    print("-----OVERALL AVERAGES-----")
    print("Wait time: {0} mins".format(15*(sum(avgWaitTime)/len(avgWaitTime))))
    print("Walked to second floor: {0}".format(sum(secondFloor)/len(secondFloor)))
    print("Walked to third floor: {0}".format(sum(thirdFloor)/len(thirdFloor)))
    print("Walked to fourth floor: {0}".format(sum(fourthFloor)/len(fourthFloor)))
    print("Waiting at 8:30 AM: {0}".format(sum(inLine830)/len(inLine830)))
    print("Waiting at 8:45 AM: {0}".format(sum(inLine845)/len(inLine845)))
    print("Waiting at 9:00 AM: {0}".format(sum(inLine9)/len(inLine9)))
    print("Last time each day: {0}".format(lastPersonTime))

    f.write("-----OVERALL AVERAGES-----\n")
    f.write("Wait time: {0} mins\n".format(15*(sum(avgWaitTime)/len(avgWaitTime))))
    f.write("Walked to second floor: {0}\n".format(sum(secondFloor)/len(secondFloor)))
    f.write("Walked to third floor: {0}\n".format(sum(thirdFloor)/len(thirdFloor)))
    f.write("Walked to fourth floor: {0}\n".format(sum(fourthFloor)/len(fourthFloor)))
    f.write("Waiting at 8:30 AM: {0}\n".format(sum(inLine830)/len(inLine830)))
    f.write("Waiting at 8:45 AM: {0}\n".format(sum(inLine845)/len(inLine845)))
    f.write("Waiting at 9:00 AM: {0}\n".format(sum(inLine9)/len(inLine9)))
    f.write("Last time each day: {0}\n".format(lastPersonTime))

    f.close()

    plt.title("Average Wait Time")
    plt.plot(avgWaitTime,'-bo')
    plt.show()


runSumWithOutputs(20)
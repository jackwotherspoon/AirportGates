# Author:Jack Wotherspoon
#Created: Nov 15, 2018
import csv
import random
start1=[]
finish1=[]
start2=[]
finish2=[]
delay1=0.25
delay2=0.50
delay3=0.75
delay4=1.00
def readFile(fileName):
    with open(fileName,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        if fileName=='start1.csv':
            for row in csv_reader:
                start1.append(float(row[0]))
        if fileName=='finish1.csv':
            for row in csv_reader:
                finish1.append(float(row[0]))
        if fileName=='start2.csv':
            for row in csv_reader:
                start2.append(float(row[0]))
        if fileName=='finish2.csv':
            for row in csv_reader:
                finish2.append(float(row[0]))
def gatesNeeded(start,finish):
    gate=0
    count=[]
    for i in range(0,(len(start)-1)):
        #make list of departure times and sort
        count.append(finish[i])
        count.sort()
        #if the start time of incoming plane is greater than oldest departure time, thus we can delete that plane from list and give current plane its gate
        if count[0]<start[i]:
            del count[0]
        #if all gates still have planes then we must create a new gate
        else:
            gate+=1
    return gate
def delayPlanes(start,finish,startDelays,finishDelays,delay):
    randIndices=random.sample(range(0,(len(start)-1)),startDelays)
    randIndices1=random.sample(range(0,(len(finish)-1)),finishDelays)
    # USE IF WE NEED TO GENERATE RANDOM NUMBER OF DELAYS OTHERWISE KEEP IT MANUAL
    #startDelays=random.randint(0,(len(start)-1))
    #finishDelays = random.randint(0,(len(finish) - 1))
   # for i in range(0,startDelays):
    #    randIndices=random.sample(range(1,(len(start)-1)),startDelays)
    #for i in range(0,finishDelays):
    #    randIndices1=random.sample(range(1,(len(finish)-1)),finishDelays)
    print("The number of arrival times delayed is ", len(randIndices), " and departure times delayed is ",len(randIndices1), ", so total delays is ",(len(randIndices)+len(randIndices1)))
    for i in randIndices:
        start[i]+=delay
        if start[i] > finish[i]:
            finish[i] = start[i] + 0.5  #half hour buffer between arrival and departure of plane
    for i in randIndices1:
        finish[i]+=delay

readFile("start1.csv")
readFile("start2.csv")
readFile("finish1.csv")
readFile("finish2.csv")
print ("--------PART 1----------")
print("The total number of gates needed for data set 1 is :", gatesNeeded(start1,finish1))
print("The total number of gates needed for data set 2 is : ",gatesNeeded(start2,finish2))
print("---------PART 2-------------")
#play around with the number of arrival delays and departure delays which are the 100's and change delay time to see impact.
delayPlanes(start1,finish1,100, 100,delay1)
print("Number of gates needed is:",gatesNeeded(start1,finish1))




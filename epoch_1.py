import random
import time
def getRandomDate(StartDate, EndDate):
    print("printing random date between", StartDate, "and", EndDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'
    startTime = time.mktime(time.strptime(StartDate, dateFormat))
    endTime = time.mktime(time.strptime(StartDate, dateFormat))
    randomTime = startTime + randomGenerator()
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("random date = ", getRandomDate("2/13/2014" , "5/6/2026"))
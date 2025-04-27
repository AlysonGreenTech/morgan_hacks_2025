import random
import time

def getInternalHumidity():
    random.seed(time.time())
    return random.randint(60,70)

def getInternalTemp():
    random.seed(time.time())
    return random.randint(80,99)

def getExternalHumidity():
    random.seed(time.time())
    return random.randint(60,70)

def getExternalTemp():
    random.seed(time.time())
    return random.randint(80,99)

def getVoltage(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return random.randint(12,13)




import random
import time

def getIMU(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

def getMotion(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return random.randint(0, 1)
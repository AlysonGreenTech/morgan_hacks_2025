class PayloadArm:
    def __init__(self, base=0, lin_act=0, yaw=0, pitch=0):
        # Initialize the payload arm
        self.Base = base
        self.LinAct = lin_act
        self.Yaw = yaw
        self.Pitch = pitch

    def setPosition(self, base=None, lin_act=None, yaw=None, pitch=None):
        # Set the position of the payload arm
        if base is not None:
            self.Base = base
        if lin_act is not None:
            self.LinAct = lin_act
        if yaw is not None:
            self.Yaw = yaw
        if pitch is not None:
            self.Pitch = pitch

    def getPosition(self):
        # Get the position of the payload arm
        return {
            "Base": self.Base,
            "LinAct": self.LinAct,
            "Yaw": self.Yaw,
            "Pitch": self.Pitch
        }
    
    def deploy(self):
        print("Deploying payload arm")
        # Code to deploy payload arm
    
    def close(self):
        print("Closing payload arm")
        # Code to close payload arm

# Create an instance of the PayloadArm class
starveArm = PayloadArm(0, 0, 0, 0)

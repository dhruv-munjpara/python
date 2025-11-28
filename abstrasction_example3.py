class car:
    def __init__(self):
        self.accelerator = False
        self.breaks = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car Started..")

c1 = car()
c1.start()

# Abstraction means Hiding Irrelevent data from users or Hiding Main details from Users

class Car():
        def __init__(self):
            self.acc=False
            self.brk=False
            self.clutch=False

        def start(self):
            self.clutch=True
            self.acc=True
            print("Car is Started...")

car1=Car()
car1.start()
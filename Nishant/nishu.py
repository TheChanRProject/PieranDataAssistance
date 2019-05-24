class Nishant():

    def __init__(self) :
        self.message = input("Type in a message for Nishant to say: ")

    def greeting (self):
        return "Nishant says " + self.message

nishu = Nishant()
print(nishu.greeting())

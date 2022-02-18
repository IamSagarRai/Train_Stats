for i in range(3):
    pass


class train:
    def __init__(self, name, fare, seats, code):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.code = code

    def train_Status(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats is {self. seats}")

    def fare_Info(self):
        print(f"The fare is {self. fare}")

    def code_Info(self):
        print(f"The code is {self. code}")

    def tickets_Info(self):
        if(self.seats > 0):
            print(
                f"The seats are available for you...\nYour seat number is {self.seats}")
            self.seats = self.seats - 1
        elif(self.seats == 0):
            print("The seats are not available for you...")
        else:
            print("The server isnt updated yet. \nPlease try again later.")

    @staticmethod
    def greeting():
        print("Welcome to Rajdhani express!!")


Inter = train("Inter Express", 180, 12, 239340)
Inter.greeting()
Inter.fare_Info()
Inter.train_Status()
Inter.tickets_Info()
Inter.train_Status()
Inter.code_Info()

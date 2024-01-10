from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    # pass

toyota=Car(2, 5)
# print(toyota.go(), toyota.fill_up_tank())
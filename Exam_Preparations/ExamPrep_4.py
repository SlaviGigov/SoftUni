class Car:

    def __init__(self, name, km, fuel):
        self.name = name
        self.km = km
        self.fuel = fuel

    def Drive(self, distance, fuel):
        if self.fuel < fuel:
            return print(f"Not enough fuel to make that ride")
        elif self.fuel >= fuel:
            self.km += distance
            self.fuel -= fuel
            return print(f"{self.name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if self.km >= 100000:
            del cars[self.name]
            return print(f"Time to sell the {self.name}!")

    def Refuel(self, fuel):
        if self.fuel + fuel > 75:
            fuel = 75 - self.fuel
            self.fuel = 75
        else:
            self.fuel += fuel
        return print(f"{self.name} refueled with {fuel} liters")

    def Revert(self, km):
        if self.km - km <= 10000:
            self.km = 10000
        else:
            self.km -= km
            return print(f"{self.name} mileage decreased by {km} kilometers")

cars = {}

for n in range(int(input())):
    name, km, fuel = input().split("|")
    cars[name] = int(km), int(fuel)

do = input()
while not do == "Stop":
    command = do.split(" : ")
    car = Car(command[1], cars[command[1]][0], cars[command[1]][1])
    if command[0] == "Drive":
        car.Drive(int(command[2]),int(command[3]))
    elif command[0] == "Refuel":
        car.Refuel(int(command[2]))
    elif command[0] == "Revert":
        car.Revert(int(command[2]))
    do = input()

sorted_cars = sorted(cars.items(), key = lambda x:(-x[1][0],x[0]))
for car in sorted_cars:
    print(f"{car[0]} -> Mileage: {car[1][0]} kms, Fuel in the tank: {car[1][1]} lt.")

# Not correct - the dictionary cars is not updated durring the commands. Tried with Class
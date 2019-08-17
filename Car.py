import math
class car:
    def __init__(self, speed = 0, mass = 1, miu = 0, slope = 0): 
        self.speed = speed
        self.mass = mass
        self.miu = miu
        self.slope = slope
        self.distance = 0
        self.time = 0 
    def state(self): 
        print("The car is {} kilograms heavy".format(self.mass))
        print("The angle of the slope is {} degrees".format(self.slope))
        print("The car is going {} kilometers per hour!".format(self.speed))
        print("It has driven {} kilometers".format(self.distance))
    def travel(self, time_interval): 
        self.time += time_interval
        self.distance += time_interval * self.speed
    def exert(self, force): 
        total_friction = force * self.miu + 9.8 * math.sin(math.radians(self.slope)) * self.mass
        combined_force = force - total_friction
        acceleration = combined_force / self.mass
        return acceleration
    def accelerate(self, acceleration, time_interval):
        self.time += time_interval
        self.distance += self.speed * time_interval + 0.5 * acceleration * time_interval * time_interval
        self.speed += acceleration * time_interval
    def brake(self, deceleration, time_interval): 
        self.time += time_interval
        if (self.speed >= deceleration * time_interval):
            self.distance += self.speed * time_interval - 0.5 * deceleration * time_interval * time_interval
            self.speed = self.speed - deceleration * time_interval
        else: 
            effective_time = self.speed / deceleration 
            self.distance += 0.5* self.speed * effective_time
            self.speed = 0
    def average_speed(self):
        if self.time == 0: 
            pass
        else: 
            return self.distance / self.time 
    def refresh(self):
        self.time = 0
        self.speed = 0
        self.distance = 0

if __name__ == '__main__':
    Porsche = car()
    print('This is a new car!')
    while True: 
        action = input("What to do? [S]Setup, [A]Travel, [B]Accerlate, [C]Brake, [D]Show Distance, [E]Show Speed?, [F]Refresh, [G]Exert Force. Your choice: ").upper()
        if action not in 'SABCDEFG' or len(action) != 1: 
            print("Wrong input! Try Again!")
            continue
        if action == 'S': 
            Porsche.mass = float(input("How heavy is the car? "))
            Porsche.miu = float(input("What is the friction coefficient? "))
            Porsche.slope = float(input("What is the angle of the slope? "))
        if action == 'A':
            time_interval = float(input("Enter time interval: "))
            Porsche.travel(time_interval)
        if action == "B": 
            acceleration = int(input("Enter acceleration: "))
            time_interval = float(input("Enter time interval: "))
            Porsche.accelerate(acceleration, time_interval)
        if action == 'C':
            deceleration = int(input("Enter deceleration: "))
            time_interval = float(input("Enter time interval: "))
            Porsche.brake(deceleration, time_interval)
        if action == 'D':
            print("The car has driven {} kilometers.".format(Porsche.distance))
        if action == 'E': 
            print("The car's average speed is {} kilometers per hour.".format(Porsche.average_speed()))
        if action == 'F':
            print("This car has been refreshed. Everything will start over.")
            Porsche.refresh()
        if action == 'G':
            force = float(input("With how much force is the car driven? "))
            time_interval = float(input("Enter time interval: "))
            acceleration = Porsche.exert(force)
            Porsche.accelerate(acceleration, time_interval)
        Porsche.state()
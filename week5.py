from datetime import datetime

# Activity 1: Class with Inheritance and Encapsulation

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self._battery_life = battery_life  # Encapsulated attribute

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def battery_status(self):
        print(f"Battery life: {self._battery_life}%")

    def charge(self, amount):
        self._battery_life = min(100, self._battery_life + amount)
        print(f"Charged! Battery life is now {self._battery_life}%")

class Smartwatch(Smartphone):  # Inheritance
    def __init__(self, brand, model, battery_life, strap_color):
        super().__init__(brand, model, battery_life)
        self.strap_color = strap_color

    def show_time(self):
        print(f"Current time: {datetime.now().strftime('%H:%M:%S')}")

# Example usage:
phone = Smartphone("Apple", "iPhone 14", 80)
watch = Smartwatch("Samsung", "Galaxy Watch", 60, "Black")

phone.call("123-456-7890")
phone.battery_status()
watch.show_time()
watch.charge(30)

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Polymorphism in action
vehicles = [Car(), Plane(), Bicycle()]
for v in vehicles:
    v.move()
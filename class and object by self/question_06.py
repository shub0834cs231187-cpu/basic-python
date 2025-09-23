## 6. Car — Start and Stop

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.brand} started.")

    def stop(self):
        self.is_running = False
        print(f"{self.brand} stopped.")

car = Car("Toyota")
car.start()
car.stop()

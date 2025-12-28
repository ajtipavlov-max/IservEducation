# class Cat:
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed
    
#     def printInfo(self):
#         print("="*10)
#         print(f"имя : {self.name}")
#         print(f"Цвет : {self.color}")
#         print(f"Порода: {self.breed} ")
#         print("="*10)


class Car:
    def __init__(self, name, color, powerd):
        self.name = name
        self.color = color
        self.powerd = powerd
        self.mileage = 0 
        self.is_running= False
    
    def printInfo(self):
        print("="*10)
        print(f"марка : {self.name}")
        print(f"Цвет : {self.color}")
        print(f"Пробег: {self.powerd} ")
        print("="*10)
    def start_engine(self):
        if self.is_running:
            print("Двигатель уже заведен!")
            return
        self.is_running = True
        print("Двигатель запущен")

        



from car import *

# cat1 = Cat("Барсик","Черный" , "шотланд")
# cat2 = Cat("Мурзик", "белый", "сфинкс")
# print("мяу")
# cat1.printInfo()
# cat2.printInfo()


car1 = Car("КИО РИО","Черный" , 250)
car2 = Car("ЛАДА ГРАНТА", "белый", 350)

car1.printInfo()
car2.printInfo()



car1 =Car("КИО РИО","Черный" , 250)

car1.printInfo()

name = getattr(car1,"name")
print(name)

setattr(car1,"color","белый")
















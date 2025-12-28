from animals import *

def info(object):
    object.printInfo()

def animalSpeak(obgect):
    object.speak()

cat = Cat("Гав",3,"Бенгальская")
dog = Dog("Вайти",1,"БШО")
newcat =HomeCat("Муся",4,"Сибирская", "Рыжая","Пуша")

newcat.printInfo()
info(cat)
info(dog)


print(cat.__name)
print(dog.__name)
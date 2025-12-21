# print("Результат остаточного деления 435 на 23 = {435 % 23}")
# print("Результат остаточного деления 543 на 245 = {543 % 245}")
# print("Результат остаточного деления 400 на 20 = {400 % 20}")

# myAge= int(input("Введите ваш возраст:"))

# if(myAge < 18):
#     print("Вы не совершенолетний!")

# else:
#     print("Вы совершенолетний!")

# myAge= int(input("Введите ваш возраст:"))

# if (myAge<6):
#     print ("Вы ребенок")
# elif (myAge<20):
#     print ("Вы подросток")
# elif :
#     print ("Вы уже взрослый")


# myBy= int(input("Введите ваш бюджет:"))

# if(myBy < 100):
#     print("Вам не хватает!,выбирайте другую книгу!")
# else:
#         print("Поздравляем!Оформляем покупку!")

current_year = 2025
current_month = 12
current_day = 31

birth_year =  int(input(" введите ваш год рождения: "))
birth_month =  int(input(" введите ваш месяц рождения: "))
birth_day =  int(input(" введите ваш день  рождения: "))
age = current_year - birth_year 
if(current_month>birth_month ):
  print("Вам ",age, "лет")
elif(current_month==birth_month ):
  if (current_day>=birth_day):
       print("Вам ",age, "лет")
  else:
     print("Вам ",age-1, "лет")
else:
  print("Вам ",age-1, "лет")



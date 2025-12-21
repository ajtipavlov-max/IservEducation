# это мой конспект


## приобразования типов:
```
print(type(55), "->" , type(str(55)))
print(type(432), "->" , type(float(432)))
print(type(6.44), "->" , type(int (6.44)))
```

## Определитель возраста :
```
current_year = 2025

birth_year =  int(input(" введите ваш год рождения: "))

print("Вам ",current_year-birth_year, "лет")
``` 

##Операторы сравнения :

```
'>','>=','<','<=','==','!='
```

##Деление
```
print("Результат остаточного деления 435 на 23 = {435 % 23}")
print("Результат остаточного деления 543 на 245 = {543 % 245}")
print("Результат остаточного деления 400 на 20 = {400 % 20}")
```

##  Несовершенолетний :
```
myAge= int(input("Введите ваш возраст:"))

if(myAge < 18):
    print("Вы не совершенолетний!")
    ```

## Вы ребенок:

```
 myAge= int(input("Введите ваш возраст:"))
if (myAge<6):
    print ("Вы ребенок")
elif (myAge<20):
    print ("Вы подросток")
else :
    print ("Вы уже взрослый")
```


###  Покупка книги :
```
myBy= int(input("Введите ваш бюджет:"))

if(myBy < 100):
    print("Вам не хватает!,выбирайте другую книгу!")
else:
        print("Поздравляем!Оформляем покупку!")
   ```



       
## Строки с числами которые не делятся на 3 и 5 :

```
for i  in  range(1,101):
    if i % 3 != 0 and i % 5 != 0:
        print (i, end = " ")
```


## Задача :
```
 задача 4

 summa = 0
 N = int(input("Ведите число:"))

 for  i in range ("1 ,N = 1"):
     summa += 1
     print (summa)

```



## Ваш возраст:
`````
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
```





### ИНДЕКСЫ
```
st = "Мы используем индексы в этот примере "
 print (st[-1])
 print (st[-7:-1])
 print (st[:-13])
 print (st[-13:])
 print (st[::-1])

ЗАДАЧА
st = "Тот кто владеет  информацией ,тот владеет миром!"
 len_st = len(st)
 new_st1 = st.title()
 new_st2 = st.replace("Иформацией","puthon")
 new_st3 = st.upper()
 count_o = st.count("о")
```







### Произведение суммы чисел
```
proizNum = 1
userInput = 1

while userInput != 0: 
   print ("Введите 0 чтобы остановить программу") 
   userInput = int (input("Или введите ваше число"))

   print ("Произведение ваших чисел равно :", proizNum)
   ```



### Полиндром:
```
st = input()
if (st[::-1] ==st):
    print ("это палиндром")
```


## Задача список фруктов 
```fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1,"lemon")
fruits.remove("banana")
print (fruits)
```

## Смайлик
```
import turtle

screen = turtle. Screen()
screen.setup(600,600)
screen.bgcolor

t = turtle.Turtle()

t.penup()
t.goto(0, -100)
t.pendown()
t.color("black","yellow")
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black","white")
t.begin_fill()
t.circle(20)
t.end_fill()


t.penup()
t.goto(-40, 40)
t.pendown()
t.color("black","black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 30)
t.pendown()
t.color("black","white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(40, 40)
t.pendown()
t.color("black","black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-60, -20)
t.pendown()
t.color("black")
t.width(5)
t.setheading(-60)
t.circle(70,120)

```
 return\


 ## Пароль

 ```
 import random
import string

def password_generatoin(lenPas,iSnums,isUpAlpha):
    symbols = string.ascii_lowercase
    password = ''
    if isUpAlpha:
        symbols+= string.ascii_uppercase
    if iSnums:
        symbols+='1234567890'
    for _ in range(lenPas):
        password += random.choice(symbols)
    return password


print (password_generatoin(8,True,True))

```

````
def  SumDigitsOfNumber(number):
    strNumber = str(number)
    summa = 0 
    for i in strNumber:
     summa += int(i)
    return(summa)

print (SumDigitsOfNumber(456))


def CountWovelsSumbols(word):
    wovelsSumbuls = "аеуёиоыэюя"
    count = 0 
    for sym  in  wovelsSumbuls :
        count += word.count(sum)

    return count 
```



### Tkinter-библиотека позволяющая создовать графический интерфейс
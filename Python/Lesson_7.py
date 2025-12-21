# import random
# import string

# def password_generatoin(lenPas,iSnums,isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ''
#     if isUpAlpha:
#         symbols+= string.ascii_uppercase
#     if iSnums:
#         symbols+='1234567890'
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password


# print (password_generatoin(8,True,True))


# def isEven(number):
#     if number % 2 == 0 :
#       return    True
#     else :
#        return False
    
# def CountWovelsSumbols(word):
#     wovelsSumbuls = "аеуёиоыэюя"
#     count = 0 
#     for sym  in  wovelsSumbuls :
#         count += word.count(sum)

#     return count


# def  SumDigitsOfNumber(number):
#     strNumber = str(number)
#     summa = 0 
#     for i in strNumber:
#      summa += int(i)
#     return(summa)

# print (SumDigitsOfNumber(456))
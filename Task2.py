#Условная конструкция. Операторы if, elif, else.
a = input('First: ')
b = input('Second: ')
c = input('Third: ')
x = 0
if a == b == c:
    x = 3
elif a == b:
    x = 2
elif b == c:
    x = 2
print (x)
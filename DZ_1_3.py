#Даны три числа a, b и c. Найти среднее геометрическое этих чисел,
# если все они отличны от нуля, и среднее арифметическое в противном случае.

a = float(input("Введите первое целое число: \n"))
b = float(input("Введите второе целое число: \n"))
c = float(input("Введите третье целое число: \n"))

if a!=0 and b!=0 and c!=0:
    z=(a*b*c)**(1./3.)
else:
    z=(a+b+c)/3.

print(str(z))
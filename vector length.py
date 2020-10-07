# #3
# Напишите функцию на языке “Python” реализующую нахождение длины вектора произвольной размерности.
import math

def length(vector):
    result =0
    for item in vector:
        result += item**2
    return math.sqrt(result)

vector=[]

x = int(input("Введите координату x "))
y = int(input("Введите координату y "))
z = int(input("Введите координату z "))

vector.append(x)
vector.append(y)
vector.append(z)

result = length(vector)
print("Длина вектора равна", result)

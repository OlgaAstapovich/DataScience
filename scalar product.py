# №2
# Напишите функцию на языке “Python” реализующую скалярное произведение
# двух векторов произвольной размерности.

def scalar_product(list1,list2, n):
    result = 0
    for i in range(n):
        result += list1[i]*list2[i]
    return result

vector1 = []
vector2 = []
result = 0

dimension = int(input("Введите размерность векторов "))

for i in range(dimension):
    data = int(input("Введите {} элемент 1-го вектора ".format(i+1)))
    vector1.append(data)

for i in range(dimension):
    data = int(input("Введите {} элемент 2-го вектора ".format(i+1)))
    vector2.append(data)

result = scalar_product(vector1,vector2,dimension)

print("Скалярное произведение данных векторов равно", result)
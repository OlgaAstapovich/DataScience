# №1
# Напишите функцию на языке “Python” получающую на вход численные значения
# некоторой случайной величины и вероятности их появления,
# а возвращающую – ее математическое ожидание и дисперсию.

def math_expectation_and_variance(list_x, list_p, n):
    math_expectation = 0
    math_expectation_x2 = 0
    variance = 0
    for i in range(n):
        math_expectation += list_x[i] * list_p[i]
        math_expectation_x2 += (list_x[i] ** 2) * list_p[i]
    variance = math_expectation_x2 - (math_expectation ** 2)
    return math_expectation, variance


def math_expectation_and_variance(list_x, list_p):
    math_expectation = 0
    math_expectation_x2 = 0
    variance = 0
    j = 0
    for i in list_x:
        j += 1
    for i in range(j):
        math_expectation += list_x[i] * list_p[i]
        math_expectation_x2 += (list_x[i] ** 2) * list_p[i]
    variance = math_expectation_x2 - (math_expectation ** 2)
    return math_expectation, variance


X = []
P = []

n = int(input("Input value"))

print("Input numericals and their probabilities in range (0;1)")
for i in range(n):
    X.append(int(input("{} numerical ".format(i + 1))))
    p = float(input("its probality "))
    while (p <= 0 or p >= 1):
        p = float(input("Input probability in range (0;1)"))
    P.append(p)

math_expectation, variance = math_expectation_and_variance(X, P, n)

print("Mathematical expectation is {}, variance is {}".format(math_expectation, variance))

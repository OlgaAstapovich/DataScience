import math

n = int(input("Введите количество подбрасываний "))

m = int(input("Введите желаемое количество выпадений "))

s = int(input("Введите границу "))

c = (math.factorial(n)) / ((math.factorial(m)) * (math.factorial(n - m)))
p = ((6 - (s - 1)) / 6)
q = (1 - p)
result = c * (p**m) *(q**(n-m))
print(result)

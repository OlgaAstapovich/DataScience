# №7
# Напишите программу на языке “Python” нахождения количества N значных чисел делящихся на m.
# Ограничение на время ее выполнения для 4-х значных чисел не более 4 сек.

N = int(input("введите разрядность "))
m = int(input("введите делитель "))

number_of_digits_of_the_specified_bit_depth = 0
number_of_digits_with_a_bit_depth_less_than_the_specified_one_by_1 = 0

for n in range(N):
    number_of_digits_of_the_specified_bit_depth += 9 * (10 ** n)

for n in range(N - 1):
    number_of_digits_with_a_bit_depth_less_than_the_specified_one_by_1 += 9 * (10 ** n)

result = (number_of_digits_of_the_specified_bit_depth // m) - (
        number_of_digits_with_a_bit_depth_less_than_the_specified_one_by_1 // m)

print("Количество {}-значных чисел делящихся на {} равно {}".format(N, m, result))

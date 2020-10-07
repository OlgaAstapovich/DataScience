# №5
# Напишите функцию на языке “Python” нахождения определителя матрицы размерностью 4Х4.

def det_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det_3(matrix):
    matrix1, matrix2, matrix3 = [], [], []
    for i in range(1, 3):
        matrix1.append(matrix[i][1:3])
        matrix2.append(matrix[i][0:1] + matrix[i][2:3])
        matrix3.append(matrix[i][0:2])
    return matrix[0][0] * det_2(matrix1) - matrix[0][1] * det_2(matrix2) + matrix[0][2] * det_2(matrix3)


def det_4(matrix):
    matrix1, matrix2, matrix3, matrix4 = [], [], [], []
    for i in range(1, 4):
        matrix1.append(matrix[i][1:4])
        matrix2.append(matrix[i][0:1] + matrix[i][2:4])
        matrix3.append(matrix[i][0:2] + matrix[i][3:4])
        matrix4.append(matrix[i][0:3])
    return matrix[0][0] * det_3(matrix1) - matrix[0][1] * det_3(matrix2) + \
           matrix[0][2] * det_3(matrix3) - matrix[0][3] * det_3(matrix4)


matrix = [[4, 2, 2, 5],
          [5, 2, 1, 2],
          [8, 9, 5, 3],
          [1, 2, 3, 4]]
print(det_4(matrix))
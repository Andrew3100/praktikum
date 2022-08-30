import random as r

# функция возвращает случайную матрицу квадратов случайных элементов кортежа
def get_matrix(cortage):
    count = len(cortage)
    matrix = []
    for i in range(0, count):
        string = []
        for g in range(0, count):
            rand_element = cortage[r.randint(0, len(cortage) - 1)]
            string.append(rand_element**2)
        matrix.append(string)
    return matrix


# функция пишет матрицу и сумму диагонали в файл
def write_data_in_file(matrix):
    sum = 0
    length = len(matrix)
    my_file = open("Scriptdata.txt", "w+")
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[i]) - 1):
            if i == j:
                sum += matrix[i][j] * length
            content = str(matrix[i][j] * length) + " "
            my_file.write(content)
            # пишем в строку матрицу, умноженную на её порядок
        my_file.write("\n")
    my_file.write("\nThe sum of the diagonal elements of the matrix is " + str(sum))
    my_file.close()


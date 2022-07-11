import time

from datetime import timedelta
start_time = time.perf_counter()

import random
class Matrix:
    def __init__(self, lines, column):
        self.lines = lines
        self.column = column
        self.matrix = self.construction()

    def construction(self):
        matrix = [[ random.randint(1,5) for i in range(self.column)] for a in range(self.lines)]
        return matrix

    def construction1(self):
        matrix = [[0 for a in range(self.lines)] for i in range(self.column)]
        return matrix


    def multiplication(self, mnogitel):
        matrix_s = [rw[:] for rw in self.matrix.copy()]
        for k in range(self.lines):
            for p in range(self.column):
                matrix_s[p][k] = self.matrix_s[p][k] * mnogitel
        return matrix_s

    def upheaval(self):
        matrix_a = [rw[:] for rw in self.matrix1.copy()]
        matrix_b = [[0 for l in range(self.column)] for i in range(self.lines)]
        for i in range(len(matrix_a)):
            for a in range(len(matrix_a[0])):
                matrix_b[i][a] = matrix_a[a][i]
        return matrix_b

    def addition(self, matrixa):
        matrix_a = [rw[:] for rw in self.matrix.copy()]
        if len(matrix_a) == len(matrixa) and len(matrix_a[0]) == len(matrixa[0]):
            for i in range(len(matrix_a)):
                for a in range(len(matrix_a[0])):
                    matrix_a[i][a] = matrixa[a][i]
            return matrix_a

    def subtraction(self, matrixa):
        matrix_a = [rw[:] for rw in self.matrix.copy()]
        if len(matrix_a) == len(matrixa) and len(matrix_1[0]) == len(matrixa[0]):
            for i in range(len(matrix_a)):
                for a in range(len(matrix_a[0])):
                    matrix_a[i][a] = matrixa[a][i]
            return matrix_a



    def multiplication_matr(self, matrixa):
        matrix_a= [rw[:] for rw in self.matrix.copy()]
        matrixa = [rw[:] for rw in matrixa]
        matrix_b = [[0 for i in range(len(matrixa[0]))] for a in range(self.lines)]
        if len(matrix_a[0]) == len(matrixa):
            count = 0
            for n in range(len(matrix_a)):
                t = 0
                for b in range(len(matrixa[0])):
                    for c in range(len(matrixa)):
                        t += matrix_a[n][c] * matrixa[c][b]


                    if count == len(matrix_a[0]):
                        count = 0
                    matrix_b[n][b] = t
                    t = 0
                count += 1
            return matrix_b

def ex_matr(matrix_a):
    for rw in matrix_a.matrix:
        for z in rw:
            print("{:4d}". format(z), end=" ")
        print()

def ex_matr2(matrix_a):
    for rw in matrix_a:
        for z in rw:
            print("{:4d}". format(z), end=" ")
        print()


nomer_1 = Matrix(100, 100)
nomer_2 = Matrix(100, 100)
nomer_1.subtraction(nomer_2)
print(nomer_1.matrix)
ex_matr(nomer_1)
print()
x = [[3], [4]]
ex_matr(nomer_2)
print()


ex_matr2(nomer_1.multiplication_matr(nomer_2.matrix))
end_time = time.perf_counter()
print(timedelta(end_time - start_time))


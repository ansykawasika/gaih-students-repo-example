import random
matrix = []
matrix1 = []
matrix2 = []
matrix3 = []

while len(matrix) < 9:                      # 9 asal elemanli dizi oluştur
    rasgele = random.randint(0,100)         # 0-100 arası rasgele sayi sec
    if rasgele > 1:
        for i in range(2,rasgele):
            if (rasgele % i) == 0:
                break
        else:
            matrix.append(rasgele)

matrix1 = matrix[0:3]                       # 3 luk parcalara ayir
matrix2 = matrix[3:6]
matrix3 = matrix[6:9]
matrix = [matrix1] + [matrix2] + [matrix3]  # 3x3 luk matrix olustur

for i in matrix:
    print(i)
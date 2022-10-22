import math

# Read the number of testcases
T = int(input())

# Process each test case
for t in range(T):
    line = input().split()
    N = int(line[0])
    lista = []

    for n in range(N):
        a = int(line[n + 1]) # El último no existe
        # print(a)
        if a >= 360:
            i = math.floor(a / 360)
            a = a - i * 360

        if a <= -360:
            i = abs(math.floor(a / 360))
            a = a + i * 360

        if -360 < a <= -180:
            a = a + 360

        if a > 180:
            if (a - 180) not in lista:
                lista.append(a - 180)
        if a < 0:
            if (a + 180) not in lista:
                lista.append(a + 180)

        if 0 <= a <= 180: # 0 y 180 són equivalentes
            if a not in lista:
                lista.append(a)

    trozos = len(lista) * 2
    if trozos == 0:
        trozos = 1
    print(trozos)
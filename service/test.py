from time import sleep
from random import randint
import numpy as np

N, M = 10, 10 # field size
Chromosoms = 4
Area = np.array([['_' for _ in range(M)] for _ in range(N)])
Outgrowthes = []

# up down left right
#Genom = np.array([[randint(0, Chromosoms * 2) for _ in range(4)] for _ in range(Chromosoms)])
Genom = np.array(
        [[2, 0, 4, 6],
         [4, 4, 6, 7],
         [5, 8, 0, 7],
         [0, 5, 7, 3]])
print(Genom)
print()
print(Area)

Area[N - 1, M // 2] = '0'
Outgrowthes.append([N - 1, M // 2])
print()
print(Area)

while Outgrowthes:
    for i, (y, x) in enumerate(Outgrowthes):
        genom_num = int(Area[y, x])
        new_outgrowthes = Genom[genom_num]
        print(new_outgrowthes)
        if y > 0 and new_outgrowthes[0] < Chromosoms and Area[y - 1, x] != '*':
            Area[y - 1, x] = str(new_outgrowthes[0])
            Outgrowthes.append([y - 1, x])
        if y < N - 1 and new_outgrowthes[1] < Chromosoms and Area[y + 1, x] != '*':
            Area[y + 1, x] = str(new_outgrowthes[1])
            Outgrowthes.append([y + 1, x])
        if x > 0 and new_outgrowthes[2] < Chromosoms and Area[y, x - 1] != '*':
            Area[y, x - 1] = str(new_outgrowthes[2])
            Outgrowthes.append([y, x - 1])
        if x < N - 1 and new_outgrowthes[3] < Chromosoms and Area[y, x + 1] != '*':
            Area[y, x + 1] = str(new_outgrowthes[3])
            Outgrowthes.append([y, x + 1])
        del Outgrowthes[i]
        Area[y, x] = '*'

        print()
        print(Area)
        sleep(0.5)

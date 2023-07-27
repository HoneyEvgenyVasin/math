import random

costs = [
    [1, -1, -1, 1],
    [-1, 3, 4, -1],
    [-1, -1, 7, 12],
    [-1, -1, -1, 0]
]

rows = 4
cols = 4

count = rows + cols
n_cycle = 0

u = [[0, False] for i in range(0, cols)]
v = [[0, False] for i in range(0, rows)]
print(u[0][1])
#    0 - значение 1 - вычислен или нет
u[0][0] = 0
u[0][1] = True

print("Матрица тарифов", costs)
print("вектор u до вычисления", u)
print("вектор v до вычисления", v)

while count > 1:
    while True:
        n_cycle = n_cycle + 1

        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if costs[r][c] == -1:
            continue
        if (u[r][1] or v[c][1]) == True and (u[r][1] != v[c][1]):
            break
    print("{0} Подходящяя ячейка {1}:{2} ==> U:{3} xor V:{4}".format(count, r, c, u[c], v[r]))

    if u[r][1] == True:
        v[c][0] = costs[r][c] - u[r][0]
        v[c][1] = True
    else:
        u[r][0] = costs[r][c] - v[c][0]
        u[r][1] = True
    
    count = count - 1

print("Рассчитаный вектор u", u)
print("Рассчитаный вектор v", v)
print("Расчет выполнен за {0} циклов".format(n_cycle))
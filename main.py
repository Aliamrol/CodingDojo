r1 = [0]*8
r2 = [0]*8
r1[1] = 0
r1[2] = 1
r1[3] = 0
n = 5

for i in range(1, n+1):
    for j in range(1, 2*(n-i)+1):
        print(' ', end='')
    for j in range(2, i+2):
        print(f'{r1[j]:4}', end='')
    print('\n')
    r2[1] = 0
    for j in range(2, i+3):
        r2[j] = r1[j-1] + r1[j]
    r2[i+3] = 0
    for j in range(1, i+4):
        r1[j] = r2[j]


for i in range(0, 8):
    print(r1[i], r2[i])
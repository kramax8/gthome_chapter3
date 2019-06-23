# Минимальное положительное число
a = [1,2,3,4,6]
b = [1,2,3]
c = [-1, -2, -6]

d = [22, 23, 14, 6, 4, 1, 2, 3, 5]
d.sort()
min_num = 1 

for e in d:
    if e < min_num and e > 0:
        min_num = e
    elif e == min_num:
        min_num += 1
    elif e < 0:
        min_num = 1

print(min_num)


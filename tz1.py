user_str = input('Введите текст... ')

sum_up = 0

sum_low = 0

for i in user_str:
    if i.isupper():
        sum_up += 1
    else:
        sum_low += 1

result = 'Количество букв: ' + str(len(user_str)) + '\n'
result += str(int(sum_up * 100 / len(user_str))) + '% в верхнем регистере' + '\n'
result += str(int(sum_low * 100 / len(user_str))) + '% в нижнем регистере' + '\n'


print(result)


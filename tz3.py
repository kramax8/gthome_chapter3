user_list = list(input('Введите слова через пробел... ').split(' '))
user_num = int(input('Ведите значение сдвига... '))

def move_str():
    if user_num > 0:
        if user_num > 1:
            slice_list = ' '.join(user_list[0:user_num])
        else:
            slice_list = ''.join(user_list[0:user_num])
        del user_list[0:user_num]
        user_list.append(slice_list)
        result = ' '.join(user_list)
    else:
        if user_num < -1:
            slice_list = ' '.join(user_list[user_num:])
        else:
            slice_list = ''.join(user_list[user_num:])
        del user_list[user_num:]
        user_list.insert(0,slice_list)
        result = ' '.join(user_list)
    print(result)
move_str()
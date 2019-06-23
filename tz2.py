
list1 = list(input('Введите слова через пробел... ').split(' '))

list2 = []

def sort_list():
    f_word = list1.pop(0)
    list2.append(f_word)
    
    i = 1
    for i in range(len(list1)):
        if len(list2[len(list2) - 1]) <= len(list1[i]):
            list2.append(list1[i])
        else:
            list2.insert(0, list1[i])
    # print(list2)
    # list3 = str(list2.join(','))
    new_str = ' '.join(list2)
    print(new_str)
sort_list()









# def sort_list():
#     list2.append(list1[0])
#     for i in range(len(list1)):
#         for st in list2:
#             if len(list1[i]) == len(st):
#                 list2.append(list1[i])
#             else:
#                 list2.insert(0, list1[i])
#         i += 1
#     print(list2)
# sort_list()




























# user_str2.append(user_str[0])

# j = 1

# for i in user_str:
#     if len(i) < len(user_str[j]):
#         user_str2.append(i)
#     else:
#         user_str2.insert(0, i)
#     j += 1
# print(len(i))
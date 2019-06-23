# s = input('Наберите скобки... ')
def isBalanced(s):
    n_list = []

    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            n_list.append(s[i])
        elif s[i] == '}' and n_list[-1] == '{' and len(n_list) > 0:
            n_list.pop()
        elif s[i] == ']' and n_list[-1] == '[' and len(n_list) > 0:
            n_list.pop()
        elif s[i] == ')' and n_list[-1] == '(' and len(n_list) > 0:
            n_list.pop()
        else:
            print('NO')
            break
    if n_list == None:
        print('YES')
    else:
        print('NO')

    print(n_list)

isBalanced('{[](({}))}[])')
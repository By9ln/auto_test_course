def start():
    action = int(input('select an action: from 1 to 3 => '))
    if action == 1:
        print(secret_code(input('your text  => '),int(input('number from 1 to 25  => '))))
    elif action == 2:
        print(decode(input('your text  => '), int(input('number from 1 to 25  => '))))
    elif action == 3:
        exit()




def secret_code(st, num):
    alf = list('abcdefghijklmnopqrstuvwxyz')
    a = list(st)
    code_res = ''
    for i in range(len(a)):
        for j in range(len(alf)):
            if a[i] not in alf:
                if a[i] == ' ':
                    code_res += ')'
                    break
                elif a[i] == ',':
                    code_res += '&'
                    break
                elif a[i] == '.':
                    code_res += '#'
                    break
                elif a[i] == '?':
                    code_res += '%'
                    break
                elif a[i] == '!':
                    code_res += '@'
                    break
                elif a[i] == '-':
                    code_res += '*'
                    break
                else:
                    code_res += a[i]
                    break
            else:
                if a[i] == alf[j]:
                    if j > 25 - num:
                        x = (num - 1) - (25 - j)
                        code_res += alf[0 + x]
                        break
                    else:
                        code_res += alf[j + num]
                        break
    print(code_res)
    print(start())


def decode(st, num):
    alf = list('abcdefghijklmnopqrstuvwxyz')
    a = list(st)
    decode_res = ''
    for i in range(len(a)):
        for j in range(len(alf)):
            if a[i] not in alf:
                if a[i] == ')':
                    decode_res += ' '
                    break
                elif a[i] == '&':
                    decode_res += ','
                    break
                elif a[i] == '#':
                    decode_res += '.'
                    break
                elif a[i] == '%':
                    decode_res += '?'
                    break
                elif a[i] == '@':
                    decode_res += '!'
                    break
                elif a[i] == '*':
                    decode_res += '-'
                    break
                else:
                    decode_res += a[i]
                    break
            else:
                if a[i] == alf[j]:
                    if j > 25 - num:
                        x = (25 - j) - (num - 1)
                        decode_res += alf[0 + x]
                        break
                    else:
                        decode_res += alf[j - num]
                        break
    print(decode_res)
    print(start())


print(start())
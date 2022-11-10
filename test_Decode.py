def secret_code(st, num):
    alf = list('abcdefghijklmnopqrstuvwxyz')
    a = list(st)
    code_res = ''
    for i in range(len(a)):
        for j in range(len(alf)):
            if a[i] == alf[j]:
                code_res += alf[j + (num%j)]
                break
print(secret_code('mom', 30))
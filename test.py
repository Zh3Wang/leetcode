import sys


def repeat_str(string):
    lst = []
    num = 0
    string = str(string)
    res = ''
    for i in string:
        if not lst:
            lst.append(i)
            res = res + i
            num = num + 1
            continue
        if i != lst[-1]:
            lst.append(i)
            res = res + str(num)
            res = res + i
            num = 1
            continue
        num = num + 1
    res = res + str(num)
    return string if len(res) >= len(string) else res


print(repeat_str('cccddeeec'))

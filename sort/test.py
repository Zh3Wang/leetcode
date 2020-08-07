def sort(lst):
    l = len(lst)
    min = lst[0]
    max = lst[0]
    for j in range(1,l):
        if lst[j] < min:
            min = lst[j]
        elif lst[j] > max:
            max = lst[j]
    
    new = []
    for i in lst:
        if i == min or i == max:
            continue
        new.append(i)
    return new
    

def test(s):
    l = len(s)+1
    for i in range(1,l):
        subs = s.split(s[0:i])
        flag = True
        for j in subs:
            if j != '':
                flag = False
                break
        if flag == True:
            count = len(subs)-1
            value = s[0:i]
            break
        
    return count,value

lst = [3,3,4,5,6,7,7]
lst = 'aabaa'
print(lst)
count,value = test(lst)
print(count,value)



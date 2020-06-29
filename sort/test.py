def sort(lst):
    n = len(lst)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lst[min] > lst[j]:
                min = j
        if min != i:
            lst[min],lst[i] = lst[i],lst[min]
    return lst

lst = [3,5,4,1,2,9,6,8]
print(lst)
lst = sort(lst)
print(lst)
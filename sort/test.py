def sort(A,m,B,n):
    for k in range(n):
        value = B[k]
        j = m - 1
        while j >= 0 and value < A[j]:
            A[j+1] = A[j]
            j -= 1
        m = m + 1
        A[j+1] = value
    return A

    
A = [1,2,3,0,0,0]
m = 3
n = 3
B = [2,5,6]
print(sort(A,m,B,n))
quit()

lst = [3,5,4,1,2,9,6,8]
print(lst)
lst = sort(lst)
print(lst)
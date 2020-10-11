def test(a,b,c):
    if a >= b:
        return
    
    a += 1
    c += 1 
    test(a,b,c)
    print(a)
    return c
    

print(test(1,5,0))
quit()


lst = [3,5,4,1,2,9,6,8]
print(lst)
lst = sort(lst)
print(lst)
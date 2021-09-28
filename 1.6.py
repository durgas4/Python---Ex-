def ret_sqare(n):
    
    for i in range(1,n+1,2):
        total=0
        total+=i*i
    return total
values=int(input('Enter a number '))
print(ret_sqare(values))

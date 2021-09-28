def ret_sqare(n):
    total=0
    for i in range(1,n+1):
        total+=total+i*i
    return total
values=int(input('Enter a number '))
print(ret_sqare(values))

def is_multiple(n,m):
    if n%m==0:
        return True
    else:
        return False

        

n=int(input('Enter first value'))        
m=int(input('Enter second value'))
print(is_multiple(n,m))


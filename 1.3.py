def minmax(data):
    mins=maxs=data[0]
    for i in data:
        if i<mins:
            mins=i
        if i>maxs:
            maxs=i   
    return mins,maxs

values=input('Enter a list ')
print(minmax(values))

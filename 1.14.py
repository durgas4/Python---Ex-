def distinct(Data):
    for k in range(1,len(Data)):
        for j in range(k):
            if Data[j]==Data[k]:
                return False
            else:
                prod=Data[j]*Data[k]

        

def reverse(lst): 
    lst = "".join(reversed(lst)) # only way to reverse input list
    # strip gives white spaces '','7', like values
    return lst


lst=input()
print(reverse(lst))


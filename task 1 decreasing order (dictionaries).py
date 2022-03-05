#function dictionarie

string1 = input("enter the string:")
d1 = dict()
for a in string1:
    if a in d1:
        d1[a] = d1[a] = 1
    else:
        d1[a] = 1

print (d1)

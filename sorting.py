l = [4,5,2,1,6]
#Sort the list to ascending & descending order

for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]<l[j+1]: # condition change korle ascending hobe
            l[j],l[j+1]=l[j+1],l[j]
        else:
            pass

print(l)
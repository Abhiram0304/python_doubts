l=[12,45,23,51,19]
size=len(l)

for i in range(0,size):
    current=l[i]
    j=i-1
    while(l[j]>current and j>0):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=current
    
print(l)
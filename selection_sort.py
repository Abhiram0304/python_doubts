l=[12,45,23,51,19]
size=len(l)

for i in range(0,size-1):
    for j in range(i+1,size):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)
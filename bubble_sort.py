l=[12,45,23,51,19]
size=len(l)
end=len(l)-1

while(end>0):
    for i in range(0,end):
        if(l[i]>l[i+1]):
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
    end=end-1

print(l)

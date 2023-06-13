l=[2,4,5,3,2,7,7,3,6,10,2,1,56,78,99]
size=len(l)
d={}

for i in range(1,101):
    count=0
    for j in range(0,size):
        if(l[j]==i):
            count+=1
    # dict={i:count}
    d.update({i:count})

print(d)
        
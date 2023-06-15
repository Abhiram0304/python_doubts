N=int(input("No. of sticks :"))
l1=[]

for i in range(0,N):
    l1.append(i+1)

K=int(input("K ? "))

l2=[]
for i in range(0,K):
    l2.append(l1[i])
for i in range(len(l1)-1,K-1,-1):
    l2.append(l1[i])

print(l2)
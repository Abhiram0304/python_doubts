n=int(input("Terms ? "))

n1=0
n2=1

next_term=n1+n2

print(n1,n2,end=" ")

for i in range(3,n+1):
    print(next_term,end=" ")
    n1=n2
    n2=next_term
    next_term=n1+n2

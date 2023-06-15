n=int(input("N ? "))

mark1=2+(4*(n-1))
mark2=0

for i in range(0,n):
    for m2 in range(0,mark2):
        print("/",end="")
    for m1 in range(0,mark1):
        print("!",end="")
    for m2 in range(0,mark2):
        print("/",end="")
    print()
    mark1=mark1-4
    mark2=mark2+2
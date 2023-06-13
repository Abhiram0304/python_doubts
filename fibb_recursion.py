def fibb(n):
    if (n==1):
        return 0 # first element
    
    if(n==2):
        return 1 # second element
    
    return (fibb(n-1)+fibb(n-2)) # Recursive Function

n=int(input("Term ? "))
print("nth term of fibb series :",fibb(n))
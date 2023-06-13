def fact(n):
    if(n==0): #BASE CASE
        return 1 # should contain a return statement 
    else:
        return (n*fact(n-1))

n=int(input("Number? "))
print("Factorial of number :",fact(n))
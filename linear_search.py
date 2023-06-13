l=[3,1,2,6,5,4] # No need of sorting the list in linear search
size=len(l)
target=5

check=False # assume the element is not present in the list

for i in range(0,size):
    if(l[i]==target):
        check==True # if the target element is found , change the value of check
        break

if(check==True):
    print("Found!")

else:
    print("Not Found!")
l=[1,2,3,4,5,6,7,8,9,10]  #list has to be SORTED
key=9 # element to be found
start=0
end=len(l)-1
mid=(start+end)//2

check=False  # initially assume that element in not present in list

while(start<=end):
    if(l[mid]==key):
        check=True  # if element is found change the value of check to True
        break
        
    elif(l[mid]>key):
        end=mid-1

    elif(l[mid]<key):
        start=mid+1
    
    mid=(start+end)//2

if(check==True):
    print("Found!")

else:
    print("Not Found!")


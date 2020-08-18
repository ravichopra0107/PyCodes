print("Enter list values:",end=" ")
lst=input().split() 
print("List before: ",lst)
for i in lst:
    try:
        l=len(i)
        print("Length of ",i," is ",l)
    except:
        print("length is undefined!")

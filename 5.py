print("Enter list values:",end=" ")
lst=list(map(int,input().split())) 
print("List before: ",lst)
for i in lst:
    if i < 20:
        print("False")
        exit()
print("True")

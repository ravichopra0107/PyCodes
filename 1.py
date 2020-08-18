print("Enter list values:",end=" ")
lst=list(map(int,input().split())) 
print("List before: ",lst)
lst[1]=7
print("List after updating value at index 1: ",lst)
print("Length of list: ",len(lst))

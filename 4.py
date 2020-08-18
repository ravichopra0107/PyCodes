print("Enter list values:",end=" ")
lst=list(map(int,input().split())) 
print("List before: ",lst)
sum=0
for i in lst:
    sum+=i
print("Sum = ",sum)

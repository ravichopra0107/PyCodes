print("Enter list values:",end=" ")
lst=input().split() 
print("List before: ",lst)
count=0
for i in lst:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print("Count: ",count)

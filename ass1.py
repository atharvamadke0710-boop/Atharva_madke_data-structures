#number of members present in the library
n=int(input("enter the number of library members:"))
borrow=[0]*n
for i in range(n):
    borrow[i]=int(input("enter the number of books borrowed by member"+ str(i+1) + ":"))
#Calculating average number of books borrowed
total=0
for i in range(n):
    total =total+borrow[i]
    average= total/n
print("Average number of books borrowed:",average)
# finding highest and lowest number of books borrowed
highest=borrow[0]
lowest=borrow[0]

for i in range(1,n):
    if borrow[i]>highest:
        highest=borrow[i]
    if borrow[i]<lowest:
        lowest=borrow[i]

print("Highest borrow count:",highest)
print("Lowest borrow count:",lowest)
#members who borrowed no books
zero_count=0
for i in range(n):
    if borrow[i]==0:
        zero_count=zero_count+1
print("Members who borrowed no books:",zero_count)

# most frequently borrowed books
mode=borrow[0]
max_count=0
for i in range(n):
    count=0
    for j in range(n):
        if borrow[i]==borrow[j]:
            count=count+1
    if count>max_count:
        max_count=count
        mode=borrow[i]
print("Most frequently borrowed book count (mode):",mode)

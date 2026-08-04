# Linear Search
def linear_search(acc,target_id):
    for i in range(len(acc)):
        if acc[i]==target_id:
            return i
    return -1
# Binary Search
def binary_search(acc,target_id):
    low=0
    high=len(acc)-1

    while low<=high:
        mid=(low+high)//2

        if acc[mid]==target_id:
            return mid
        elif acc[mid]>target_id:
            return mid-1
        else:
            return mid+1
    return -1

# Taking input for the no. od ID's
n=int(input("Enter no. of ID's:"))
# Taking input for the ID's
print("Enter ID's in sorted manner:")
acc=[]
for i in range(n):
    acc.append(int(input()))
 
# The input of ID you want to search 
target_id=int(input("Enter the ID you want to search:"))
# Calling linear search function 
result1=linear_search(acc,target_id)
if result1!=-1:
    print("The ID is at:",result1+1)
else:
    print("The ID not found")
# Calling binary search fuction
result2=binary_search(acc,target_id)
if result2!=-1:
    print("The ID is at:",result2+1)
else:
    print("The ID not found")



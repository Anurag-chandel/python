lst=[]
n=int(input("Enter the length of list"))
for i in range(n):
    x=int(input("Enter the next number"))
    lst.append(x)
def count(lst):
    even=0
    odd=0
    for j in lst:
        if j%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd=count(lst)
print("Even:{}\nOdd {}".format(even,odd))
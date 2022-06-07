def count(ls):
    even=0
    odd=0
    for i in ls:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd


ls=list(map(int,input().split()))
even, odd = count(ls)
print("Even :{} Odd :{}", format(even, odd))

print("Even number are ", even)
print("Odd number are", odd)
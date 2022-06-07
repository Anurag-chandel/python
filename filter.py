def is_even(n):
    return n%2==0


num=[1, 2, 3, 4, 5, 6]
f=list(filter(is_even, num))
print(f)
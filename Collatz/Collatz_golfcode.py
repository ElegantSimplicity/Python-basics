# a golfcode taste

n=int(input())
while n>1:
    n=(n//2,3*n+1)[n%2]
    print(n)

"""
n=5**100     # lâu
d,max_value=0,n
while n>1:
    print(n,end=' -> ')
    n=(n//2,3*n+1)[n%2]
    d +=1
    max_value = max(n,max_value)
print(1)
print('The length: ',d)
print('The maximum value: ',max_value)
"""
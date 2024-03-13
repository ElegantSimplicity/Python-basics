def permutations(n):
    """List gồm các hoán vị của n phần tử"""
    if n == 1: return [[1]]
    temp = []
    #for i in range(n):
    for i in range(n-1,-1,-1):      # Cách viết theo thứ tự khác
        for p in permutations(n - 1):
            temp.append(p[:i] + [n] + p[i:])
    return temp

k = 3
P = permutations(k)
print(f'Có {len(P)} hoán vị: {P}')

#""" Nếu thích viết đẹp hơn
print(f'Có {len(P)} hoán vị:')
for p in P:
    for i in range(len(p)):
        print(p[i],end='')
    print(end=' ')
#"""    
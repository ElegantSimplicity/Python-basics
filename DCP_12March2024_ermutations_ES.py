def permutations(n):
    """List gồm các hoán vị của n phần tử"""
    if n == 1: return [[1]]
    temp = []
    for i in range(n):
    #for i in range(n-1,-1,-1):      # Cách viết theo thứ tự khác
        for p in permutations(n-1):
            temp.append(p[:i] + [n] + p[i:])
    return temp

k = 3
Per = permutations(k)
print(f'Có {len(Per)} hoán vị: {Per}')

#""" Nếu thích viết đẹp hơn
print(f'Có {len(Per)} hoán vị:')
for per in Per:
    for k in range(len(per)):
        print(per[k], end='')
    print(end=' ')
#"""    

# https://www.tutorialspoint.com/python/python_the_continue_statement.htm
#N = 85800   # thiếu 11
N = 68958232200    # thiếu 103
print ("Prime factors for: ", N)
n=N
d=2
primefactor=[]
while n>1:
    if n%d==0:
        primefactor.append(d)
        n=int(n/d)
        continue
    d+=1

print(primefactor)

# Should we? list to dict <k:v> is <divisor> : <its multiplicity>
# Should NOT! but we can printout as desỉed
# Lỗi tinh tế: thiếu số 11! Đố bạn biết lý do và sửa được
pf=primefactor
print(N,' = ',end=' ')
for i in pf:
    if pf.count(i)>1:
        print(f'{i}^{pf.count(i)}',end=' . ')
        for j in pf:
            if i==j: pf.remove(j)
    else:
        print(f'{i}',end=' . ')
        pf.remove(i)
# https://www.tutorialspoint.com/python/python_the_continue_statement.htm
#N = 85800
N = 22986077400*3
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
# Sửa lỗi thiếu số 11
# Ví dụ tốt: set/list of tuples (here are pairs) + lambda + for (i,j)

dm={(i,primefactor.count(i)) for i in primefactor}     # set comprehension (avoiding duplicated)
dms=sorted(dm, key=lambda a: a[0])                     # now is a list 
print(N,' = ', dm)
print(N,' = ', dms)

print(N,' = ',end=' ')
for (i,j) in dms:
    if j==1: print(i,end=' . ')
    else:    print(f'{i}^{j}',end=' . ')
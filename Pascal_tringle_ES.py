# In ra tam giác Pascal
# (là các hệ số của khai triển nhị thức Newton)
# Quy tắc (công thức): C_{n+1}^{k+1} = C_n^k + C_n^{k+1}
n=9            # số dòng tam giác
a=[[1],[1,1]]   # dòng 0 và dòng 1
i=2             # bắt đầu tính dòng 2
while i<n:                       
    b=[1]                                 # thêm 1 vào đầu dòng i
    for j in range(1,i):
        b.append(a[i-1][j-1]+a[i-1][j])   # cộng theo quy tắc 
    b.append(1)                           # thêm 1 vào cuối dòng i
    a.append(b)
    i +=1    

# Cách in ra thứ nhất: thô, có []
for i in range(len(a)):
    print(a[i])

# Cách in ra thứ hai: đỡ thô hơn, không có []
for i in range(len(a)):
    for j in range(len(a[i])):
        #print(a[i][j],end=' ')
        print(f"{a[i][j]:3d}",end=' ')
    print()    

# Cách in ra thứ ba: căn giữa
for i in range(len(a)):
    print('   '*(n-i+1),end='')
    for j in range(len(a[i])):
        #print(a[i][j],end='   ')
        print(f"{a[i][j]:3d}",end='   ')
    print()    

# Cách in ra thứ tư: căn giữa
for i in range(len(a)):
    s=''
    for j in range(len(a[i])):
        s += str(a[i][j]) + '    '
    print(s.center(80))    

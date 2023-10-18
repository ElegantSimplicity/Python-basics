# dùng for hay while là tùy ngữ cảnh. be FLEXIBLE!
# Ví dụ: in ra dãy Fibonacci sao cho

# nhỏ hơn 100
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a+b
 
print() 
# 15 số hạng đầu của dãy
a, b = 0, 1
n = 1
while n < 15:
    print(b, end=' ')
    a, b = b, a+b
    n += 1

print() 
# 15 số hạng đầu của dãy
a, b = 0, 1
for i in range(1,15):
    print(b, end=' ')
    a, b = b, a+b
    

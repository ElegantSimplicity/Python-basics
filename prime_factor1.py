# https://www.tutorialspoint.com/python/python_the_continue_statement.htm
#n = 85800
n = 68958232200    # thiếu 103

print ("Prime factors for: ", n)
d=2
while n>1:
    if n%d==0:
        print(d)
        n=int(n/d)
        continue
    d+=1
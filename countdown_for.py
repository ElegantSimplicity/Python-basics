# https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
# https://sites.pitt.edu/~naraehan/python3/mbb15.html
# Thời gian: 10 phút
# 5 phút đầu: time.sleep(1) có tác dụng gì?
# 5 phút cuối: hãy viết lại chương trình dùng for
# (vì trong trường hợp này số lần lặp đã biết trước)
import time
countdown = 10
newYear = 0
for i in range(countdown,0,-1):
    print(i)
    time.sleep(1)
    
print('Happy New Year!')

# https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
# https://sites.pitt.edu/~naraehan/python3/mbb15.html
# Bạn hãy viết lại chương trình dùng for
# (vì trong trường hợp này số lần lặp đã biết trước)
import time
countdown = 10
newYear = 0
while countdown > newYear:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print('Happy New Year!')
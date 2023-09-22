"""
Matrix Example: plain Python! (không dùng numpy)
Consider the case of recording temprature for 1 week
measured in the morning, mid-day, evening and mid-night.
It can be presented as a 7X5 matrix using an array
and the reshape method available in numpy.
"""
m = [['Mon',18,20,22,17],
    ['Tue',11,18,21,18],
    ['Wed',15,21,20,19],
    ['Thu',11,20,22,21],
    ['Fri',18,17,23,22],
    ['Sat',12,22,20,18],
    ['Sun',13,15,19,16]]

print(m)   # ra danh sách ngang, có thể không tiện xem
for i in range(len(m)): print(m[i])  # in ra danh sách dọc

# Print data for Wednesday
print(m[2])
# Print data for friday evening
print(m[4][3])

"""
https://www.tutorialspoint.com/python_data_structure/python_data_structure_quick_guide.htm
Matrix Example: dùng numpy
Consider the case of recording temprature for 1 week
measured in the morning, mid-day, evening and mid-night.
It can be presented as a 7X5 matrix using an array
and the reshape method available in numpy.
"""
from numpy import * 
a = array([['Mon',18,20,22,17],
           ['Tue',11,18,21,18],
           ['Wed',15,21,20,19],
           ['Thu',11,20,22,21],
           ['Fri',18,17,23,22],
           ['Sat',12,22,20,18],
           ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)
# Print data for Wednesday
print(m[2])
# Print data for friday evening
print(m[4][3])
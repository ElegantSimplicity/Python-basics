"""Hàm where() của numpy
https://numpy.org/doc/stable/reference/generated/numpy.where
https://www.geeksforgeeks.org/numpy-where-in-python/
https://www.w3schools.com/python/numpy/default.asp
https://www.programiz.com/python-programming/numpy/methods/where
Hỏi Gemini (Bard, Google) https://g.co/gemini/share/0e14604fcf5f
Hỏi Bing's Copilot: https://sl.bing.net/kLNHDmQUGPI
Numpy.where() là một hàm của thư viện numpy, dùng để trả về các chỉ số của các phần tử
trong một mảng đầu vào mà thỏa mãn một điều kiện cho trước.
Bạn có thể truyền vào ba tham số cho hàm này: condition, x và y.
Nếu bạn chỉ truyền vào condition: 
numpy.where(condition) >>> hàm sẽ trả về một tuple
chứa các mảng chỉ số của các phần tử thỏa mãn condition.
Nếu bạn truyền vào cả x và y,
numpy.where(condition, x, y) >>> hàm sẽ trả về một mảng có cùng kích thước với condition,
mà mỗi phần tử là x nếu condition là True, và y nếu condition là False.
"""  
import numpy as np 

a = np.array([10, 1, 10, 4, 5, 2, 8, 7])  # mảng điểm các sinh viên 
index8 = np.where(a >= 8)
print('Các sinh viên ở vị trí ', index8)
print('\tcó điểm giỏi (>=8): ', a[index8])


print ('Sinh viên điểm dưới 5 thì cho lên 5 điểm:') 
b = np.where(a < 5, 5, a)
print(b) 

index_max = np.where(a == max(a)) 
print(f"Các sinh viên có điểm tốt nhất (điểm {max(a)})") 
print('\tở vị trí: ', index_max)

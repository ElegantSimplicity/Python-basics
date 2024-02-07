"""NamedTuple vs class"""
#https://g.co/bard/share/3ab14d8f6fa9

# Cách dùng dữ liệu thứ nhất: NamedTuple từ typing
# (tạo kiểu dữ liệu là 1 bộ: đơn giản ngắn gọn nhưng không thay đổi được)
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
from typing import NamedTuple
class Employee(NamedTuple):
    name: str
    age: int = 8

H = Employee('Huy')
H_dad = Employee('Huy',46)
print(f'{H.name} is {H.age}')
print(f'{H_dad.name} is {H_dad.age}')

# Cách dùng dữ liệu thứ hai: class thông thường
# tạo kiểu dữ liệu phức tạp, nhưng cần khởi tạo
# https://www.w3schools.com/python/python_classes.asp
class Person:
    def __init__(self, name, age = 8):
        self.name = name
        self.age = age

p = Person("John")
q = Person("Black",45)
print(f'{p.name} is {p.age}')
print(f'{q.name} is {q.age}')
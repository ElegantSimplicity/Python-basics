# Các kiểu dữ liệu và Conprehension
# Bộ số 1,4,9,16,25,36 có nhiều cách lưu dữ liệu
print('1. This is about LIST conprehension')
a = [i*i for i in range(1,7)]
print(a)
print(type(a))

print('2. This is about GENERATOR')
b = (i*i for i in range(1,7))
print(b)
print(type(b))

print('3. This is about TUPLE conprehension')
c = tuple(i*i for i in range(1,7))
print(c)
print(type(c))

print('4. This is about SET conprehension')
d = {i*i for i in range(1,7)}
print(d)
print(type(d))

print('5. This is about DICT conprehension, consist of pairs <key> : <value>')
e = {x: x**2 for x in range(7)}
print(e)
print(type(e))

print('6. This is about ENUMERATE')
e=enumerate(i*i for i in range(1,7))
print(e)
print(type(e))

print('7. This is about DICT using ENUMERATE')
f=dict(enumerate(i*i for i in range(7)))
print(f)
print(type(f))



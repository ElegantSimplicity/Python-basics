# Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là
# một chuỗi mật khẩu mạnh hay không (một chuỗi mật khẩu mạnh
# cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số,
# 1 chữ thường và độ dài phải lớn hơn 6
# Dùng thư viện Regular Expression
# có thể thay \d bởi [0-9]

import re

def strong_password(password):
    special_characters = '[@_!#$%^&*()<>?/\|}{~:]'
    password_rule = ['.{7,}', '[A-Z]', '[a-z]', '\d', special_characters]
    return all(re.search(pattern, password) for pattern in password_rule)

password = input("Nhập mật khẩu: ")
if strong_password(password):
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu, hãy thử lại!")

# Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là
# một chuỗi mật khẩu mạnh hay không (một chuỗi mật khẩu mạnh
# cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số,
# 1 chữ thường và độ dài phải lớn hơn 6
# Chương trình chưa tối ưu, nhưng chấp nhận được vì password thường không quá dài! 
def strong_password(password):
    cond1 = len(password) > 6
    cond2 = any(cha.isupper() for cha in password)
    cond3 = any(cha.islower() for cha in password)
    cond4 = any(cha.isdigit() for cha in password)
    special_chars = '[@_!#$%^&*()<>?/\|}{~:]'  
    cond5 = any(cha in special_chars for cha in password)
    return cond1 and cond2 and cond3 and cond4 and cond5

password = input("Nhập mật khẩu: ")
if strong_password(password):
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu, hãy thử lại!")
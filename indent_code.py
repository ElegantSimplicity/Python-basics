# Hiện tại Bard gợi ý code với thụt lề tab 2 khoảng trống
# trong khi PEP8 khuyến khích với thụt lề tab chuẩn 4 khoảng trống
# Bài tập thêm: lấy code từ file rồi chỉnh khoảng trống
# (từ mã miller-rabin của Bard gợi ý thuật toán tốt nhất kiểm tra số nguyên tố)
def indent_code(code):
    """
    Input : code với thụt lề các tab 2 khoảng trống
    Output: code với thụt lề các tab chuẩn 4 khoảng trống
    Cách làm: nhân đôi khoảng trống đầu mỗi dòng 
    """

    lines = code.splitlines()
    for i, line in enumerate(lines):
        # Lấy số lượng khoảng trống ở đầu dòng
        indent_length = len(line) - len(line.lstrip())
        # Thụt lề dòng
        lines[i] = " " * indent_length * 2 + line.lstrip()
    return "\n".join(lines)

# mã này chỉ thụt lề các tab 2 ký tự 
code = """
def foo():
  for i in range(5):
    print("Hello, world!")
    if i % 3 == 0:
      break
"""

print('The code is:')
print(code)

# Mã mới thụt lề các tab 4 khoảng trống
new_code = indent_code(code)
print('The new code is:')
print(new_code)
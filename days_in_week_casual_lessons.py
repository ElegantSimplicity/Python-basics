""" https://www.w3schools.com/cpp/cpp_switch.asp
w3schools chưa cập nhật cú pháp mới match case
# C++ to Python
# Nhập số ngày, in ra tên của ngày 
# Các bài học:
1. Chọn ngôn ngữ là quan trọng:
    C++ nói chung là dài và buồn tẻ hơn Python
2. Chọn cú pháp:
    Trong tình huống này, match case (Python) hay switch case (C++) không thích hợp 
3. Chọn kiểu dữ liệu:
    - Nên dùng kiểu từ điển
    - Dùng dict trực tiếp, hoặc gián tiếp qua zip      
4. Chọn programing style:
    Không nhất thiết cứ phải viết hàm (functional programing style)
"""
# Cách 1: trực tiếp dùng từ điển
days = {1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
        }
day = 4
print(days[day])

# Cách 2: dùng dict qua zip
day_string = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
mydays = dict(zip(range(1,8),day_string))
day = 4
print(mydays[day])

# Cách 3: viết hàm, dùng match case >>> dài dòng
def day_of_week(day: int) -> str:
    match day:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Saturday"
        case _: return "Unknown"

day = 4
print(day_of_week(day))

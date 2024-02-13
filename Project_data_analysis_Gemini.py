""" Project: Data Analysis in AI time
Copy yêu cầu dưới đây và hỏi Gemini (trước đây tên Bard) của Google.
Gemini cho code trong vài giây https://g.co/gemini/share/907371161030
AI đã làm thay hầu hết việc phân tích dữ liệu
"""
"""Yêu cầu: Cho bộ dữ liệu tên và điểm của lớp 12A (kiểu từ điển).
1. Sắp xếp danh sách theo tên (kèm theo điểm)
2. Sắp xếp danh sách theo điểm từ cao xuống thấp (kèm theo tên)
3. In ra các bạn điểm cao nhất (kèm theo điểm)
4. Các thống kê (median, max, min) và phân loại:
        điểm sinh giỏi (>=8);
        điểm trung bình trở lên (>=5);
        điểm dưới trung bình (<5)
"""
score_12A = {
    'Nam' : 3,
    'Hoài': 5,
    'Liên': 9,
    'Lan': 7,
    'Phương': 8,
    'Xuân': 9,
    'Mai': 1,
    'Tuyết': 9,
    'Bông': 1,
    'Tuyến': 6
    }

from collections import OrderedDict

print('1. Sắp xếp danh sách theo tên (kèm theo điểm)')
# Sắp xếp theo key (tên)
sorted_by_name = OrderedDict(sorted(score_12A.items()))

# In ra danh sách
for name, score in sorted_by_name.items():
    print(f"{name} : {score}")

print('2. Sắp xếp danh sách theo điểm từ cao xuống thấp (kèm theo tên)')
# Chuyển đổi từ điển thành danh sách
score_list = [(name, score) for name, score in score_12A.items()]

# Sắp xếp theo value (điểm) từ cao xuống thấp
score_list.sort(key=lambda x: x[1], reverse=True)

# In ra danh sách
for name, score in score_list:
    print(f"{name} : {score}")

print('3. In ra các bạn điểm cao nhất (kèm theo điểm)')
# Tìm điểm cao nhất
max_score = max(score_12A.values())

# Lọc ra các bạn có điểm cao nhất
best_students = [name for name, score in score_12A.items() if score == max_score]

# In ra danh sách
print("Học sinh có điểm cao nhất:")
for name in best_students:
    print(f"{name} : {max_score}")
    
print('4. Các thống kê (median, max, min) và phân loại (có chỉ ra phần trăm):')
import statistics

# Tính toán các thống kê
median_score = statistics.median(score_12A.values())
max_score = max(score_12A.values())
min_score = min(score_12A.values())

# Phân loại điểm
score_categories = {
    "Giỏi": 0,
    "Trung bình trở lên": 0,
    "Dưới trung bình": 0
}
for score in score_12A.values():
    if score >= 8:
        score_categories["Giỏi"] += 1
    elif score >= 5:
        score_categories["Trung bình trở lên"] += 1
    else:
        score_categories["Dưới trung bình"] += 1

# Tính toán phần trăm
total_students = len(score_12A)
for category, count in score_categories.items():
    percentage = round(count / total_students * 100, 2)
    print(f"{category}: {count} ({percentage}%)")

# In ra các thống kê
print(f"Median: {median_score}")
print(f"Max: {max_score}")
print(f"Min: {min_score}")


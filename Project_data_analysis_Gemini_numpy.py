import numpy as np

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
# Tạo mảng tên và điểm
#names = np.array(['Nam', 'Hoài', 'Liên', 'Lan', 'Phương', 'Xuân', 'Mai', 'Tuyết', 'Bông', 'Tuyến'])
#scores = np.array([3, 5, 9, 7, 8, 9, 1, 9, 1, 6])
names = np.array(list(score_12A.keys()))
scores = np.array(list(score_12A.values()))
print(names)
print(scores)
# Sắp xếp danh sách theo tên (kèm theo điểm)
sorted_by_name = np.lexsort([scores, names])

# In ra danh sách
for i in sorted_by_name:
    print(f"{names[i]} - {scores[i]}")

# Sắp xếp danh sách theo điểm từ cao xuống thấp (kèm theo tên)
sorted_by_score = np.argsort(scores)[::-1]

# In ra danh sách
for i in sorted_by_score:
    print(f"{names[i]} - {scores[i]}")

# In ra các bạn điểm cao nhất (kèm theo điểm)
best_students = names[scores == np.max(scores)]

# In ra danh sách
print("Học sinh có điểm cao nhất:")
for name in best_students:
    print(f"{name} - {np.max(scores)}")

# Phân loại điểm
score_categories = {
    "Giỏi": np.sum(scores >= 8),
    "Trung bình trở lên": np.sum(scores >= 5),
    "Dưới trung bình": np.sum(scores < 5)
}

# Tính toán phần trăm
total_students = len(scores)
for category, count in score_categories.items():
    percentage = round(count / total_students * 100, 2)
    print(f"{category}: {count} ({percentage}%)")

# In ra các thống kê
print(f"Median: {np.median(scores)}")
print(f"Max: {np.max(scores)}")
print(f"Min: {np.min(scores)}")

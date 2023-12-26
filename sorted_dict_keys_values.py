# Program 73: sắp xếp từ điển theo key; theo value
# https://drive.google.com/file/d/1Lf76ElJmwZU3cF7DMrDBun9wTSVtrbfF/view
# # https://github.com/ElegantSimplicity/Python-basics/blob/main/sorted_dict_keys_values.py
# Từ điển (dict) là kiểu dữ liệu gồm các bộ key : value
# Chú ý: key trong lệnh sorted khác với key trong từ điển
# (xem https://www.w3schools.com/python/ref_func_sorted.asp)

D = {'Apple': 3, 'Papaya': 1, 'Banana': 4, 'Cherry': 2}
print("My dict is:      ", D)
print("Sắp xếp dùng hàm 'sorted'")
D_keys = dict(sorted(D.items()))
print("Sorted by keys:  ", D_keys)

D_values = dict(sorted(D.items(), key=lambda item: item[1]))
print("Sorted by values:", D_values)

###########################################################
print("\nCách in khác như sau:")
print("Theo keys", end = " "*10)
for k, v in D_keys.items():
    print(f"{k}: {v}", end = " "*5)
print("\nTheo values", end = " "*8)
for k, v in D_values.items():
    print(f"{k}: {v}", end = " "*5)

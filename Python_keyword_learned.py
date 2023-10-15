# In ra bảng các từ khóa Python: cả cứng và mềm
# Tô màu các từ khóa Python đã biết
# Lưu ý: gõ help('keyword') tại dấu nhắc thì cũng ra bảng

# Hàm in bảng các phần tử của arr, mặc định 5 cột
def ESprint(arr, column=5):
    for i in range(len(arr)):
        if i % column == 0: print()
        print(arr[i].ljust(10),end='')

# https://github.com/tartley/colorama
# Các màu sắc có dạng '\033[3im' với i từ 0 đến 9
# 30m      # black
# 31m      # red
# 32m      # green
# 33m      # yellow
# 34m      # blue
# 35m      # magenta
# 36m      # cyan
# 37m      # white
# 39m      # reset

# Hàm in bảng các phần tử của arr, mặc định 5 cột
# và các phẩn tử của subarr được in màu đỏ
def ESprint_with_color(arr, column=5, sub_arr={}):
    for i in range(len(arr)):
        if i % column == 0: print()
        if arr[i] in sub_arr:
            # 31m : red, 39m : back to normal 
            print('\033[31m' + arr[i].ljust(10) + '\033[39m',end='')
        else:
            print(arr[i].ljust(10),end='')

import keyword

kw  = keyword.kwlist        # các từ khóa
skw = keyword.softkwlist    # các từ khóa mềm

print('All Python keywords'.upper())
ESprint(kw + skw,6)

s = '\033[31m' + 'red' + '\033[39m'
print(f'\n\nAll Python keywords I have learnt in {s}:')
learned_keywords = {'match','case','_','from','import',
                    'global','as','and','or','is',
                    'lambda','return','def',
                    'if','elif','for','else','while',
                    'in','not','True','False','None',
                    'break','continue','pass'}
ESprint_with_color(kw + skw,6,learned_keywords)
t = len(learned_keywords)/ len(kw + skw) * 100
print(f'\n\nBạn đã học {t:.2f} % từ khóa Python. Keep trying!')
""" Cho trước hai xâu kí tự s1, s2.
Viết đoạn chương trình in ra xâu kí tự
bao gồm lần lượt các kí tự được lấy ra từ s1, s2.
Nếu một trong hai xâu s1, s2 hết trước thì lấy tiếp từ xâu còn lại.
Ví dụ nếu s1 = "012", s2 = "0a1b2cde" thì kết quả sẽ là "00a1b2cde".
"""
# Dùng for: đơn giản hơn
def combine_stringA(s1, s2):
    s = ''
    minlen = min(len(s1),len(s2))
    maxlen = max(len(s1),len(s2))
    for i in range(minlen):
        s += s1[i]
        s += s2[i]
    
    if len(s1) >= len(s2):
        s += s1[minlen:]
    else:
        s += s2[minlen:]
    return s

# dùng while: hiệu quả hơn
def combine_stringB(s1, s2):
    s = ""
    i = 0
    j = 0
    while i < len(s1) or j < len(s2):
        if i < len(s1):
            s += s1[i]
            i += 1
        if j < len(s2):
            s += s2[j]
            j += 1
    return s

s1 = '012345'
s2 = 'abcdefghij'
print(combine_stringA(s1, s2))
print(combine_stringB(s1, s2))
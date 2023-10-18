# break continue pass đều dùng cho các vòng lặp for while
# Minh họa bằng 1 ví dụ đơn giản
# break     >>> thoát khỏi tất cả vòng lặp
# continue  >>> nhảy sang vòng lặp tiếp theo
# pass      >>> bỏ qua câu lệnh chứa pass
#               làm nốt việc của vòng lặp hiện tại
#               nhảy sang vòng lặp tiếp theo
# Như vậy 'pass' làm nhiều việc hơn `continue`
# Trong 2 chương trình sau, break và pass có cùng kết quả
# nhưng continue cho khác kêt quả. (Check why)
i=1
while i < 9:
    if i == 4:
        #break
        continue
        #pass
    else: print(i,end='  ')
    i +=1
    print(f'  ... end of the {i}-th loop of while')

print('\nDo something else ...')
print('\nDone!')
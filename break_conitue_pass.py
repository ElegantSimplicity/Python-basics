# Minh họa break continue pass: dễ thôi!
# break     >>> thoát khỏi tất cả vòng lặp
# continue  >>> nhảy sang vòng lặp tiếp theo
# pass      >>> bỏ qua câu lệnh chứa pass
#               làm nốt việc của vòng lặp hiện tại
#               nhảy sang vòng lặp tiếp theo
# Như vậy 'pass' làm nhiều việc hơn `continue`

for i in range(1,9):
    if i == 4:
        #break
        #continue
        pass
    else: print(i,end='  ')
    print(f'  ... end of {i}-th loop')
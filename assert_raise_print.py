unique_characters = 'fkfkbkfdj.nskjfnkè'
#print(len(unique_characters))

"""
3 lệnh sau có cùng tác dụng. Bạn thích dùng lệnh nào?
nghe Bard giải thích https://g.co/bard/share/44da0c8de057
"""

#if len(unique_characters) > 5:
 #   print('Error: Too many letters')                      # rồi tiếp tục chạy
    
#if len(unique_characters) > 5:
    #raise ValueError('Too many letters')                  # ngừng chạy

assert len(unique_characters) <= 5, 'Nhiều chữ quá'        # ngừng chạy

print('Tiếp tục chạy ...')

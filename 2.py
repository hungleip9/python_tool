# d = open('test.txt', 'w', encoding='utf-8')
# d.write('day la noi dung file nhe3')
# d.close

import os
# đổi tên file
# os.rename('test.txt', 'test_moi.txt')
# xóa file
# os.remove('test_moi.txt')
# tạo folder
# os.mkdir('mat_khau')
# xóa folder
# os.rmdir('mat_khau')
# đọc nội dung thư mục
# D = os.listdir('D:\ToolPython\hung')
# print(D)
# đổi tên thư mục
# os.rename('hung', 'hunglq')

# xóa thư mục
import shutil
shutil.rmtree('D:\ToolPython\hunglq')
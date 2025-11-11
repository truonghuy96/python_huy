import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from common.delete_danhmuc import delete_danhmuc

while True:
    ma = input("Nhập mã danh mục cần xóa: ")
    delete_danhmuc(ma)
    cont = input("Nhấn 'y' để tiếp tục, phím khác để thoát: ")
    if cont.lower() != 'y':
        break

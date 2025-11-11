import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập tên danh mục: ")
    mota = input("Nhập mô tả danh mục: ")
    insert_danhmuc(ten, mota)
    cont = input("Nhấn 'y' để tiếp tục, phím khác để thoát: ")
    if cont.lower() != 'y':
        break

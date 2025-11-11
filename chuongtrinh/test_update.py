import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from common.update_danhmuc import update_danhmuc

ma_dm = input("Nhập mã danh mục cần cập nhật: ")
ten_moi = input("Nhập tên danh mục mới: ")
mota_moi = input("Nhập mô tả mới: ")

update_danhmuc(ma_dm, ten_moi, mota_moi)

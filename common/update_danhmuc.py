from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(ma_dm, ten_moi, mota_moi):
    """Cập nhật tên và mô tả danh mục theo mã danh mục"""
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối MySQL.")
            return

        cursor = connection.cursor()

        # Câu lệnh SQL cập nhật
        sql = """
        UPDATE danh_muc
        SET ten_dm = %s,
            mo_ta = %s
        WHERE ma_dm = %s
        """

        # Dữ liệu truyền vào
        data = (ten_moi, mota_moi, ma_dm)
        cursor.execute(sql, data)
        connection.commit()

        # Kiểm tra có bản ghi nào bị ảnh hưởng không
        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có mã {ma_dm}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {ma_dm}")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")

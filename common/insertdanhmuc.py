from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def insert_danhmuc(ten_dm, mo_ta):
    """Thêm danh mục mới vào bảng danh_muc (ma_dm, ten_dm, mo_ta)"""
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối MySQL.")
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danh_muc (ten_dm, mo_ta) VALUES (%s, %s)"
        data = (ten_dm, mo_ta)
        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã thêm danh mục mới: {ten_dm}")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")

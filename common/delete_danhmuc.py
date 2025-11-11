from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(ma_dm):
    """Xóa danh mục theo mã danh mục"""
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối MySQL.")
            return

        cursor = connection.cursor()
        sql = "DELETE FROM danh_muc WHERE ma_dm = %s"
        data = (ma_dm, )
        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Đã xóa danh mục có mã: {ma_dm}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã: {ma_dm}")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

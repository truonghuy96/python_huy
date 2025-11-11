from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    """Lấy danh sách tất cả danh mục trong bảng danh_muc"""
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối MySQL.")
            return

        cursor = connection.cursor()
        sql = "SELECT ma_dm, ten_dm, mo_ta FROM danh_muc"
        cursor.execute(sql)
        records = cursor.fetchall()

        if len(records) == 0:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("\n📋 DANH SÁCH DANH MỤC")
            print("-" * 60)
            print(f"{'Mã DM':<6} {'Tên danh mục':<30} {'Mô tả'}")
            print("-" * 60)
            for row in records:
                print(f"{row[0]:<6} {row[1]:<30} {row[2]}")
            print("-" * 60)
            print(f"✅ Tổng cộng: {len(records)} danh mục.\n")

    except Error as e:
        print("❌ Lỗi khi truy vấn danh mục:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")

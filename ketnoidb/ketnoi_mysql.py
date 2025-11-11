import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối đến MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # nếu MySQL có mật khẩu thì điền vào đây
            database='QLThuocAnKhang'  # đúng tên database của bạn
        )

        if connection.is_connected():
            print("✅ Kết nối thành công tới database QLThuocAnKhang!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None

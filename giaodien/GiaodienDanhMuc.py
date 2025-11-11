import tkinter as tk
from tkinter import ttk, messagebox
from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.get_all_danhmuc import get_all_danhmuc


# ================
# HÀM XỬ LÝ SỰ KIỆN
# ================

def load_data():
    """Hiển thị danh sách danh mục"""
    tree.delete(*tree.get_children())
    rows = get_all_danhmuc()
    if rows:
        for row in rows:
            tree.insert("", tk.END, values=row)
    else:
        messagebox.showinfo("Thông báo", "Không có dữ liệu danh mục.")


def them_danhmuc():
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()

    if ten == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return

    insert_danhmuc(ten, mota)
    load_data()
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)


def sua_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần sửa.")
        return

    ma_dm = tree.item(selected[0])["values"][0]
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()

    if ten == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return

    update_danhmuc(ma_dm, ten, mota)
    load_data()


def xoa_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa.")
        return

    ma_dm = tree.item(selected[0])["values"][0]
    xacnhan = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục có mã {ma_dm}?")
    if not xacnhan:
        return

    delete_danhmuc(ma_dm)
    load_data()


def chon_dong(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0])["values"]
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.insert(0, values[2])


# ================
# GIAO DIỆN CHÍNH
# ================

root = tk.Tk()
root.title("Quản lý Danh Mục - QLThuocAnKhang")
root.geometry("750x500")

frame_input = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, sticky="w")
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- Nút chức năng ---
frame_btn = tk.Frame(root)
frame_btn.pack(fill="x", pady=5)

tk.Button(frame_btn, text="Thêm", bg="#4CAF50", fg="white", width=12, command=them_danhmuc).pack(side="left", padx=5)
tk.Button(frame_btn, text="Sửa", bg="#2196F3", fg="white", width=12, command=sua_danhmuc).pack(side="left", padx=5)
tk.Button(frame_btn, text="Xóa", bg="#F44336", fg="white", width=12, command=xoa_danhmuc).pack(side="left", padx=5)
tk.Button(frame_btn, text="Tải lại", bg="#9E9E9E", fg="white", width=12, command=load_data).pack(side="left", padx=5)

# --- Bảng Treeview ---
columns = ("ma_dm", "ten_dm", "mo_ta")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("ma_dm", text="Mã DM")
tree.heading("ten_dm", text="Tên danh mục")
tree.heading("mo_ta", text="Mô tả")
tree.column("ma_dm", width=80, anchor="center")
tree.column("ten_dm", width=200)
tree.column("mo_ta", width=350)
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", chon_dong)

# --- Hiển thị danh sách ban đầu ---
load_data()

root.mainloop()

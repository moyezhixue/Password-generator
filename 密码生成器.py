import tkinter as tk
from tkinter import messagebox, simpledialog
import secrets
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("密码长度必须大于0")
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_password = ''.join(secrets.choice(characters) for i in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, secure_password)
    except ValueError as e:
        messagebox.showerror("错误", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("复制成功", "密码已复制到剪贴板")

def password_strength():
    password = password_entry.get()
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength = 0
    if length >= 8: strength += 1
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_digit: strength += 1
    if has_special: strength += 1

    strength评定 = ["非常弱", "弱", "中等", "强", "非常强"]
    strength = min(strength, len(strength评定) - 1)
    messagebox.showinfo("密码强度", f"密码强度: {strength评定[strength]}")

# 创建主窗口
root = tk.Tk()
root.title("密码生成器")

# 创建UI元素
length_label = tk.Label(root, text="密码长度:")
length_label.pack()

length_entry = tk.Entry(root, width=50)
length_entry.pack()

generate_button = tk.Button(root, text="生成密码", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root, width=50)
password_entry.pack()

copy_button = tk.Button(root, text="复制密码", command=copy_to_clipboard)
copy_button.pack()

strength_button = tk.Button(root, text="检查密码强度", command=password_strength)
strength_button.pack()

# 运行主循环
root.mainloop()

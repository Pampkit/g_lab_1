import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Оформление заказа")
root.geometry('500x500')

conn = sqlite3.connect('SQLiteStudio.db')
cursor = conn.cursor()


def add_products():
    selected_product = combo.get()
    selected_buyers = combo1.get()
    if selected_product:
        cursor.execute("SELECT id_buy FROM buyers WHERE fio = ?", (selected_buyers,))
        buyers_id = cursor.fetchone()[0]

        cursor.execute("SELECT id_prod FROM products WHERE titl = ?", (selected_product,))
        product_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO products_has_buyers (date, products_id_prod, buyers_id_buy) VALUES (?,?,?)",
                       ("02.04.2020", product_id, buyers_id))
        conn.commit()
        messagebox.showinfo("Успешно")
    else:
        messagebox.showinfo("Выберите товар из списка")


def get_products_from_database():
    cursor.execute("SELECT titl FROM products")
    products = cursor.fetchall()
    return [product[0] for product in products]


def get_buyers_from_database():
    cursor.execute("SELECT fio FROM buyers")
    buyers = cursor.fetchall()
    return [buyers[0] for buyers in buyers]


buyers = get_buyers_from_database()
combo1 = ttk.Combobox(root, values=buyers)
combo1.pack(pady=10)

products = get_products_from_database()
combo = ttk.Combobox(root, values=products)
combo.pack(pady=10)

add_button = tk.Button(root, text="add tovar", command=add_products)
add_button.pack()
root.mainloop()

import sqlite3
from datetime import datetime

class PasswordDatabase:


    def _init_(self, db_name="passwords.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()

    def insert_password(self, site, username, password):
        self.cursor.execute('''
            INSERT INTO passwords (site, username, password, created_at)
            VALUES (?, ?, ?, ?)
        ''', (site, username, password, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.connection.commit()

    def get_all_passwords(self):
        self.cursor.execute('SELECT * FROM passwords')
        return self.cursor.fetchall()

    def get_password_by_id(self, password_id):
        self.cursor.execute('SELECT * FROM passwords WHERE id=?', (password_id,))
        return self.cursor.fetchone()

    def update_password(self, password_id, new_password):
        self.cursor.execute('''
            UPDATE passwords
            SET password=?, created_at=?
            WHERE id=?
        ''', (new_password, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), password_id))
        self.connection.commit()

    def delete_password(self, password_id):
        self.cursor.execute('DELETE FROM passwords WHERE id=?', (password_id,))
        self.connection.commit()

    def search_by_site(self, site):
        self.cursor.execute("SELECT * FROM passwords WHERE site LIKE ?", ('%' + site + '%',))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()




        import tkinter as tk
from tkinter import messagebox, simpledialog
from database import PasswordDatabase
from generator import PasswordGenerator

class PasswordManagerApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.db = PasswordDatabase()
        self.generator = PasswordGenerator()

        self.setup_ui()

    def setup_ui(self):
        # Entry fields
        tk.Label(self.master, text="Site:").grid(row=0, column=0)
        tk.Label(self.master, text="Username:").grid(row=1, column=0)
        self.site_entry = tk.Entry(self.master)
        self.username_entry = tk.Entry(self.master)
        self.site_entry.grid(row=0, column=1)
        self.username_entry.grid(row=1, column=1)

        # Password length slider
        tk.Label(self.master, text="Password Length").grid(row=2, column=0)
        self.length_slider = tk.Scale(self.master, from_=6, to=32, orient=tk.HORIZONTAL)
        self.length_slider.set(12)
        self.length_slider.grid(row=2, column=1)



   # Checkboxes
        self.upper_var = tk.IntVar(value=1)
        self.lower_var = tk.IntVar(value=1)
        self.digit_var = tk.IntVar(value=1)
        self.special_var = tk.IntVar(value=1)

        tk.Checkbutton(self.master, text="Uppercase", variable=self.upper_var).grid(row=3, column=0)
        tk.Checkbutton(self.master, text="Lowercase", variable=self.lower_var).grid(row=3, column=1)
        tk.Checkbutton(self.master, text="Digits", variable=self.digit_var).grid(row=4, column=0)
        tk.Checkbutton(self.master, text="Special", variable=self.special_var).grid(row=4, column=1)


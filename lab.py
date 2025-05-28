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




  def update_password(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            messagebox.showwarning("Warning", "Please select a password to update.")
            return

        new_password = simpledialog.askstring("Update", "Enter new password:")
        if new_password:
            self.db.update_password(self.selected_id, new_password)
            messagebox.showinfo("Updated", "Password updated successfully.")
            self.view_all_passwords()

    def delete_password(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            messagebox.showwarning("Warning", "Please select a password to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this password?")
        if confirm:
            self.db.delete_password(self.selected_id)
            messagebox.showinfo("Deleted", "Password deleted.")
            self.view_all_passwords()




  def update_password(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            messagebox.showwarning("Warning", "Please select a password to update.")
            return

        new_password = simpledialog.askstring("Update", "Enter new password:")
        if new_password:
            self.db.update_password(self.selected_id, new_password)
            messagebox.showinfo("Updated", "Password updated successfully.")
            self.view_all_passwords()

    def delete_password(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            messagebox.showwarning("Warning", "Please select a password to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this password?")
        if confirm:
            self.db.delete_password(self.selected_id)
            messagebox.showinfo("Deleted", "Password deleted.")
            self.view_all_passwords()


            import tkinter as tk
from ui import PasswordManagerApp

if _name_ == "_main_":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
        



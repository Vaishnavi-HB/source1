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



             # Buttons
        tk.Button(self.master, text="Generate Password", command=self.generate_password).grid(row=5, column=0)
        self.generated_password = tk.Entry(self.master, width=30)
        self.generated_password.grid(row=5, column=1)

        tk.Button(self.master, text="Save Password", command=self.save_password).grid(row=6, column=0)
        tk.Button(self.master, text="View All", command=self.view_all_passwords).grid(row=6, column=1)
        tk.Button(self.master, text="Search", command=self.search_password).grid(row=7, column=0)

        self.result_box = tk.Listbox(self.master, width=80)
        self.result_box.grid(row=8, column=0, columnspan=2)
        self.result_box.bind('<<ListboxSelect>>', self.select_password)

        # Delete and Update Buttons
        tk.Button(self.master, text="Update Password", command=self.update_password).grid(row=9, column=0)
        tk.Button(self.master, text="Delete", command=self.delete_password).grid(row=9, column=1)






 def generate_password(self):
        try:
            self.generator.set_length(self.length_slider.get())
            self.generator.configure(
                upper=self.upper_var.get(),
                lower=self.lower_var.get(),
                digits=self.digit_var.get(),
                special=self.special_var.get()
            )
            password = self.generator.generate()
            self.generated_password.delete(0, tk.END)
            self.generated_password.insert(0, password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def save_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.generated_password.get()

        if not (site and username and password):
            messagebox.showwarning("Warning", "Please fill all fields.")
            return

        self.db.insert_password(site, username, password)
        messagebox.showinfo("Success", "Password saved successfully.")



 def view_all_passwords(self):
        self.result_box.delete(0, tk.END)
        for row in self.db.get_all_passwords():
            self.result_box.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    def search_password(self):
        site = simpledialog.askstring("Search", "Enter site name to search:")
        if site:
            results = self.db.search_by_site(site)
            self.result_box.delete(0, tk.END)
            for row in results:
                self.result_box.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    def select_password(self, event):
        try:
            selection = self.result_box.get(self.result_box.curselection())
            fields = selection.split(" | ")
            self.selected_id = int(fields[0])
        except:
            self.selected_id = None



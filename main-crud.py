"""CRUD with Tkinter"""

import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class MainApplication:
    """Create Application"""

    def __init__(self, window):
        """run on initialization of class"""

        self.db_name = 'database.db'

        self.window = window
        self.window.title('Contacts - CRUD')

        # Frame container
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, columnspan=6, pady=20)

        # ID textbox
        tk.Label(self.frame, text='Code: ').grid(sticky=tk.W, row=1, column=0)
        self.code_var = tk.StringVar()
        self.code = tk.Entry(self.frame, width=7, state='disabled', textvariable=self.code_var).grid(sticky=tk.W,
                                                                                                     row=1, column=1)

        # Name textbox
        tk.Label(self.frame, text='Name: ').grid(sticky=tk.W, row=2, column=0)
        self.name_var = tk.StringVar()
        self.name = tk.Entry(self.frame, width=26, textvariable=self.name_var).grid(row=2, column=1)

        # Phone textbox
        tk.Label(self.frame, text='Phone: ').grid(sticky=tk.W, row=3, column=0)
        self.phone_var = tk.StringVar()
        self.phone = tk.Entry(self.frame, width=26, textvariable=self.phone_var).grid(row=3, column=1)

        # City textbox
        tk.Label(self.frame, text='City: ').grid(sticky=tk.W, row=4, column=0)
        self.city_var = tk.StringVar()
        self.city = tk.Entry(self.frame, width=26, textvariable=self.city_var).grid(row=4, column=1)

        # Email textbox
        tk.Label(self.frame, text='Email: ').grid(sticky=tk.W, row=5, column=0)
        self.email_var = tk.StringVar()
        self.email = tk.Entry(self.frame, width=26, textvariable=self.email_var).grid(row=5, column=1)

        # Buttons
        self.create = tk.Button(self.frame, text='Create', command=self.create, width=10).grid(row=6, column=1,
                                                                                               sticky=tk.W)
        self.update = tk.Button(self.frame, text='Update', command=self.update, width=10).grid(row=6, column=1,
                                                                                               sticky=tk.E)
        self.delete = tk.Button(self.frame, text='Delete', command=self.delete, width=10).grid(row=7, column=1,
                                                                                               sticky=tk.W)
        self.clear = tk.Button(self.frame, text='Clear', command=self.clean_textbox, width=10).grid(row=7, column=1,
                                                                                                    sticky=tk.E)

        # Tree widget
        self.tree = ttk.Treeview(height=10, columns=("Code", "Name", "Phone", "City", "Email"),
                                 style="mystyle.Treeview")
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bg=0)
        self.tree.grid(row=8, column=0, columnspan=2, pady=10, padx=10)
        self.tree.bind("<Double-1>", self.on_double_click)  # Bind double click event to the table tree
        self.tree.heading('#0', text='Code', anchor=tk.CENTER)
        self.tree.column("#0", width=45, minwidth=45)
        self.tree.heading('#1', text='Name', anchor=tk.CENTER)
        self.tree.column("#1", width=200, minwidth=200)
        self.tree.heading('#2', text='Phone', anchor=tk.CENTER)
        self.tree.column("#2", width=100, minwidth=100)
        self.tree.heading('#3', text='City', anchor=tk.CENTER)
        self.tree.column("#3", width=130, minwidth=130)
        self.tree.heading('#4', text='Email', anchor=tk.CENTER)
        self.tree.column("#4", width=150, minwidth=150)

        self.get_contacts()

    def run_query(self, query, parameters=()):
        """Run queries in db file"""

        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            result = cur.execute(query, parameters)
            conn.commit()
        return result

    def on_double_click(self, event):
        """On double click event populate all textbox"""

        self.code_var.set(self.tree.item(self.tree.selection())['text'])
        self.name_var.set(self.tree.item(self.tree.selection())['values'][0])
        self.phone_var.set(self.tree.item(self.tree.selection())['values'][1])
        self.city_var.set(self.tree.item(self.tree.selection())['values'][2])
        self.email_var.set(self.tree.item(self.tree.selection())['values'][3])
        return

    def clean_tree(self):
        """Clean table tree"""

        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        return

    def get_contacts(self):
        """ Get all values from table and populate the tree widget"""

        self.clean_tree()
        query = 'SELECT * FROM Inventario ORDER BY ID DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], value=row[1:])
        return

    def clean_textbox(self):
        """Clean all text box"""

        self.code_var.set("")
        self.name_var.set("")
        self.phone_var.set("")
        self.city_var.set("")
        self.email_var.set("")
        return

    def check_parameters(self):
        """Check if not empty fields"""

        if len(self.name_var.get()) != 0 and len(self.phone_var.get()) != 0 and len(self.city_var.get()) != 0 \
                and len(self.email_var.get()) != 0:
            return True
        return False

    def create(self):
        """Insert value into db"""

        if len(self.code_var.get()) == 0:
            if self.check_parameters():
                query = 'INSERT INTO Inventario VALUES (NULL, ?, ?, ?, ?)'
                parameters = (self.name_var.get()), (self.phone_var.get()), (self.city_var.get()),\
                             (self.email_var.get())
                self.run_query(query, parameters)
                self.clean_textbox()
                self.get_contacts()
                tk.messagebox.showinfo(title="OK", message="Created")
                return
            else:
                tk.messagebox.showerror(title="Error", message="Error. Missing values")
                return
        else:
            tk.messagebox.showerror(title="Error", message="Unable to create because tree item was selected."
                                                           " Clean textbox and try again.")
            return

    def update(self):
        """update selected value"""

        if len(self.code_var.get()) != 0:
            if self.check_parameters():
                query = 'UPDATE Inventario SET Nombre = ?, Telefono = ?, Ciudad = ?, Email = ? WHERE ID = ?'
                parameters = (self.name_var.get()), (self.phone_var.get()), (self.city_var.get()), \
                             (self.email_var.get()), (self.code_var.get())
                self.run_query(query, parameters)
                self.clean_textbox()
                self.get_contacts()
                tk.messagebox.showinfo(title="OK", message="Updated")
                return
            else:
                tk.messagebox.showerror(title="Error", message="Some textbox may be left empty")
                return
        else:
            tk.messagebox.showerror(title="Error", message="Unable to update because NO tree item was selected.")
            return

    def delete(self):
        """delete selected value"""

        if len(self.code_var.get()) != 0:
            if self.check_parameters():
                query = 'DELETE FROM Inventario WHERE ID =' + str(self.code_var.get())
                self.run_query(query)
                self.clean_textbox()
                self.get_contacts()
                tk.messagebox.showinfo(title="OK", message="Deleted")
                return
            else:
                tk.messagebox.showerror(title="Error", message="Some textbox may be left empty")
                return
        else:
            tk.messagebox.showerror(title="Error", message="Unable to delete because NO tree item was selected.")
            return


def main():
    """Create Main Window"""

    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()

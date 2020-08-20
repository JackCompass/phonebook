"""creating a demo gui application for phonebook"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Phonebook")


"""Creating labels in regarding the phonebook command line software"""

lb_name = ttk.Label(root, text = "Name")
lb_name.grid(row = 0, column = 0, sticky = tk.W)
lb_phno = ttk.Label(root, text = "Phone")
lb_phno.grid(row = 1, column = 0, sticky = tk.W)
lb_email = ttk.Label(root, text = "Email")
lb_email.grid(row = 2, column = 0, sticky = tk.W)

"""Creating entry box for taking values from the user."""
box_name = ttk.Entry(root, width = 20)
box_name.focus()
box_name.grid(row = 0, column = 1)
box_phno = ttk.Entry(root, width = 20)
box_phno.grid(row = 1, column = 1)

"""Submit button"""
submit_btn = ttk.Button(root, text = 'Submit')
submit_btn.grid(row = 3, column = 1)

"""combobox button"""
Cbox_email = ttk.Combobox(root, width = 17, values =['NULL'])
Cbox_email.current(0)
Cbox_email.grid(row = 2, column = 1)

"""Adding a radio button"""
ttk.Radiobutton(root, text = 'Add Contact', value = 1).grid(row = 4, column = 0, sticky = tk.W)
ttk.Radiobutton(root, text = 'Modify Contact', value = 2).grid(row = 5, column = 0, sticky = tk.W)
ttk.Radiobutton(root, text = 'Delete Contact', value = 3).grid(row = 6, column = 0, sticky = tk.W)
ttk.Radiobutton(root, text = 'Search Contact', value = 4).grid(row = 7, column = 0, sticky = tk.W)
ttk.Radiobutton(root, text = 'Import CSV', value = 5).grid(row = 8, column = 0, sticky = tk.W)
ttk.Radiobutton(root, text = 'Export CSV', value = 6).grid(row = 9, column = 0, sticky = tk.W)



"""It keep the app open until user close it."""
root.mainloop()

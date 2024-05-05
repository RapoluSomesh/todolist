import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task != "":
        listbox = tk.Listbox(root, width=120, height=2, font=('ariel', 8, 'bold'))
        listbox.grid(row=len(listbox_list) + 5, column=0, padx=5, pady=5)
        listbox.insert(tk.END, task)
        listbox_list.append(listbox)
        entry.delete(0, tk.END)
        update_buttons()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task(listbox):
    listbox.grid_forget()
    listbox_list.remove(listbox)
    update_buttons()


def edit_task(listbox):
    try:
        edited_task = entry.get()
        if edited_task != "":
            last_task_index = listbox.size() - 1
            listbox.delete(last_task_index)
            listbox.insert(last_task_index, edited_task)
            entry.delete(0, tk.END)
            success_label.config(text="Text edited successfully")
            root.after(2000, clear_success_message)  # Remove success message after 2 seconds

        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")


def update_buttons():
    for i, listbox in enumerate(listbox_list):
        edit_button = tk.Button(listbox, text="Edit", command=lambda lb=listbox: edit_task(lb),
                                bg='green', fg='white', bd=3)
        edit_button.place(relx=0.8, rely=1, anchor="se")
        delete_button = tk.Button(listbox, text="Delete", command=lambda lb=listbox: delete_task(lb),
                                  bg='red', fg='white', bd=3)
        delete_button.place(relx=1, rely=1, anchor="se")


def clear_success_message():
    success_label.config(text="")


# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry('1000x700+300+50')
root.resizable(0, 0)

# Create todolist label
todo_label = tk.Label(root, text="   ToDo List", bg="green", fg="black", font=("Arial", 30), padx=10, pady=10, width=43,
                      anchor='w', height=3)
todo_label.grid(row=0, column=0, columnspan=3, sticky="ew")

# Create add item label
add_item = tk.Label(root, text='Add Items', font=('ariel', 20, 'bold'), anchor='w')
add_item.grid(row=1, ipadx=280, pady=20)

# Create success message label
success_label = tk.Label(root, text="", fg="green")
success_label.grid(row=1, column=1, columnspan=2, sticky="w")

# Create entry widget
entry = tk.Entry(root, font=('ariel', 18))
entry.grid(row=2, column=0, ipadx=230, pady=5, columnspan=1)

# Create submit button
submit_button = tk.Button(root, text="submit", command=add_task, bg='black', fg='white', height=2, width=8,
                          font=('ariel', 9), bd=3)
submit_button.grid(row=2, column=1, padx=5, pady=5)

# create task label
task_label = tk.Label(root, text='Tasks', font=('ariel', 20, 'bold'))
task_label.grid(row=3, padx=5)

# List to store all listboxes
listbox_list = []

# Run the application
root.mainloop()

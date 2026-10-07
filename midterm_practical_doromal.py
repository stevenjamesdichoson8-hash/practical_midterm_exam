import tkinter as tk
from tkinter import messagebox

records = []

def add_record():
    name = entry_name.get()
    age = entry_age.get()
    genre = entry_genre.get()

    if not name or not age or not genre:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    records.append({"name": name, "age": age, "genre": genre})
    refresh_output()
    clear_fields()

def update_record():
    name = entry_name.get()
    age = entry_age.get()
    genre = entry_genre.get()

    if not name:
        messagebox.showwarning("Missing Info", "Enter the artist name to update.")
        return

    for rec in records:
        if rec["name"] == name:
            rec["age"] = age
            rec["genre"] = genre
            refresh_output()
            clear_fields()
            return

    messagebox.showinfo("Not Found", f"No record found for '{name}'.")

def delete_record():
    name = entry_name.get()

    if not name:
        messagebox.showwarning("Missing Info", "Enter the artist name to delete.")
        return

    for rec in records:
        if rec["name"] == name:
            records.remove(rec)
            refresh_output()
            clear_fields()
            return

    messagebox.showinfo("Not Found", f"No record found for '{name}'.")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_genre.delete(0, tk.END)

def refresh_output():
    output.delete("1.0", tk.END)
    for rec in records:
        output.insert(tk.END, "Song Artist Information\n")
        output.insert(tk.END, f"Name: {rec['name']}\n")
        output.insert(tk.END, f"Age: {rec['age']}\n")
        output.insert(tk.END, f"Genre: {rec['genre']}\n")
        output.insert(tk.END, "-" * 30 + "\n")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Song Artist Information System")
root.geometry("400x500")

tk.Label(root, text="Artist Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(root, width=25)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Genre:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_genre = tk.Entry(root, width=25)
entry_genre.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Add", width=10, command=add_record).grid(row=3, column=0, padx=5, pady=10)
tk.Button(root, text="Update", width=10, command=update_record).grid(row=3, column=1, padx=5, pady=10)
tk.Button(root, text="Delete", width=10, command=delete_record).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Clear", width=10, command=clear_fields).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Exit", width=22, command=exit_app).grid(row=5, column=0, columnspan=2, pady=5)

output = tk.Text(root, width=45, height=15)
output.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

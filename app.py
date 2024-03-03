import tkinter as tk
from tkinter import messagebox

class Worker:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class WorkerDatabase:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def search_workers(self, skill):
        matched_workers = []
        for worker in self.workers:
            if worker.skill == skill:
                matched_workers.append(worker)
        return matched_workers

def search_workers():
    skill = skill_entry.get()
    matched_workers = database.search_workers(skill)
    if matched_workers:
        worker_listbox.delete(0, tk.END)
        for worker in matched_workers:
            worker_listbox.insert(tk.END, f"Name: {worker.name}, Skill: {worker.skill}")
    else:
        messagebox.showinfo("No Workers Found", "No workers found with that skill.")

def exit_app():
    root.destroy()

database = WorkerDatabase()

# Add some sample workers to the database
database.add_worker(Worker("John", "Electrician"))
database.add_worker(Worker("Alice", "Plumber"))
database.add_worker(Worker("Bob", "Painter"))

root = tk.Tk()
root.title("Household Worker Connect App")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

skill_label = tk.Label(frame, text="Enter the skill you are looking for:")
skill_label.grid(row=0, column=0, padx=5, pady=5)

skill_entry = tk.Entry(frame)
skill_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text="Search", command=search_workers)
search_button.grid(row=0, column=2, padx=5, pady=5)

worker_listbox = tk.Listbox(frame, width=40, height=10)
worker_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

exit_button = tk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()

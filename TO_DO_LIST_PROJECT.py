import tkinter as tk

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")

        # Create task list and status variables
        self.tasks = []
        self.statuses = {}

        # Create widgets
        self.task_entry = tk.Entry(self, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(self, width=50)
        self.task_list.pack()

        self.mark_done_button = tk.Button(self, text="Mark Done", command=self.mark_done)
        self.mark_done_button.pack()

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_task)
        self.delete_button.pack()

        # Update task list when the window is opened
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.statuses[task] = False  # Mark new task as not done
            self.update_task_list()
            self.task_entry.delete(0, tk.END)  # Clear the entry field

    def update_task_list(self):
        self.task_list.delete(0, tk.END)  # Clear the listbox
        for task, status in self.statuses.items():
            if status:
                self.task_list.insert(tk.END, f"{task} (Done)")
            else:
                self.task_list.insert(tk.END, task)

    def mark_done(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.task_list.get(selected_index)
            self.statuses[task] = True
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.task_list.get(selected_index)
            del self.tasks[self.tasks.index(task)]
            del self.statuses[task]
            self.update_task_list()

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()

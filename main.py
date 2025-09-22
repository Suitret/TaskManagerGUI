import tkinter as tk
from ui import TaskManagerGUI
from storage import Storage
from config import DATA_FILE

def main():
    root = tk.Tk()
    storage = Storage(DATA_FILE)
    app = TaskManagerGUI(root, storage)
    root.mainloop()

if __name__ == "__main__":
    main()

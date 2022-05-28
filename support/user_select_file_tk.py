import tkinter as tk
from tkinter import filedialog


def select_files(filetypes, window_title="Open", onefile=True):
    root = tk.Tk()
    root.withdraw()
    root.title(window_title)
    if onefile:
        return filedialog.askopenfilename(filetypes=filetypes)
    else:
        return filedialog.askopenfilenames()


if __name__ == "__main__":
    select_files([("CSV Files", "*.csv")])

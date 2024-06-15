import os.path
from difflib import Differ
import pandas as pd
from functions import load_and_compare
import tkinter as tk
from tkinter import filedialog

file_path = []
def select_and_store_file():
    global file_path
    selected_file = filedialog.askopenfilenames()
    if selected_file:
        try:
            file_path = list(selected_file)
            print("Paths: ", file_path)
            for i, path in enumerate(file_path):
                path_lbl = tk.Label(main_window, text=f"Path {i+1}: {path}")
                path_lbl.pack()

            load_and_compare(file_path[0], file_path[1])
        except Exception as e:
            print(f"Reading file loc error: {e}")



main_window = tk.Tk()
main_window.title("DiffProj - Main Window")
main_window.geometry("400x300")

title_lbl = tk.Label(main_window, text="Difference Delta - Please select two files:")
title_lbl.pack()

basefile_btn = tk.Button(main_window, text="Select the files (first the base and later the other one)", command=select_and_store_file)
basefile_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, anchor=tk.S)

main_window.mainloop()
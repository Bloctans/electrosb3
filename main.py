import sys
import electrosb3
from tkinter import filedialog

file = filedialog.askopenfilename(filetypes=[["Scratch Projects","sb3"], ["PenguinMod Projects","pmp"]])

if __name__ == "__main__":
    e = electrosb3.Electro(file)
    e.start_window()
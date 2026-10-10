import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

f = 1

messagebox.showinfo("None", "привет!, я ZERO")
if messagebox.askyesno("None", "ты готов?"):
  messagebox.showinfo("None", "хорошо!")
else:
  while not messagebox.askyesno("None", f"ты готов{f*'!'}"):
    if f < 20:
      f += 1
    else:
      messagebox.showinfo("None", "почему?")
      messagebox.showinfo("None", "ты готов?")
      break
  else:
    messagebox.showinfo("None", "хорошо!")
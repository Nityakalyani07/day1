from tkinter import Tk, Label
import time

root = Tk()
root.title("Cute Clock")

def get_time():
    time_str = time.strftime("%H:%M:%S %p")
    label.config(text=time_str)
    label.after(1000, get_time)

label = Label(root, font=("Courier", 40), background="pink", foreground="white")
label.pack(anchor='center')
get_time()
root.mainloop()

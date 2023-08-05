from tkinter import *

root = Tk()  # create a root widget
root.title("Tk Example")
root.configure(background="white")
root.minsize(1920, 1080)  # width, height
root.maxsize(1920, 1080)
root.geometry("300x300+50+50")  # width x height + x + y
image = PhotoImage(file="test.png")
root.mainloop()
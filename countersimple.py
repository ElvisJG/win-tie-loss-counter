import tkinter
import sys

root = tkinter.Tk()
root.geometry("200x200")
root.title("His Button Increaser")

counter = tkinter.IntVar()

def onClick(event=None):
    counter.set(counter.get() + 1)
def onClickD(event=None):
    counter.set(counter.get() - 1)
def clear(event=None):
    counter.set(0)

tkinter.Label(root, textvariable=counter).pack()
tkinter.Button(root, text="Increase", command=onClick, fg="dark green", bg = "white").pack()
tkinter.Button(root, text="Decrease", command=onClickD, fg="dark green", bg = "white").pack()
tkinter.Button(root, text="Clear", command=clear, fg="dark green", bg = "white").pack()

root.mainloop()
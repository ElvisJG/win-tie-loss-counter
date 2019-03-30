import tkinter as tkinter
import sys
import os

root = tkinter.Tk()

winCounter = tkinter.IntVar()
tieCounter = tkinter.IntVar()
loseCounter = tkinter.IntVar()

def countUp(counter):
    counter.set(counter.get() + 1)
    counter4file = str((counter.get() + 1) - 1)
    if counter == winCounter:
        file = open("winsCounter.txt","w+")
        file.write(counter4file)
        file.close()
    elif counter == loseCounter:
        file = open("loseCounter.txt","w+")
        file.write(counter4file)
        file.close()
    else:
        file = open("tiesCounter.txt","w+")
        file.write(counter4file)
        file.close()

def countDown(counter):
    counter.set(counter.get() - 1)
    counter4file = str((counter.get() - 1) + 1)
    if counter == winCounter:
        file = open("winsCounter.txt","w+")
        file.write(counter4file)
        file.close()
    elif counter == loseCounter:
        file = open("loseCounter.txt","w+")
        file.write(counter4file)
        file.close()
    else:
        file = open("tiesCounter.txt","w+")
        file.write(counter4file)
        file.close()

def countClear(event=None):
    winCounter.set(0)
    loseCounter.set(0)
    tieCounter.set(0)
    zeroOut = "0"
    file1 = open("winsCounter.txt","w+")
    file2 = open("loseCounter.txt","w+")
    file3 = open("tiesCounter.txt","w+")
    file1.write(zeroOut)
    file2.write(zeroOut)
    file3.write(zeroOut)
    file1.close()
    file2.close()
    file3.close()
    #os.remove("winsCounter.txt")
    #os.remove("tiesCounter.txt")
    #os.remove("loseCounter.txt")

tkinter.Label(root, textvariable=winCounter, fg = "white", bg ="green", font = "Verdana 30 bold").pack()
tkinter.Label(root, textvariable=tieCounter, fg = "white", bg ="green", font = "Verdana 30 bold").pack()
tkinter.Label(root, textvariable=loseCounter, fg = "white", bg ="green", font = "Verdana 30 bold").pack()

winUp = tkinter.Button(root, text="Win +1", command=lambda: countUp(winCounter)).pack()
winDown = tkinter.Button(root, text="Win -1", command=lambda: countDown(winCounter)).pack()
tieUp = tkinter.Button(root, text="Tie +1", command=lambda: countUp(tieCounter)).pack()
tieDown = tkinter.Button(root, text="Tie -1", command=lambda: countDown(tieCounter)).pack()
loseUp = tkinter.Button(root, text="Lose +1", command=lambda: countUp(loseCounter)).pack()
loseDown = tkinter.Button(root, text="Lose -1", command=lambda: countDown(loseCounter)).pack()
clearAll = tkinter.Button(root, text="CLEAR!!", command=lambda: countClear()).pack()

root.bind("<Control-q>", lambda event: countUp(winCounter))
root.bind("<Control-w>", lambda event: countDown(winCounter))
root.bind("<Control-a>", lambda event: countUp(tieCounter))
root.bind("<Control-s>", lambda event: countDown(tieCounter))
root.bind("<Control-z>", lambda event: countUp(loseCounter))
root.bind("<Control-x>", lambda event: countDown(loseCounter))
root.bind("<Control-f>", lambda event: countClear())

root.mainloop()
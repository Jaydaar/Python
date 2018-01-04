# import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

# Showing the pack manager

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+8+400")

label = tkinter.Label(mainWindow, text='Hello World')
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='top')

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.pack(side='left', anchor='n')
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')

mainWindow.mainloop()
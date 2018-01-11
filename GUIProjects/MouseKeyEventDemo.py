from tkinter import Tk, Canvas

class MouseKeyEventDemo:
    """
        Creates a canvas where you can know the key pressed and the 
        mouse button event with its location.
    """
    def __init__(self):
        window = Tk() # Create a window
        window.title("Event Demo") # Set a title
        canvas = Canvas(window, bg="white", width=200, height=100)
        canvas.pack()

        # Bind with <Button-1> event
        canvas.bind("<Button-1>", self.processMouseEvent)

        # Bind with <Key> event
        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set()

        window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        print("Clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked?", event.num)

    def processKeyEvent(self, event):
        print("Keysym? ", event.keysym)
        print("Char? ", event.char)
        print("Keycode? ", event.keycode)

MouseKeyEventDemo() # Create GUI

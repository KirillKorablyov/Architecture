
from tkinter import Tk, Frame, BOTH

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("GUI")
        self.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry("600x600")
    app = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()

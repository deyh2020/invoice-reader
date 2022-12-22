from tkinter import *
import tkinter as tk
import tkinter.messagebox
import sys

class CreateWindow(tk.Tk):

    def __init__(self):
        #super().__init__(screenName=screenName, baseName=baseName, className, useTk=useTk, sync=sync, use=use)
        tk.Tk.__init__(self)

        self.floater = HomeWindow(self)
        self.withdraw()




class HomeWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        #super().__init__(master=master, cnf, **kw)
        tk.Toplevel.__init__(self, *args, **kwargs)

        # Sets size of window
        self.geometry("960x540")

        # Sets title of window
        self.title("  Invoice To Spreadsheet")

        # Sets window icon
        self.iconbitmap('')

        # Create UI Components
        self.createUIComponents()

        # Initialise UI layout
        self.initUI()

    # Defines components
    def createUIComponents(self):

        
        self.buttonLayout = Frame(self, bg = "red")

        #self.selectFileButton = Button(self.buttonLayout, text = "File", command = self.selectFile, borderwidth = 0, width = '50', height = '10', bg = "grey", fg = "white", activebackground = "gray")
        #self.selectFolderButton = Button(self.buttonLayout, text = "File", command = self.selectFolder, borderwidth = 0, width = '50', height = '10', bg = "grey", fg = "white", activebackground = "gray")

        pass

    # Initialises UI
    def initUI(self):

        self.buttonLayout.pack(fill = Y)

        #self.selectFileButton.pack(side = RIGHT, fill = Y)
        #self.selectFolderButton.pack(side = RIGHT, fill = Y)

        


    def selectFile(self):

        pass

    def selectFolder(self):

        pass


class SettingsWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        #super().__init__(master=master, cnf, **kw)
        tk.Toplevel.__init__(self, *args, **kwargs)




def askToQuit():

    if tk.messagebox.askokcancel("Quit", "Are You Sure You Want To Quit?"):
        
        root.destroy()




root = CreateWindow()
root.protocol("WM_DELETE_WINDOW", askToQuit)
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
root.destroy()
    
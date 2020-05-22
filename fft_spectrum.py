import tkinter as tk  # 1 imports
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import HISTORY
from HISTORY import *
import tab3
from tab3 import *
from threading import Thread
import time
from queue import Queue

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
#tao duc day
# commiy lan 2
#LAN3
#lan4
class OPP():
    def useQueues(self):
        guiQueue = Queue()

    def methodInAThread(self, clgt=10):
        print('Hi, how are you?')
        for idx in range(clgt):
            time.sleep(2)
            self.scr.insert(tk.INSERT, str(idx) + '\n')

            print('methodInAThread():', self.thread1.is_alive())

    def __init__(self):
        self.win = tk.Tk()  # 2 Create instance
        self.win.iconbitmap(r"C:\Users\Admin\Desktop\vibration\icon.ico")
        self.win.title("VIBRATION FFT SPECTRUM")  # 3 Add a title
        self.win.geometry("400x400")
        self.win.resizable(1, 1)  # 4 Disable resizing the GUI
        self.creatWidget()

    def changecolor(self):
        color = self.ratio1.get()
        if (color == 0): self.lb.configure(foreground='red')
        if (color == 1): self.lb.configure(foreground='blue')
        if (color == 2): self.lb.configure(foreground='white')

    def click(self):
        self.action.configure(text="DONE" + self.numberChosen.get())
        # lb.configure(foreground='red')
        spinValue = self.spin.get()
        # scr.delete(1.0,tk.END)
        self.scr.insert(tk.END, str(spinValue) + "\n")
        self.creatThread()
        # for idx in range(10):
        #     time.sleep(1)
        #     self.scr.insert(tk.INSERT, str(idx) + '\n')

    def creatThread(self):
        self.thread1 = Thread(target=self.methodInAThread, args=[5])
        self.thread1.start()
        print(self.thread1)
        print(self.thread1)
        print('createThread():', self.thread1.is_alive())

    # --------------------------------MESSAGE BOX----------------------------------------

    def _msgBox(self):
        feedback = mBox.askyesno("COULD NOT RECEIVE DATA", " CONNECT THE SENSOR \n ACCELERATION")

        if feedback == True:
            count = 0
            while (count < 100):
                self.scr.insert(tk.END, "The count is: " + str(count) + "\n")

                # Pushes the scrollbar and focus of text to the end of the text input.
                self.scr.yview(tk.END)
                count += 1

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def creatWidget(self):
        self.tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(self.tabControl)
        tab2 = ttk.Frame(self.tabControl)
        self.tab3 = TAB3._creatTab3(self.tabControl)

        self.tabControl.add(tab1, text="SIGNAL AND SPECTRUM")
        self.tabControl.add(tab2, text="PREDICTION")
        self.tabControl.add(self.tab3, text="LOVE")

        self.tabControl.pack(expand=1, fill="both")

        self.lb = ttk.Label(tab1, text="Enter a name: ")
        self.lb.grid(column=0, row=0, sticky=tk.W, padx=20, pady=1)  # 5

        self.labelFrame = ttk.LabelFrame(tab1, text="Label frame")
        self.labelFrame.grid(column=0, row=10, padx=20, pady=10)

        self.lableFrame0 = ttk.LabelFrame(tab1, text="NHAP SO LIEU")
        self.lableFrame0.grid(column=0, row=1, sticky=tk.W)

        self.lableFrame1 = ttk.LabelFrame(tab1, text="OPTION")
        self.lableFrame1.grid(column=0, row=2, sticky=tk.W)

        name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.lableFrame0, width=12, textvariable=name)
        self.nameEntered.grid(column=0, row=0, sticky=tk.W, padx=10, pady=1)
        self.nameEntered.focus()
        createToolTip(self.nameEntered, " Nhap so lieu !")

        number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.lableFrame0, width=12, textvariable=number, state="readonly")
        self.numberChosen["values"] = (1, 2, 3, 4, 100)
        self.numberChosen.grid(column=1, row=0, padx=10, pady=1)
        self.numberChosen.current(0)

        self.spin = Spinbox(self.lableFrame0, from_=0, to=10, width=10, bd=2)
        self.spin.grid(column=2, row=0, padx=10, pady=1)

        self.action = tk.Button(tab1, text="Click Me", command=self.click)
        self.action.grid(column=1, row=10)

        chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.lableFrame1, text="Disable", variable=chVarDis, state="disable")
        self.check1.select()
        self.check1.grid(column=0, row=0, sticky=tk.W, padx=20, pady=1)

        chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.lableFrame1, text="Disable", variable=chVarUn, state="normal")
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W, padx=20, pady=1)

        chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.lableFrame1, text="Enable", variable=chVarEn, state="normal")
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W, padx=20, pady=1)

        colors = ["Red", "Blue", "White"]

        self.ratio1 = tk.IntVar()
        self.ratio1.set(10)

        for i in range(0, 3):
            ratio = "ratio" + str(i)
            ratio = tk.Radiobutton(self.labelFrame, text=colors[i], var=self.ratio1, value=i, command=self.changecolor)
            ratio.grid(column=i, row=3, sticky=tk.W)

        for child in self.labelFrame.winfo_children():
            child.grid_configure(padx=20, pady=1)
        # ratioRed=tk.Radiobutton(win,text="Color1",var=ratio1,value=1, command=changecolor)
        # ratioRed.grid(column=0,row=3,sticky=tk.W)
        #
        # ratioRed=tk.Radiobutton(win,text="Color2",var=ratio1,value=2, command=changecolor)
        # ratioRed.grid(column=1,row=3,sticky=tk.W)
        #
        # ratioRed=tk.Radiobutton(win,text="Color3",var=ratio1,value=3, command=changecolor)
        # ratioRed.grid(column=2,row=3,sticky=tk.W)

        from tkinter import scrolledtext
        scrolW = 30
        scrolH = 10
        self.scr = scrolledtext.ScrolledText(tab1, height=scrolH, width=scrolW, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, columnspan=2, sticky="WE", padx=20, pady=4)
        createToolTip(self.scr, 'This is a ScrolledText widget.')

        # ---------------MENU BAR------------------

        menuBar = Menu(self.win)

        self.win.config(menu=menuBar)

        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu1 = Menu(menuBar, tearoff=0)
        fileMenu2 = Menu(menuBar, tearoff=0)

        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Import")
        fileMenu.add_separator()
        fileMenu.add_command(label="Export")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        fileMenu.add_separator()
        menuBar.add_cascade(label="File", menu=fileMenu)

        fileMenu1.add_command(label="ABS")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="RAM")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="RMS")
        fileMenu1.add_separator()
        fileMenu1.add_command(label="Pick-Pick")
        fileMenu1.add_separator()
        menuBar.add_cascade(label="TOOL", menu=fileMenu1)

        fileMenu2.add_separator()
        fileMenu2.add_command(label="License")
        fileMenu2.add_separator()
        menuBar.add_cascade(label="ABOUT", menu=fileMenu2)

        # message box

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self._msgBox)
        menuBar.add_cascade(label="ALERT", menu=helpMenu)

        # --------------------------------TAB2----------------------------------------

        # --------------LABEL FRAME-----------------------------------------
        tab2LabelFrame = ttk.LabelFrame(tab2, text="Label frame")
        tab2LabelFrame.grid(column=0, row=10, padx=20, pady=20)

        tab2LableFrame0 = ttk.LabelFrame(tab2, text="NHAP SO LIEU")
        tab2LableFrame0.grid(column=0, row=1, sticky=tk.W)

        tab2LableFrame1 = ttk.LabelFrame(tab2, text="OPTION")
        tab2LableFrame1.grid(column=0, row=2, sticky=tk.W)

        # ---------------INPUT BOX------------------------------------------
        name = tk.StringVar()
        tab2NameEntered = ttk.Entry(tab2LableFrame0, width=12, textvariable=name)
        tab2NameEntered.grid(column=0, row=0, sticky=tk.W, padx=20, pady=1)
        tab2NameEntered.focus()

    # ---------------LOOP-----------------------------------------------
    # ---------------PLOT------------------

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # X = np.arange(-5, 5, 0.25)
    # Y = np.arange(-5, 5, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    # surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.
    #                        coolwarm, linewidth=0, antialiased=False)
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # fig.colorbar(surf, shrink=0.5, aspect=5)

    # plt.show()


opp = OPP()
runT = Thread(target=opp.methodInAThread)
# opp.win.update()
# opp.win.deiconify()
opp.win.mainloop()



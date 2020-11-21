# import sys
# if sys.version_info[0] < 3:
#     import Tkinter as tk
#     from Tkinter import filedialog as fd
# else:
#     import tkinter as tk
#     from tkinter import filedialog as fd

import sys
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mesbox
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#import gprpy.gprpy as gp
#import numpy as np
import gprpy.toolbox.splash_simple as splash
import os
# import Pmw
#import scipy.interpolate as interp




colsp=2
rightcol=9
halfwid=6
figrowsp=21+1
figcolsp=9


class GPRPyApp:
    '''
    GPRPy class for graphical user interface for GPR profile data
    '''

    def __init__(self,master):
        # self.window = master

        # # Set up for high-resolution screens
        normscrwidt=1024
        normscrhigt=768
        # scrwidt=master.winfo_screenwidth()
        # scrhigt=master.winfo_screenheight()
        # # These to use if operating system doesn't automatically adjust
        # #self.widfac=scrwidt/normscrwidt
        # #self.highfac=scrhigt/normscrhigt
        self.widfac=normscrwidt/normscrhigt
        self.highfac=1
        # fontfac=(normscrwidt/normscrhigt)/(scrwidt/scrhigt)
        
        # master.title("GPRPy")
        
        # # Variables specific to GUI
        # # self.balloon = Pmw.Balloon()
        # self.picking = False       
        # self.delimiter = None
        # self.grid = False

        # # Initialize the gprpy
        # #proj = gp.gprpyProfile()

        # # Show splash screen
        fig=Figure(figsize=(8*self.widfac,5*self.highfac))
        # a=fig.add_subplot(111)
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # splash.showSplash(a,dir_path,self.widfac,self.highfac,fontfac)

        # # # Set font size for screen res
        # # mpl.rcParams.update({'font.size': mpl.rcParams['font.size']*self.widfac})
        # # a.tick_params(direction='out',length=6*self.widfac,width=self.highfac)
        
        # # a.get_xaxis().set_visible(False)
        # # a.get_yaxis().set_visible(False)
        # canvas = FigureCanvasTkAgg(fig, master=self.window)
        # # canvas.get_tk_widget().grid(row=2,column=0,columnspan=figcolsp,rowspan=figrowsp,sticky='nsew')

        # canvas.draw() 
               
        
        ########### SOME TESTING #################
        self.window = master
        #self.canvas = tk.Canvas(master, width=450, height=500)
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        # to make a frame
        #sself.frame = tk.Frame(master, bg='white')
        canvas.pack()

        # to place a menu item in the window
        #sself.menu = tk.Menu(master)
        #smaster.config(menu=self.menu)

            
# root = tk.Tk()
    
# for col in range(rightcol):
#     root.columnconfigure(col, weight=1)
# for row in range(figrowsp):    
#     root.rowconfigure(row, weight=1)
            
# app = GPRPyApp(root)

# root.mainloop()




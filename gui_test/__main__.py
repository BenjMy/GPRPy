import sys
import tkinter as tk

#from gprpy.gprpyGUI import GPRPyApp
#from gprpy.gprpyCWGUI import GPRPyCWApp

from gui_test.gui import MainApplication

def main(args=None):
    window = tk.Tk()
    window.title("Example for Tkinter")
    c = MainApplication(window)
    window.mainloop()  # keeps the application open 

if __name__ == "__main__":
	main()
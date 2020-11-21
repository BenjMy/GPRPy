import sys
import tkinter as tk

#from gui_test.gui import MainApplication
#from gprpy.gprpyGUI import GPRPyApp
from gprpy.gprpyGUI_simple import GPRPyApp as GPRPyApp_simple
#from gprpy.gprpyCWGUI import GPRPyCWApp

def main(args=None):

	# if len(sys.argv) < 2:
	# 	mode = input("Profile [p] or Common Midpoint / WARR [c]?  ")
	# else:
	# 	mode = sys.argv[1][0]

	mode='p_simple'

	if mode == 'test':	
		root = tk.Tk()
		app = MainApplication(root)
		root.mainloop()

	elif mode == 'p_simple':
		rightcol=9
		figrowsp=19+1
    
		root = tk.Tk()
    
		for col in range(rightcol):
			root.columnconfigure(col, weight=1)
		for row in range(figrowsp):    
			root.rowconfigure(row, weight=1)
            
		app = GPRPyApp_simple(root)

		root.mainloop()


	elif mode == 'p':
		rightcol=9
		figrowsp=19+1
    
		root = tk.Tk()
    
		for col in range(rightcol):
			root.columnconfigure(col, weight=1)
		for row in range(figrowsp):    
			root.rowconfigure(row, weight=1)
            
		app = GPRPyApp(root)

		root.mainloop()

	elif mode == 'c' or mode == 'w':
		rightcol=10
		figrowsp=15+1
    
		root = tk.Tk()

		for col in range(rightcol):
			root.columnconfigure(col, weight=1)
		for row in range(figrowsp):    
			root.rowconfigure(row, weight=1)

		app = GPRPyCWApp(root)

		root.mainloop()

	else:
		print("You need to chose either profile [p] or CMP/WARR [c] mode.")
    
    

if __name__ == "__main__":
	main()
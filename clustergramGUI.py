from tkinter import *
from tkinter import ttk
from GUIUtils import GUIUtils as GU

def clustergramGUI():
	root = Tk()
	root.title("Clustergram Options")

	#Create the frame that will contain the parameters to create a clutergram
	mainframe = ttk.Frame(root, padding="15 15 15 15")
	mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

	#Create resizing parameters for each clustergram dataset.
	root.columnconfigure(0, weight = 1)
	root.rowconfigure(0, weight = 1)
	mainframe.columnconfigure(1, weight=2)
	mainframe.columnconfigure(2, weight =2)
	mainframe.rowconfigure(1, weight = 2)
	mainframe.rowconfigure(2, weight = 2)
	mainframe.rowconfigure(3, weight = 2)
	mainframe.rowconfigure(4, weight= 2)

	output = StringVar()
	#Create a radiobuttons to allow for the selection of a linkage function
	linkageSingle =   ttk.Radiobutton(mainframe,text='Single',variable=output,value='single').grid(column=2,row=2,sticky=(N,S,E,W))
	linkageComplete = ttk.Radiobutton(mainframe,text='Complete',variable=output,value='complete').grid(column=2,row=3,sticky=(N,S,E,W))
	linkageWard =     ttk.Radiobutton(mainframe,text='Ward',variable=output,value='ward').grid(column=2,row=1,sticky=(N,S,E,W))
	linkageAverage =  ttk.Radiobutton(mainframe,text='Average',variable=output,value='average').grid(column=2,row=4,sticky=(N,S,E,W))

	#Create a button in the column that doesnt contain any radiobuttons that allow for the user to properly go to the create clustergram function
	clustergramBtn = ttk.Button(mainframe,text="Create Clustergram",command=GU.createClustergram).grid(column=1,row=1,sticky=(N,S,E,W))

	root.mainloop()
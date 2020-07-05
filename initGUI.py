from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import btn_functions as bf 

root = Tk()
root.title("Clustering GUI")
#Create frame that goes on the inside of the window created by the root object
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#give appropriate weights to the resizing of the elements in each row to allow for appropriate sizing of the buttons upon screen resizing.
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight=2)
mainframe.columnconfigure(2, weight =2)
mainframe.rowconfigure(1, weight = 2)
mainframe.rowconfigure(2, weight = 2)
mainframe.rowconfigure(3, weight = 2)
mainframe.rowconfigure(4, weight= 2)

#Create label that tells the user the interface that they are currently witin.
juneLab = ttk.Label(mainframe, text="Welcome to the June Lab Clustering GUI",font="TkHeadingFont").grid(column=1,row=1,columnspan=3)

#Create a button to allow the user to create a new clustergram
clust = ttk.Button(mainframe, text="Create Clustergram", command=bf.cluster).grid(column=1, row=2, sticky =(N,S,E,W))

#Create a button to allow the user to create a medians file for better clustering results. 
med = ttk.Button(mainframe, text="Group Medians", command=bf.Medians).grid(column=2, row=2, sticky =(N,S,E,W))

#Create a button to allow the user to compare the four most common linkage functions.
link = ttk.Button(mainframe, text="Compare Linkage functions", command=bf.Linkages).grid(column=1, row=3,sticky =(N,S,E,W))

#Create a button to allow the user to validate the appropriate number of clusters needed for a given set of metabolites.
val = ttk.Button(mainframe, text="Validity index", command=bf.Valid).grid(column=1, row=4, sticky =(N,S,E,W))

#Create a button to allow the user to create the peaks to pathways files needed to analyze the peaks to pathways in Mummichog
peak = ttk.Button(mainframe, text="Peaks to Pathways", command=bf.P2P).grid(column=2, row=3, sticky =(N,S,E,W))

#Create a button to allow the user to check the integrity of the data downloaded from Metaboanalysts Volcano plot results. 
integrity = ttk.Button(mainframe, text="Data Integrity", command=bf.integrity).grid(column=2, row=4, sticky =(N,S,E,W))


# pad each widget with 5 pixels on each side to ensure that the buttons do not stay together. 
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#Create a Messagebox that recommends that the user looks at the readme file before beginning to use the interface
messagebox.showinfo(message="Please make sure to read the README file, before using this GUI, additionally if you get stuck at any point please make sure to cover the examples provided.")

#start the application
root.mainloop()

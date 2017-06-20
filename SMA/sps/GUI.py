'''
Created on Jun 3, 2017

@author: Survya Pratap Singh
'''
from tkinter import *
from _ctypes import alignment
from sps.constant import *
from tkinter import font
from sps.CustomNotebook import *
import ttk
import numbers



global app
global logo
global appNotebook


class createAppGui:
    
    #Constructor for initalizing GUI
    def __init__(self):
        icon = PhotoImage(file=appLogo)
        app.tk.call('wm', 'iconphoto', app._w, icon)
        app.wm_title(appTitle)
        app.geometry('500x500')
        
        rows=0
        while rows<50:
            app.rowconfigure(rows, weight=1)
            app.columnconfigure(rows, weight=1)
            rows+=1
            
        app.configure(background='white')
     
     #Method for creating menubar   
    def createMenuBar(self):
        menubar = Menu(app)
        filemenu =Menu(menubar)
        filemenu.add_command(label="New",command=self.createNewTab)
        filemenu.add_command(label="Open", command='')
        filemenu.add_command(label="Save", command='')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        app.config(menu=menubar)
    
    

    def createHomeTab(self):
        homeframe = Frame(appNotebook,background='white')   # first page, which would get widgets gridded into it
        appNotebook.add(homeframe, text='Home')
        w = Label(homeframe, image=logo, bg="white", fg="white")
        w.place(x = 200, y = 100)
        w1 = Label(homeframe, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
        w1.place(x = 400, y = 90)
        
        
        
    def createNewTab(self):
        workframe=Frame(appNotebook,background='white')   # first page, which would get widgets gridded into it
        appNotebook.add(workframe, text='work')


           
        
 
        
        
        
        
        

    

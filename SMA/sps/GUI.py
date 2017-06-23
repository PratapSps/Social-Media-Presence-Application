'''
Created on Jun 3, 2017

@author: Survya Pratap Singh
'''
from tkinter import *
from _ctypes import alignment
from sps.AppVariables import *
from tkinter import font
from sps.CustomNotebook import *
from tkinter import ttk
import numbers
from sps import AppVariables



class createAppGui:
    name=""
    #Constructor for initalizing GUI
    def __init__(self):
        icon = PhotoImage(file=appLogo)
        app.tk.call('wm', 'iconphoto', app._w, icon)
        app.wm_title(appTitle)
        app.geometry('500x500')
        app.maxsize(width=1300, height=700)
        app.wm_state('zoomed')
        rows=0
        while rows<50:
            app.rowconfigure(rows, weight=1)
            app.columnconfigure(rows, weight=1)
            rows+=1
            
        app.configure(background='white')
     
     #Method for creating menubar   
    def createMenuBar(self):
        filemenu.add_command(label="New",command=self.createNewTab)
        filemenu.add_command(label="Open", command='')
        filemenu.add_command(label="Save", command='')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app.quit)
        #filemenu.entryconfig(1, state=DISABLED)
        menubar.add_cascade(label="File", menu=filemenu)
        app.config(menu=menubar)
    
#create home tab frame        
    def createHomeTab(self,name):
        Home_frame = Frame(notebook,background='white')
        Home_frame.pack(fill=BOTH, expand=True)
        notebook.add(Home_frame, text=name,image='/images/applogo.png')
        frame=self.createFramedScrollBar(Home_frame)
        frame.config(background='white')
        w = Label(frame, image=logo, bg="white", fg="white")
        w.place(x = 400, y = 200)
        w1 = Label(frame, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
        w1.place(x = 600, y = 170)
        
        
#create new tab frame with user input.
  
    def createNewTab(self):
        AppVariables.checktab=AppVariables.checktab+1
        filemenu.entryconfig(1, state=DISABLED)
        self.getTabName(app)
        new_frame=Frame(notebook,background='gray')
        new_frame.pack(fill=BOTH, expand=True)
        notebook.add(new_frame,text=AppVariables.username)
        frame=self.createFramedScrollBar(new_frame)
        frame.config(background='ivory2')
        self.addElementToFrame(frame)
        
        
        
    def getTabName(self,parent):
        top = self.top = Toplevel(parent)
        icon = PhotoImage(file=appLogo)
        top.tk.call('wm', 'iconphoto', top._w, icon)
        top.wm_title("Give Search Name")
        top.geometry('300x100')
        self.myLabel = Label(top, text='Enter name for your Search: ')
        self.myLabel.pack()
        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
        app.wait_window(top)
        
    def send(self):
        AppVariables.username=self.myEntryBox.get()
        self.top.destroy()
     
     
     #create scrollbar contained frame   
    def createFramedScrollBar(self,container):
        canvas = Canvas(container,bg='white')
        xscroll = Scrollbar(container, command=canvas.xview,orient = HORIZONTAL)
        yscroll = Scrollbar(container, command=canvas.yview,orient = VERTICAL)
        canvas.config(xscrollcommand=xscroll.set)
        canvas.config(yscrollcommand=yscroll.set,)
        canvas.configure(scrollregion=(0,0,1200,600))
        xscroll.pack(side=BOTTOM, fill=X,expand = FALSE)
        yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        frame = Frame(canvas)
        canvas.create_window(0,0, anchor =NW, window = frame, width = 1300, height = 700)
        return frame
    
    
    #create method for adding widget to new frame
    
    def addElementToFrame(self,frame):
        innerFrame = Frame(frame,height=500, width=1000,bd=1,background= 'gray99',relief=GROOVE)
        innerFrame.place(x = 140, y = 70)
        FirstName=Label(innerFrame,text='First Name*',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        FirstName.place(x=100,y=40)
        MiddleName=Label(innerFrame,text='Middle Name',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        MiddleName.place(x=400,y=40)
        LastName=Label(innerFrame,text='Last Name*',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        LastName.place(x=750,y=40)
        Country=Label(innerFrame)
        City=Label(innerFrame)
        State=Label(innerFrame)
        Email=Label(innerFrame)
        Phone=Label(innerFrame)
        School_Name=Label(innerFrame)
        
        
        
        
                


        
    
    

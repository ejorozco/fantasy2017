'''
Created on May 4, 2017

@author: wookiee
'''
from Tkinter import *
from PIL import Image, ImageTk
#from mainMenu import getTeamPic

def research():
    global researchEL
    global rootR
 
    rootR = Toplevel() # This now makes a new window.
    rootR.geometry('350x350') # Makes the window a certain size
    rootR.title('\t\tResearch Main Menu\t\t') # This makes the window title
    
    image = Image.open("./pics/magglass.jpeg") #adding the image to window
    image = image.resize((150,150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Label(rootR, image = img)
    panel.image = img
    intruction = Label(rootR, text='Please Enter a Player\'s first or last name\n') # More labels to tell us what they do
    searchB = Button(rootR, text='Search', command=search) # This makes the login button, which will go to the CheckLogin def.
    researchEL = Entry(rootR) # The entry input

    panel.grid(row=0,column=0,sticky=E)
    intruction.grid(row=1,sticky='WE')
    researchEL.grid(padx=5, pady=5, ipadx=5, ipady=5,row=2, sticky='WE')
    searchB.grid(columnspan=1, sticky='WE')
 


def search():
    '''
    print 'search'
    global searchEL
    global rootS
 
    rootS = Toplevel() # This now makes a new window.
    rootS.geometry('350x350') # Makes the window a certain size
    rootS.title('\tAarron Rodgers') # This makes the window title
    
    image = Image.open(getTeamPic('Green Bay Packers')) #adding the image to window
    image = image.resize((150,150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Label(rootS, image = img)
    panel.image = img
    

    
    label1 = Label(rootS, text='') # More labels to tell us what they do
    searchB = Button(rootS, text='EXIT', command=search) # This makes the login button, which will go to the CheckLogin def.
    searchEL = Entry(rootS) # The entry input
    
    
    panel.grid(row=0,column=0,sticky=E)
    '''

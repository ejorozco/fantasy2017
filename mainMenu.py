'''
Created on May 1, 2017

@author: wookiee
'''
from Tkinter import *

def menu(User):
    global r
    r = Tk() # Opens new window
    string = "Welcome " + User.username
    r.title(string)
    r.geometry('500x500') # Makes the window a certain size
    fmL = Label(r, text='Fantasy Football Manager 2017') # "logged in" label
    mainL = Label(r, text='MAIN MENU') # "logged in" label
    
    fmL.grid(sticky=W)
    mainL.grid(sticky=W)
    
    simulateB = Button(r, text='Simulate Game', command=simulate)
    simulateB.grid(columnspan=10, sticky=N)
    
    viewTeamB = Button(r, text='View Team', command=viewTeam)
    viewTeamB.grid(columnspan=10, sticky=N)

    researchB = Button(r, text='Research', command=reseach)
    researchB.grid(columnspan=10, sticky=N)
    
    logoutB = Button(r, text='Log Out', command=logOut)
    logoutB.grid(columnspan=10, sticky=N)
    
    r.mainloop()
    
def simulate():
    print 'simulate'  
     
def viewTeam():
    print 'viewing team'

def viewSchedules():
    print 'view schedules'
     
def reseach():
    print 'research'
    
def profileOptions():
    print 'options'
    
def logOut():
    r.destroy()
    
    
    
    

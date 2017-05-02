'''
Created on May 1, 2017

@author: wookiee
'''
from Tkinter import *
import login

def mainMenu(name):
    global r
    r = Tk() # Opens new window
    string = "Welcome " + name
    r.title(string)
    r.geometry('500x500') # Makes the window a certain size
    fmL = Label(r, text='Fantasy Football Manager 2017') # "logged in" label
    mainL = Label(r, text='MAIN MENU') # "logged in" label
    
    fmL.grid(row=0, column=5, sticky=W)
    mainL.grid(row=1, column=9, sticky=W)
    
    simulateB = Button(r, text='Simulate', command=simulate)
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
    login.Login()
    

    
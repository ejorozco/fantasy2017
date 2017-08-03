'''
Created on May 1, 2017

@author: wookiee
'''
from Tkinter import *
from PIL import Image, ImageTk
from research import research

def menu(User):
    global r
    r = Tk() # Opens new window
    string = "Fantasy Football Manger 2017"
    r.title(string)
    r.geometry('450x450') # Makes the window a certain size
    getPic = getTeamPic(User.favoriteTeam)
    
    image = Image.open(getPic) #adding the image to window
    image = image.resize((230,230), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Label(r, image = img)
    #panel.grid(sticky=W)
    
    panel.place(x=200,y=0)
    
    #fmL = Label(r, text='Fantasy Football Manager 2017') # "logged in" label
    fmL = Label(r, text="\nWelcome "+ User.username) # "logged in" label
    mainL = Label(r, text='\nMAIN MENU\n') # "logged in" label
    fmL.grid(row=1, column=2,sticky=W)
    mainL.grid(row=2,column=2,sticky=W)
    
    simulateB = Button(r, text='Simulate Game', command=simulate)
    #simulateB.grid(columnspan=10, sticky=N)
    simulateB.grid(row=3,column=2,sticky=W)
    
    viewTeamB = Button(r, text='  View Team  ', command=viewTeam)
    #viewTeamB.grid(columnspan=10, sticky=N)
    viewTeamB.grid(row=4,column=2,sticky=W)

    researchB = Button(r, text='  Research   ', command=reseach)
    #researchB.grid(columnspan=10, sticky=N)
    researchB.grid(row=5,column=2,sticky=W)
    
    logoutB = Button(r, text='   Log Out     ', command=logOut)
    #logoutB.grid(columnspan=10, sticky=N)
    logoutB.grid(row=6,column=2,sticky=W)
    
    r.mainloop()
def getTeamPic(myTeam):
    teams = {"Arizona Cardinals":"./teamLogo/cardinals.jpeg",
             "Atlanta Falcons":"./teamLogo/falcons.jpeg",
             "Baltimore Ravens":"./teamLogo/ravens.jpeg",
             "Buffalo Bills":"./teamLogo/bills.jpeg",
             "Carolina Panthers":"./teamLogo/panthers.jpeg",
             "Chicago Bears":"./teamLogo/bears.jpeg",
             "Cincinnati Bengals":"./teamLogo/bengals.jpeg",
             "Cleveland Browns":"./teamLogo/browns.jpeg",
             "Dallas Cowboys":"./teamLogo/cowboys.jpeg",
             "Denver Broncos":"./teamLogo/broncos.jpeg",
             "Detroit Lions":"./teamLogo/lions.jpeg",
             "Green Bay Packers":"./teamLogo/packers.jpeg",
             "Houston Texans":"./teamLogo/texans.jpeg",
             "Indianapolis Colts":"./teamLogo/colts.jpeg",
             "Jacksonville Jaguars":"./teamLogo/jaguars.jpeg",
             "Kansas City Chiefs":"./teamLogo/chiefs.jpeg",
             "Miami Dolphins":"./teamLogo/dolphins.jpeg",
             "Minnesota Vikings":"./teamLogo/vikings.jpeg",
             "New England Patriots":"./teamLogo/patriots.jpeg",
             "New Orleans Saints":"./teamLogo/saints.jpeg",
             "Los Angeles Chargers":"./teamLogo/chargers.jpeg",
             "Los Angeles Rams":"./teamLogo/rams.jpeg",
             "New York Giants":"./teamLogo/giants.jpeg",
             "New York Jets":"./teamLogo/jets.jpeg",
             "Oakland Raiders":"./teamLogo/raiders.jpeg",
             "Philadelphia Eagles":"./teamLogo/eagles.jpeg",
             "Pittsburgh Steelers":"./teamLogo/steelers.jpeg",
             "San Francisco 49ers":"./teamLogo/49ers.jpeg",
             "Seattle Seahawks":"./teamLogo/seahawks.jpeg",
             "Tampa Bay Buccaneers":"./teamLogo/buccaneers.jpeg",
             "Tennessee Titans":"./teamLogo/titans.jpeg",
             "Washington Redskins":"./teamLogo/redskins.jpeg"}
    
    return teams[myTeam]
        
def simulate():
    print 'simulate'
     
def viewTeam():
    print 'viewing team'

def viewSchedules():
    print 'view schedules'
     
def reseach():
    print 'research'
    research()
    
def profileOptions():
    print 'options'
    
def logOut():
    r.destroy()
    
    
    
    

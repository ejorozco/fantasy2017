from Tkinter import *
from PIL import Image, ImageTk
from User import User
from mainMenu import menu
import os

userList = []
creds = 'login.txt' # This just sets the variable creds for txt file

def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.geometry('450x500') # Makes the window a certain size
    rootA.title('\t\tWelcome to Fantasy Football Manager 2017\t\t') # This makes the window title 'login'
    
    image = Image.open("logo.jpg") #adding the image to window
    img = ImageTk.PhotoImage(image)
    panel = Label(rootA, image = img)
    panel.grid(sticky=W)
    
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(row=1,sticky=S)
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=2, sticky=W)
    pwordL.grid(row=3, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=2, column=0)
    pwordEL.grid(row=3, column=0)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=N)

    nmuser = Button(rootA, text='New User', command=Signup) # This makes the deluser button. blah go to the deluser def.
    nmuser.grid(columnspan=2, sticky=N)
    
    closer = Button(rootA, text='Quit', command=Quit) # This closes the program
    closer.grid(columnspan=2, sticky=N)
    
    rootA.mainloop()

def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
    
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    
    roots.mainloop() # This just makes the window keep open, we will destroy it soon

def CheckLogin():
    flag = 0
    print userList
    for user in userList:
        print user.username
        print user.password
        if nameEL.get() == user.username and pwordEL.get() == user.password: # Checks to see if you entered the correct data.
            rootA.destroy()
            menu(user)
            flag = 1
            Login() # Return to login menu after user logs out
            
    if flag == 0:
        r = Tk()
        r.title('Please Try Again')
        r.geometry('250x100')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()    
def FSSignup():
    with open(creds, 'a') as f: # Creates a document using the variable we made at the top. 'a' is for append
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.write('\n')
        f.close() # Closes the file
    
    createUsers()
    roots.destroy() # This will destroy the signup window. :)

def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
    
def Quit():
    rootA.destroy()

def createUsers():
    del userList[:]
    with open(creds) as f:
        try:
            while 1:
                uname = f.next().rstrip()
                pword = f.next().rstrip()
                user = User(uname,pword)
                userList.append(user)
                
        except: StopIteration

                
#Begin Fantasy manager login
createUsers()
if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
    
    
    

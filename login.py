from Tkinter import *
import mainMenu
#from PIL import Image, ImageTk
import os
 
creds = 'login.txt' # This just sets the variable creds to 'tempfile.temp'

def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.geometry('500x300') # Makes the window a certain size
    rootA.title('\t\tWelcome to Fantasy Football Manager 2017\t\t') # This makes the window title 'login'
    
    """
    #adding image
    img = PhotoImage(Image.open("/Users/wookiee/Desktop/Eclipse/Fantasy2017/FantasyFootball/fantasy-logo.png"))
    panel = Label(rootA, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    """

    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E)
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=N)

    nmuser = Button(rootA, text='New User', command=Signup) # This makes the deluser button. blah go to the deluser def.
    nmuser.grid(columnspan=2, sticky=N)
    
    closer = Button(rootA, text='Quit', command=Quit) # This makes the deluser button. blah go to the deluser def.
    closer.grid(columnspan=2, sticky=N)

 
    #rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    #rmuser.grid(columnspan=2, sticky=W)
    #rmuser.pack()
    
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
 
def FSSignup():
    with open(creds, 'a') as f: # Creates a document using the variable we made at the top. 'a' is for append
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.write('\n')
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    #Login() # This will move us onto the login definition :D

def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        """
        r = Tk() # Opens new window
        r.title(':D')
        r.geometry('200x200') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        r.mainloop()
        """
        rootA.destroy()
        mainMenu.mainMenu(uname)
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
    
def Quit():
    rootA.destroy()

#Begin Fantasy manager login
if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    #Signup()
    Login()
    
    
    
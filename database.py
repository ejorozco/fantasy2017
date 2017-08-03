'''
Created on May 1, 2017

@author: wookiee

Fro preperation to connect to server you must:
    - pip install psycopg2
    - pip install pygresql

This file will connect to Postgres SQL server
to hold and ontain data

SQl will hold;
user table
    - username
    - password
    - favorite team
    - team position players
    

Player table
    - 

'''

# Import package to connect to PostgreSQL database
import psycopg2
from User import User
from Player import Player
from Tkinter import *
from PIL import Image, ImageTk
import xlrd
from datetime import timedelta, datetime

# SQL Database credientals
hostname = 'localhost'
user = 'postgres'
password = '3235'
database = 'fantasy2017'

class PlayerDatabase(object):
    
    statistics = {}
    
    def obtainPlayerLibrary(self):
        # TIME TO PULL THE DATA
        path = './Stats/Stats2017.xlsx'
        workbook = xlrd.open_workbook(path)
        player = Player()
        
        #Obtaining data from the excel file
        #Saving all data into Player objects
        for sheet in xrange(0,5):
            worksheet = workbook.sheet_by_index(sheet)
            numberOFRows = worksheet.nrows
            numberOFColumns = worksheet.ncols 
            for rowCounter in xrange(3,numberOFRows):
                row = worksheet.row_values(rowCounter)
                if row[0] != "":
                    player = Player()   #create a new object variable
                    
                    names = row[0].split(" ")
                    
                    player.fullName = row[0]
                    player.first_name = names[0]
                    player.last_name = names[1]
                    player.team = row[1]
                    
                    if sheet == 0:
                        player.position = "QB"
                    elif sheet == 1:
                        player.position = "RB"
                    elif sheet == 2:
                        player.position = "WR"
                    elif sheet == 3:
                        player.position = "TE"
                    elif sheet == 4:
                        player.position = "K"
                    elif sheet == 5:
                        player.position = "DEF"
                        
                    player.draft = row[2]
                    player.college = row[3]
                    player.height = row[4]
                    player.weight = row[5]
                    
                    d = timedelta(days=row[6])
                    st = datetime(1899,12,31)
                    date = st + d
                    player.dob = str(date).replace('00:00:00', ' ')
                    
                    player.age = row[7]
                    player.week = [row[8]]
                    player.opponent = [row[9]]
                    player.Results = [row[10]]
                else:
                    if sheet == 0:      #Sheet1: QB
                        player
                        player.Cmp.append(row[11])
                        player.Att.append(row[12])
                        player.CmpPercent.append(row[13])
                        player.Yard.append(row[14]) 
                        player.TD.append(row[15])
                        player.INT.append(row[16])
                        player.Att.append(row[17])
                        player.Yard.append(row[18])
                        player.Avg.append(row[19])
                        player.passTD.append(row[20])
                        player.fpts.append(row[21])
                    elif sheet == 1:    #Sheet1: RB
                        player.targets.append(row[11])
                        player.receptions.append(row[12])
                        player.receivingYds.append(row[13])
                        player.receivingAvg.append(row[14])  
                        player.receivingTD.append(row[15])
                        player.rushingAtt.append(row[16])     
                        player.rushingYds.append(row[17])  
                        player.rushingAvg.append(row[18])  
                        player.rushingTD.append(row[19])
                        player.fpts.append(row[20])
                    elif sheet == 2:    #Sheet1: WR
                        player.targets.append(row[11])
                        player.receptions.append(row[12])
                        player.receivingYds.append(row[13])
                        player.receivingAvg.append(row[14])  
                        player.receivingTD.append(row[15])
                        player.rushingAtt.append(row[16])     
                        player.rushingYds.append(row[17])  
                        player.rushingAvg.append(row[18])  
                        player.rushingTD.append(row[19])
                        player.fpts.append(row[20])
                    elif sheet == 3:    #Sheet1: TE
                        player.targets.append(row[11])
                        player.receptions.append(row[12])
                        player.receivingYds.append(row[13])
                        player.receivingAvg.append(row[14])  
                        player.receivingTD.append(row[15])
                        player.rushingAtt.append(row[16])     
                        player.rushingYds.append(row[17])  
                        player.rushingAvg.append(row[18])  
                        player.rushingTD.append(row[19])
                        player.fpts.append(row[20])
                    elif sheet == 4:    #Sheet1: K
                        player.FGM.append(row[11])
                        player.FGA.append(row[12])
                        player.FGpercent.append(row[13])
                        player.EPM.append(row[14])
                        player.EPA.append(row[15])
                        player.fpts.append(row[16])
                    elif sheet == 5:    #Sheet1: DEF
                        player.takles_sacks.append(row[11]) 
                        player.int.append(row[12]) 
                        player.fum_Rec.append(row[13])   
                        player.safety.append(row[14])   
                        player.defTD.append(row[15])   
                        player.pts_allowed.append(row[16])
                        player.fpts.append(row[17])
                        
                self.statistics[player.last_name] = player
        return self.statistics
            
# SQL function call SQL INSERT query to database
def insertUser(name, passw, favTeam):
    myConnection = psycopg2.connect( host=hostname, user=user, password=password, dbname=database )
    cur = myConnection.cursor()
    cur.execute('INSERT INTO fantasyuser (username, user_password, favorite_team) VALUES(%s, %s, %s)', (name,passw,favTeam,))
    myConnection.commit()
    cur.close()
    myConnection.close()
    
# Routine to run a query to find user:
def findUser(name, passw):
    foundUser = None
    myConnection = psycopg2.connect( host=hostname, user=user, password=password, dbname=database )
    cur = myConnection.cursor()
    cur.execute("SELECT username,user_password,favorite_team FROM fantasyuser")

    for username, user_password, favorite_team in cur.fetchall() :
        print username.strip(),'\n',user_password.strip(),'\n',favorite_team.strip()
        if username.strip() == name and user_password.strip():
            foundUser = User(username.strip(), user_password.strip(), favorite_team.strip())
            return foundUser      
    return foundUser
    
    def findPlayer():
        print "find player"
    
data = PlayerDatabase()
data.obtainPlayerLibrary()
#print data.statistics

for key, value in data.statistics.iteritems():
    print "%s.....%s.....week TD 6: %s  ..... week TD 8:%s" % (key, value.team,value.weekTD(6),value.weekTD(8))
    
    
    
    

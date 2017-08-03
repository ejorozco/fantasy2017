'''
Created on May 1, 2017

@author: wookiee
'''

POINTS_PER_PASSING_YARD = 0.04
POINTS_PER_PASSING_TOUCHDOWN = 4
POINTS_PER_INTERCEPTION = -1 
POINTS_PER_RUSHING_YARD = 0.1
POINTS_PER_RUSHING_TOUCHDOWN = 6
POINTS_PER_RUSHING_FUMBLE = -2
POINTS_PER_RECEPTION_YARD = 0.1
POINTS_PER_RECEPTION_TOUCHDOWN = 6


class Player(object):
    '''
    This is the Player Stats container object
    '''
    # Personal Information of player
    fullName = ""
    first_name = ""
    last_name = ""
    team = ""
    position = ""
    draft = ""
    college = ""
    height = ""
    weight = ""
    dob = ""
    age = ""
    
    # Weekly game summaries
    week = []
    opponent = []
    Results = []
    
    # Quarterback stats only
    Cmp = [] 
    Att = []  
    CmpPercent = []   
    Yard = []    
    TD = [] 
    INT = []
    Att = []
    Yard = []
    Avg = []
    passTD = []
    
    # Receiving Stats
    targets = []
    receptions = []
    receivingYds = []
    receivingAvg = []   
    receivingTD = []  

    # Rushing stats
    rushingAtt = []      
    rushingYds = []  
    rushingAvg = []   
    rushingTD = []
    
    # Kicker Stats
    FGM = []
    FGA = []
    FGpercent = []
    EPM = []
    EPA = []
    
    # DEF Stats
    takles_sacks = []  
    int = [] 
    fum_Rec = []    
    safety = []    
    defTD = []    
    pts_allowed = []
    
    # Total fantasy points, of that week 
    fpts = []
    
    # Constructor
    #def __init__(self, params):
    
    def weekTD(self, week):
        if self.position == "QB":
            return self.passTD[week]
        elif self.position == "RB":
            return self.receivingTD[week] + self.rushingTD[week]
        elif self.position == "WR":
            return self.receivingTD[week] + self.rushingTD[week]
        elif self.position == "TE":
            return self.receivingTD[week] + self.rushingTD[week]
        elif self.position == "DEF":
            return self.defTD[week]
        elif self.position == "K":
            return 0
        
     
        

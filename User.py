'''
Created on May 1, 2017

@author: wookiee
'''

class User:
    """
    This is the user object which holds personal login
    information including an ID for their perspective
    custom team they created
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.favoriteTeam = favoriteTeam
        #self.customID = customID

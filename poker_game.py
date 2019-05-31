#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:57:47 2019

@author: brandon
"""
#%%

"""
Write a Poker game

For this assignment we are going to (also) create a poker game. The game needs to do the following:

- Needs to be written on a file named poker_game.py



- The game can be played by running python poker_game.py NUMBER_OF_PLAYERS
- The script accepts an argument number_of_players which is a number indicating the number of players.
- For each player the script will ask the name (using input() function).
- The script will deal 5 cards to each player (you can use random.choice to select at random from a list). The different cards, sorted from lowest to highest are 2,3,4,5,6,7,8,9,10,J,Q,K,A. There are four suits, clubs, spades, hearts, diamonds.
- The script will print out each one of the players' hand, find out which one of the players have a winning hand and will print out the name of the winner
- For the winning rules, there are two possible implementations:
Easy version, where we just compare the hands and the hand with the highest cards wins. For example, if Player 1 has the hand 2,3,K,Q,7 and Player 2 has the hand 8,10, ACE,J,2 Player 2 would win because 1 ACE beats a K. If Player 1 has the hand 2,3,K,Q,7, and Player 2 has the hand J,J,K,7,3 then Player 1 would win (since K,Q beats K,J).
Hard version, where we implement the different poker hands taking the suits into account (flush, poker, straight, etc).
hint: You can use the __gt__ , __lt__ or __eq__ methods on a class to implement comparisons (greater than, less than).

Finally, we will create a repository on github called poker_game, upload the poker_game.py file and a README.md file explaining what the game does. Then we will link the repository on the blog post.
"""
#%%



import random

class game:
    #where 11: J, 12: Q, 13: K, 14: A
   
    
    
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        
        
    def name(self):
#        name = ''
        self.players = []
        
        for each in range(self.number_of_players):
            player_name = input()
            self.players.append(player_name)
        
        print(self.players)
    
    
    def player_hands(self):
       self.hands = []
       for each in range(self.number_of_players):
            hand = random.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4, 5)
            self.hands.append(hand)
            
       dict_players = { i : self.hands[i] for i in range(0, len(self.hands) ) }
       print(dict_players)
       
        
    
        
    def winner(self):
        
        x = self.hands
        max_list=[]
        print(x)
        #Converting the symbols into integers to count points
        for lists in x:
            for card in lists:
                if card == 'J':
                    lists[lists.index(card)]=11
                elif card == 'Q':
                    lists[lists.index(card)]=12
                elif card == 'K':
                    lists[lists.index(card)]=13
                elif card == 'A':
                    lists[lists.index(card)]=14
                else: pass
            
        print(x)
        #Maximum of each player    
        for i in range(len(x)):
            max_list.append(max(x[i]))
    
        #Highest max:
        m=max(max_list)
        
        #Winner:
        #This game assumes that the player with the highest card wins.
        winners = []
            
        for i in range(len(max_list)):
            if max_list[i] == m:
                ind_max = i
                winners.append(ind_max)
        print(winners) 
        
        #Winners' names:\
        for winner in winners:
            print("Congratulations to {}!".format(self.players[winner]))
    
    """         
    #Attempt at writing a code to have only one winner in case more than one person has the same max:
        
        while len(winners)>1:
            winners.clear()
            max_list.clear()
            
        print(winners)    
            for each in winners:
               del x[each]
            print(x)
               
            for i in range(len(x)):
                max_list.append(max(x[i]))
            
            for i in range(len(max_list)):
                if max_list[i] == m:
                    ind_max = i
                    winners.append(ind_max)
        print(max_list)
        
       
        print("Congratulations to {}".format(self.players[winners[0]]))
            
       
    
    """  

    
        
       

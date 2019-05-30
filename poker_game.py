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
    #rank = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    
    def __init__(self, number_of_players):
        self.point = points.point  
        
    def __eq__ (self, other):
        return (self.point == other.point)

    def __lt__ (self, other):
        return (self.point < other.point)

    def __gt__ (self, other):
        return (self.point > other.point)
    
    
    def deal(self):
       
        #player1 = random.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 5)
        #give the rest to the other players
        
           for i in range (hands):
               hand = []
           for j in range (cards):
               #hand.append (self.deck.deal())
               #self.hands.append (hand)
    
        
        
    def points(self, hand):
        sortedHand=sorted(hand,reverse=True)
        point = sortedHand[0]
        print(point)
    
    
    def name(self):
        name = ''
        players = []
        input(name)
        
        players.append(name)
        
        return players


    
    def winner(self, points, other):
        winner = ''
        for player in players:
            if player.point > other.point:
                winner = player
        print(winner)
        

#%%
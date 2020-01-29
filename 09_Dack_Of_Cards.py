"""
Created on:1/29/2020
@author:Marvin Senjaliya
"""
"""
problem statement:
Write a Program DeckOfCards.java, to initialize deck of cards having suit ("Clubs", "Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players using 2D Array…
"""

from queue import Queue
class Card:
    def __init__(self,suits=0,rank=0):
        self.suits=suits
        self.rank=rank

class Deck:

    Rank=("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    Suits=("Clubs","Diamonds", "Hearts", "Spades")

    def __init__(self):
        self.cards = []
        for suit in self.Suits:
            for rank in self.Rank:
                self.cards.append((suit,rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def Shuffle(self):
        import random
        num_cards=len(self.cards)
        for i in range(len(num_cards)):
            j=random.randrange(0,num_cards)
            self.card[i] , self.card[j]= self.card[j] , self.card[i]

    def players_cards(self):
        import random
        num_cards=len(self.cards)
        for i in range(1,5):
            print("cards of first player:",i)
            for j in range(1,10):
                players_card=random.randrange(0,num_cards)
                print(self.cards[players_card])

    def Sort_by_rank(self):
        l=len(self.Rank)
        for i in range(0,l):
            for j in range(0,l-i-1):
                if self.Rank[j]>self.Rank[j+1]:
                    self.Rank[j], self.Rank[j+1] = self.Rank[j+1], self.Rank[j]
        print(self.Rank[j])




obj = Deck()
obj.print_deck()
obj.players_cards()
obj.Sort_by_rank()

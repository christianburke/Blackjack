import math
import random


class Card(object):
    """Represents a standard playing card."""
    #Built using info from the book

    def __init__(self, suit=0, rank=0):
        #Defines suit and rank of cards in the deck
        self.suit = suit
        self.rank = rank

    #Gives suits and ranks real values
        self.suit_names =  ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8',
            '9', '10', 'Jack', 'Queen', 'King']
        self.rank_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
            '9':9, '10':10, 'Jack': 10, 'Queen': 10, 'King':10, 'Ace':11}

    def __str__(self):
        #Returns a selected card rank and suit
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        #Modeled from exercise 18.1, returns positive if greater,
        #negative if less than, and 0 if equal.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    """Represents a deck of standard playing cards."""
    #Also built form the book

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
    #Removes first card from deck. Essentially dealing.
        return self.cards.pop(0)

    def add_card(self, card):
    #Add a card to the deck.
        self.cards.append(card)

    def shuffle(self):
    #Randomly shuffles the deck.
        random.shuffle(self.cards)

    def sort(self):
    #Sorts the deck.
        self.cards.sort(cmp=Card.__cmp__)



class Hand(object):
    """Represents the hand dealt to a player or dealer."""

    def __init__(self):
        self.cards = []
        self.type = 'hard'
        self.isBusted = False
        self.isBlackjack = False
        self.isPair = False
        self.isDoubleDown = False
        self.total = 0

    def __str__(self):
        return '%s, %s' % (self.cards[0], self.cards[1])

    def add(self, card):
        print 'drew', card
        self.cards.append(card)
        #self.isPair = (len(self.card) == 2 and\
            #self.cards[0].rank == self.cards[1].rank)

    def draw_hand(self, deck):
        for item in range(2):
            self.cards.append(deck.pop_card())
        return self.cards

    def calc_total(self):
        #soft means that a hand contains an ace as value 11.
        #Hard means that it contains no ace or ace as value 1.
        self.type = 'hard'
        self.total = 0
        for card in self.cards:
            if card.rank == 1:
                self.type = 'soft'
        if self.type == 'soft':
            for card in self.cards:
                if card.rank_values[card.rank_names[card.rank]] > 21:
                    self.type == 'hard'
                    Card.rank_values['Ace'] = 1
                elif card.rank_values[card.rank_names[card.rank]] <=21:
                    for card in self.cards:
                        self.total += card.rank_values[card.rank_names[card.rank]]
                    return self.total
        if self.type == 'hard':
            for card in self.cards:
                self.total += card.rank_values[card.rank_names[card.rank]]
            return self.total

#print hand.draw_hand()
#print hand.calc_total()

class Dealer(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()
        self.isBusted = False
        self.isBlackjack = False
        self.total = self.hand.calc_total()


    def play(self):
        self.total = self.hand.calc_total()
        print self.hand
        print self.total
        if self.total == 21:
            hand.isBlackjack == True
            return 'Dealer has blackjack!'
        if self.total > 21:
            hand.isBusted == True
            print "Dealer busted!"
        while self.total <17 and self.isBusted == False \
        and self.isBlackjack == False:
            if self.total < 17:
                print 'hit'
                self.hand.add(self.deck.pop_card())
                self.total = self.hand.calc_total()
                print self.hand.cards
                print self.total


#deck = Deck()
#hand = Hand()

#dealer = Dealer(deck)
#dealer.hand.draw_hand(deck)
#print dealer.play()


class Player(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()
        self.isBusted = False
        self.isBlackjack = False
        self.total = self.hand.calc_total()

    def play(self):
        self.total = self.hand.calc_total()
        print self.hand
        print self.total
        if self.total == 21:
            hand.isBlackjack == True
            return 'Player has blackjack!'
        hit = raw_input("Would you like to hit? Answer Y for yes, N for no.")
        if self.total < 21:
        if hit == 'Y':
            self.hand.add(self.deck.pop_card())
            self.total = self.hand.calc_total()
            print self.hand.cards
            print self.total
        if hit == 'N':
            self.total = self.hand.calc_total()
            print self.hand.cards
            print self.total
        if self.total > 21:
            hand.isBusted = True
            return "Player busted!"

#Need help with while loop

deck = Deck()
hand = Hand()

player = Player(deck)
player.hand.draw_hand(deck)
print player.play()

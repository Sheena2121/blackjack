import random


class Card:
    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.value == "Ten" or "Jack" or "Queen" or "King":
            self.pointValue = 10
        if self.value == "Ace":
            self.pointValue = 11
        if self.value == "Two":
            self.pointValue = 2
        if self.value == "Three":
            self.pointValue = 3
        if self.value == "Four":
            self.pointValue = 4
        if self.value == "Five":
            self.pointValue = 5
        if self.value == "Six":
            self.pointValue = 6
        if self.value == "Seven":
            self.pointValue = 7
        if self.value == "Eight":
            self.pointValue = 8
        if self.value == "Nine":
            self.pointValue = 9

    # Returns the suit of the card.
    def suit(self):
        return self.suit

    # Returns the value of the card.
    def value(self):
        return self.value


    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self):
        print("{} of {} aka {} points".format(self.value, self.suit, self.pointValue))
        return "{} of {} aka {} points".format(self.value, self.suit, self.pointValue)


class Deck:

    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
        self.deck = []
        self.reset()

    # Returns the number of Cards in the Deck
    def size(self):
        print("size:")
        print(len(self.deck))
        return len(self.deck)

    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self):
        random.shuffle(self.deck)
        print("shuffle:")
        print(self.deck)
        return self.deck

    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self):
        print("peek:")
        print(self.deck[0])
        return self.deck[0]

    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        return self.deck.pop(0)

    # Adds the input card to the deck.
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self):
        if len(self.deck) <= 51:
            deck2 = Deck()
            self.deck.append(deck2.deck.pop(0))
            print("new length of deck")
            print(len(self.deck))

        else:
            print("there are already 52 cards in the deck")

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        for c in self.deck:
            c.__str__()

    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self):
        SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
        VALUES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
                  "Queen", "King"]
        self.deck = [Card(suit, value) for value in VALUES for suit in SUITS]
        self.shuffle()


class Blackjack:  
    # Creates a Blackjack game with a new Deck.
    def __init__(self):
        playerlist = ["Sheena", "Dealer"]
        self.deck = Deck()
        self.players = [Player(name) for name in playerlist]
        self.print_playerlist()
    
    def print_playerlist(self):
        for p in self.players:
            print(p.name)

    def deal(self):
        for p in self.players:
            p.hand.append(self.deck.draw())
            p.hand.append(self.deck.draw())
            print("this is {}'s hand".format(p.name))
            for c in p.hand:
                c.__str__()
                p.handValue += c.pointValue
            print("this is {}'s total".format(p.name))
            print(p.handValue)
    # Deals one more card to the current player.
    # Prints the new score and entire hand.
    # If new score is over 21, then "Bust" is printed instead of a score.
    # The current hand is immediately discarded and can no longer call "hit"
    # "hit" can only be called if there is an active hand that called "deal"

    def hit(self, player):
        player.hand.append(self.deck.draw())
        player.handValue += value of the card that was just added
        --
        if player.handValue == 21:
            print("we have blackjack!")
        elif player.handValue < 21:
            print("your hand is worth")
            print(player.handValue)
        elif player.handValue > 21:
            print("you busted!")

    # Reshuffles all cards back into the Deck.
    def reshuffle(self):
        self.deck.reset()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.handValue = 0


game = Blackjack()

game.deck.size()

game.deal()

game.hit("Sheena")

# Deck of Cards implementation. Contains power to shuffle.

import random


class Deck:

    def __init__(self, amt=1):
        self.size = 0
        self.cards = []
        self.multiple_decks = False
        self.create_deck(amt)

    def look_into(self):
        print([i for i in self.cards])

    def is_empty(self):
        return self.size <= 0

    def empty_deck(self):
        self.size = 0
        self.cards = []
        self.multiple_decks = False

    def create_deck(self, amt=1):
        for count in range(amt):
            card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            card_suits = ['H', 'D', 'C', 'S']
            for suit in card_suits:
                for face in card_faces:
                    self.add_card(Card(face, suit))
            if self.size > 52:
                self.multiple_decks = True

    def add_card(self, card):
        self.cards.append(card)
        self.size += 1

    def draw_card(self):
        if not self.is_empty():
            self.size -= 1
            return self.cards.pop()


    def shuffle(self):
        random.shuffle(self.cards)

    def sort_cards(self):

        # - position (in for loop) : collects item to be sorted in list. Happens to be index next to sorted list
        # - position (in while loop) : Traverses list to find proper index of item

        # - comparisons : How many times objects have been compared

        for position in range(len(self.cards)):
            item = self.cards[position]
            while position > 0:
                position -= 1

                if item > self.cards[position]:
                    break
                else:
                    self.cards[position], self.cards[position + 1] = self.cards[position + 1], self.cards[position]


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        if self.suit == 'C' or self.suit == 'S':
            self.color = 'black'
        else:
            self.color = 'red'

    def __repr__(self):
        return f'({self.face}, {self.suit})'

    def __lt__(self, other):
        card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_suits = ['H', 'D', 'C', 'S']
        if card_suits.index(self.suit) < card_suits.index(other.suit):
            return True
        elif card_suits.index(self.suit) > card_suits.index(other.suit):
            return False
        elif card_faces.index(self.face) < card_faces.index(other.face):
            return True
        else:
            return False

    def get_value(self):
        if self.face == 'A':
            return 1, 11
        elif self.face.isalpha():
            return 10
        else:
            return int(self.face)


if __name__ == '__main__':
    deck = Deck()
    deck.look_into()
    deck.create_deck(3)
    deck.look_into()
    deck.shuffle()
    deck.look_into()
    deck.sort_cards()
    deck.look_into()

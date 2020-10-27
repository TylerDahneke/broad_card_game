import deck_of_cards

class BlackJack:

    def __init__(self):
        self.dealer_cards = []
        self.player_cards = {}
        self.deck = deck_of_cards.Deck(3)

    def __repr__(self):
        return f'dealer_cards:({self.dealer_cards[0]} (_, _)) , {self.player_cards}'

    def add_player(self, player_name):
        if player_name not in self.player_cards:
            self.player_cards[player_name] = []
        else:
            print('player already added')

    def dealer_turn(self):
        total = 0
        for card in self.dealer_cards:
            total += card.get_value()
        while total < 17:
            card = self.deck.draw_card()
            total += card.get_value()
            self.dealer_cards.append(card)

    def give_player_cards(self):
        for player in self.player_cards:
            self.player_cards[player].append(self.deck.draw_card())
            self.player_cards[player].append(self.deck.draw_card())
        self.dealer_cards.append(self.deck.draw_card())
        self.dealer_cards.append(self.deck.draw_card())


    def take_cards_back(self, deck):
        for player in self.player_cards:
            while len(self.player_cards[player]):
                deck.add_card(self.player_cards[player].pop())
        while len(self.dealer_cards):
            deck.add_card(self.dealer_cards.pop())


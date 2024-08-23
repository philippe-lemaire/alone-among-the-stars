from dataclasses import dataclass
import random


@dataclass
class Card:
    suit: str
    rank: str

    def __str__(self):
        return f"{self.rank} of {self.suit}."


class Deck:
    ranks = [str(k) for k in range(2, 11)] + "J Q K A".split()
    suits = "Spades Hearts Diamonds Clubs".split()

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def __getitem__(self, i):
        return self.cards[i]

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def draw(self, n):
        cards = self[:n]
        self.cards = self[n:]
        return cards

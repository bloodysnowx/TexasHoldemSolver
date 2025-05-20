from dataclasses import dataclass
from typing import List
import random


SUITS = ['H', 'D', 'C', 'S']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def card_to_str(card: int) -> str:
    suit = SUITS[card // 13]
    rank = RANKS[card % 13]
    return rank + suit


@dataclass
class Deck:
    cards: List[int]

    def __init__(self):
        self.cards = list(range(52))
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[int]:
        """Deal n cards from the deck."""
        dealt, self.cards = self.cards[:n], self.cards[n:]
        return dealt

from texas_holdem_solver.utils import Deck


def test_deck_deal():
    deck = Deck()
    cards = deck.deal(5)
    assert len(cards) == 5
    assert len(deck.cards) == 52 - 5

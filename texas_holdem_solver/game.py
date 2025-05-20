from dataclasses import dataclass, field
from typing import List

from .utils import Deck


@dataclass
class Player:
    stack: int
    hand: List[int] = field(default_factory=list)
    folded: bool = False


@dataclass
class GameState:
    players: List[Player]
    board: List[int]
    pot: int
    current_player: int


class TexasHoldem:
    """Simplified Texas Hold'em environment for 6 players."""

    def __init__(self, num_players: int = 6, starting_stack: int = 100):
        self.num_players = num_players
        self.starting_stack = starting_stack
        self.reset()

    def reset(self) -> GameState:
        self.deck = Deck()
        players = [Player(self.starting_stack, hand=self.deck.deal(2))
                   for _ in range(self.num_players)]
        board: List[int] = []
        self.state = GameState(players=players, board=board, pot=0, current_player=0)
        return self.state

    def deal_flop(self):
        self.state.board.extend(self.deck.deal(3))

    def deal_turn(self):
        self.state.board.extend(self.deck.deal(1))

    def deal_river(self):
        self.state.board.extend(self.deck.deal(1))

    def step(self, action: str):
        """Very simplified betting mechanic."""
        player = self.state.players[self.state.current_player]
        if action == 'fold':
            player.folded = True
        elif action == 'call':
            call_amount = 1
            player.stack -= call_amount
            self.state.pot += call_amount
        elif action == 'raise':
            raise_amount = 2
            player.stack -= raise_amount
            self.state.pot += raise_amount
        self.state.current_player = (self.state.current_player + 1) % self.num_players

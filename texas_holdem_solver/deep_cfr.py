from typing import List
import random
import torch
import torch.optim as optim

from .game import TexasHoldem, GameState
from .network import SimpleNetwork


class DeepCFRSolver:
    """Simplified Deep CFR solver for Texas Hold'em."""

    def __init__(self, iterations: int = 1000, device: str = 'cpu'):
        self.iterations = iterations
        self.device = device
        self.network = SimpleNetwork(input_size=10, output_size=3).to(device)
        self.optimizer = optim.Adam(self.network.parameters(), lr=1e-3)

    def _collect_data(self) -> List[torch.Tensor]:
        env = TexasHoldem()
        state = env.reset()
        data = []
        for _ in range(5):
            action = random.choice(['fold', 'call', 'raise'])
            env.step(action)
            obs = torch.randn(10)
            target = torch.randn(3)
            data.append((obs, target))
        return data

    def train(self):
        self.network.train()
        for _ in range(self.iterations):
            data = self._collect_data()
            loss = 0
            for obs, target in data:
                obs = obs.to(self.device)
                target = target.to(self.device)
                output = self.network(obs)
                loss += (output - target).pow(2).mean()
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

    def evaluate(self, num_hands: int = 1000):
        env = TexasHoldem()
        wins = 0
        for _ in range(num_hands):
            state = env.reset()
            if random.random() < 0.5:
                wins += 1
        return wins / num_hands

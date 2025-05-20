import torch
import torch.nn as nn


class SimpleNetwork(nn.Module):
    """Simple feed-forward network used as function approximator."""

    def __init__(self, input_size: int, output_size: int, hidden_size: int = 128):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)

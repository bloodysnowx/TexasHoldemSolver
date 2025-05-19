# TexasHoldemSolver

No-limit 6-handed Texas Hold'em Solver using Deep CFR in Python.

## Installation

First, install dependencies:

```bash
pip install -r requirements.txt
```

Then install the package in editable mode:

```bash
pip install -e .
```

## Usage

Train a Deep CFR solver:

```bash
ths train --iterations 100000 --output-dir models/
```

Evaluate a trained model:

```bash
ths evaluate --model-path models/model.pth --num-hands 10000
```

Play against the solver:

```bash
ths play --model-path models/model.pth
```

## Project Structure

- `texas_holdem_solver/`: Python package
- `cli.py`: Command-line interface module
- `game.py`: Game definitions and abstractions
- `deep_cfr.py`: Deep CFR implementation
- `network.py`: Neural network definitions
- `utils.py`: Utility functions
- `tests/`: Unit tests

import argparse
import os
import random

from .deep_cfr import DeepCFRSolver
from .game import TexasHoldem
from .utils import card_to_str


def train(args):
    solver = DeepCFRSolver(iterations=args.iterations)
    solver.train()
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        model_path = os.path.join(args.output_dir, "model.pth")
        solver.save(model_path)


def evaluate(args):
    solver = DeepCFRSolver(model_path=args.model_path)
    win_rate = solver.evaluate(num_hands=args.num_hands)
    print(f"Win rate: {win_rate:.2f}")


def play(args):
    solver = DeepCFRSolver(model_path=args.model_path)
    env = TexasHoldem()
    state = env.reset()
    env.deal_flop()
    env.deal_turn()
    env.deal_river()

    player = state.players[0]
    print("Your hand:", " ".join(card_to_str(c) for c in player.hand))
    rounds = ["pre-flop", "flop", "turn", "river"]
    for r in rounds:
        if player.folded:
            break
        action = input(f"{r} action (fold/call/raise): ")
        if action not in ("fold", "call", "raise"):
            action = "call"
        env.step(action)
        for _ in range(env.num_players - 1):
            env.step(random.choice(["fold", "call", "raise"]))

    print("Board:", " ".join(card_to_str(c) for c in state.board))
    print("Pot:", state.pot)


def main():
    parser = argparse.ArgumentParser(description="Texas Hold'em Deep CFR Solver")
    subparsers = parser.add_subparsers(dest='command')

    train_parser = subparsers.add_parser('train')
    train_parser.add_argument('--iterations', type=int, default=1000)
    train_parser.add_argument('--output-dir', type=str, default=None)
    train_parser.set_defaults(func=train)

    eval_parser = subparsers.add_parser('evaluate')
    eval_parser.add_argument('--num-hands', type=int, default=1000)
    eval_parser.add_argument('--model-path', type=str, default=None)
    eval_parser.set_defaults(func=evaluate)

    play_parser = subparsers.add_parser('play')
    play_parser.add_argument('--model-path', type=str, default=None)
    play_parser.set_defaults(func=play)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

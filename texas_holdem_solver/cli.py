import argparse

from .deep_cfr import DeepCFRSolver


def train(args):
    solver = DeepCFRSolver(iterations=args.iterations)
    solver.train()


def evaluate(args):
    solver = DeepCFRSolver()
    win_rate = solver.evaluate(num_hands=args.num_hands)
    print(f"Win rate: {win_rate:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Texas Hold'em Deep CFR Solver")
    subparsers = parser.add_subparsers(dest='command')

    train_parser = subparsers.add_parser('train')
    train_parser.add_argument('--iterations', type=int, default=1000)
    train_parser.set_defaults(func=train)

    eval_parser = subparsers.add_parser('evaluate')
    eval_parser.add_argument('--num-hands', type=int, default=1000)
    eval_parser.set_defaults(func=evaluate)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

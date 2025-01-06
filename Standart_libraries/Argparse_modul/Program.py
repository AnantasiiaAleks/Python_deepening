import argparse

parser = argparse.ArgumentParser(description='Parser for HW')
parser.add_argument('numbers', type=int, nargs='*', help='some numbers')
parser.add_argument('text', type=str, nargs='*', help='some text')
parser.add_argument('--verbose', action='store_true', help='Дополнительный вывод')
parser.add_argument('--repeat', type=int, default=1, help='Повторения')
args = parser.parse_args()


if args.verbose:
    print(f'Получено: numbers={args.numbers}, text="{args.text}", повторить={args.repeat}')

print(f'numbers={args.numbers}, text={' '.join(args.text) * args.repeat}')
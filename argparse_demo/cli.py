import argparse
import sys

from argparse_demo.services import (
    python_version,
    ip_addresses,
    cpu_load,
    ram_available
)


HELP_TEXT = f'argparse demonstration'


def cli_logic(args: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog='argparse_demo',
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--python',
        default=False,
        type=bool,
        help='python version',
    )
    parser.add_argument(
        '--ip',
        type=bool,
        help='ip address list'
    )
    parser.add_argument(
        '--cpu',
        default=False,
        type=bool,
        help='cpu load',
    )
    parser.add_argument(
        '--ram',
        default=False,
        type=bool,
        help='ram available',
    )
    parser.add_argument(
        '--int',
        default=0,
        type=int,
        help='any int',
    )

    parsed_args = parser.parse_args(args)

    if parsed_args.python:
        print(f'python version {python_version()}')

    if parsed_args.ip:
        for address in ip_addresses():
            print(f'ip: {address}')

    if parsed_args.cpu:
        print(f'cpu load {cpu_load()}')

    if parsed_args.ram:
        print(f'ram available {ram_available() / 1024 ** 2}')

    if parsed_args.int:
        print(f'int arg {parsed_args.int}')

    return 0


def cli():
    exit(
        cli_logic(
            sys.argv[1:]
        )
    )

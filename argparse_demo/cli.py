from argparse import ArgumentParser, RawTextHelpFormatter
from sys import argv as sys_argv

from argparse_demo.services import ip_addresses, cpu_load, ram_available


HELP_TEXT = f'argparse demonstration'


def cli_logic(args: list[str]) -> int:
    parser = ArgumentParser(
        prog='argparse_demo',
        description=HELP_TEXT,
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        '--ip',
        action='store_true',
        help='show ip address list'
    )
    parser.add_argument(
        '--cpu',
        action='store_true',
        help='show cpu load',
    )
    parser.add_argument(
        '--ram',
        action='store_true',
        help='show ram available',
    )
    parser.add_argument(
        '--int',
        default=0,
        type=int,
        help='show any int',
    )

    parsed_args = parser.parse_args(args)

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
            sys_argv[1:]
        )
    )

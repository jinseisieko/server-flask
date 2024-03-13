import argparse
from typing import IO

import click
import requests
from pprint import pprint


@click.command(epilog="Text at the bottom of help")
@click.argument('filename', type=click.File())
@click.option('-c', '--count', default=1, type=int, help="Number")
@click.option('-v', '--verbose', is_flag=True, help="Flag")
def main(filename: IO, count, verbose):
    """What the program does"""
    click.echo((filename.read(), count, verbose))


if __name__ == '__main__':
    main()
#
# parser = argparse.ArgumentParser(
#     prog='ProgramName',
#     description='What the program does',
#     epilog='Text at the bottom of help')
#
# parser.add_argument('filename')  # positional argument
# parser.add_argument('-c', '--count', type=int)  # option that takes a value
# parser.add_argument('-v', '--verbose',
#                     action='store_true')  # on/off flag
#
# args = parser.parse_args()
# print(args.filename, args.count, args.verbose)

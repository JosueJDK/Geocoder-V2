#!/usr/bin/env python

import argparse
import os

VERSION = None
from geocode.config import config


def main():
    if VERSION:
        print("Geocode", VERSION)
    main_parser = argparse.ArgumentParser(
        description="Geocode command line.", add_help=False
    )
    main_parser.add_argument("--config", help="Local config")
    args, extras = main_parser.parse_known_args()
    if args.config:
        os.environ["ADDOK_CONFIG_MODULE"] = args.config
    main_parser.add_argument(
        "-h", "--help", action="store_true", help="Show this help message and exit"
    )

    subparsers = main_parser.add_subparsers(title="Available commands", metavar="")

    from geocode.core import hooks

    config.load()
    hooks.register_command(subparsers)
    args = main_parser.parse_args(args=extras)
    if getattr(args, "func", None):
        args.func(args)
    else:
        main_parser.print_help()


if __name__ == "__main__":
    main()

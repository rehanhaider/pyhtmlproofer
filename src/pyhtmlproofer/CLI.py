from .main import file, directories, links
import argparse
import sys


class CLI:
    def main():
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest="command")
        subparser.required = True

        check = subparser.add_parser("check", help="Check a file, directory, or URL")
        check.add_argument("-F", "--file", help="Check a file")
        check.add_argument("-D", "--directories", nargs="+", help="Check list of directories")
        check.add_argument("-L", "--links", nargs="+", help="Check list of links")

        args = parser.parse_args()

        # Ensure that maximum of one of the options is specified
        if sum(1 for x in [args.file, args.directories, args.links] if x) > 1:
            parser.error("Only one of -F/--file, -D/--directories, or -L/--links may be specified")

        if args.file:
            file(args.file).check()
        elif args.directories:
            directories(args.directories).check()
        elif args.links:
            links(args.links).check()
        else:
            parser.error("No command specified")

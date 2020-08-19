import configparser
import subprocess
import os
import sys


DEFAULT_INIT_FILE = """\
[p8]
failfast = true

[black]
command = black --line-length 120 .

[flake8]
command = flake8 --ignore E501

[mypy]
command = mypy --ignore-missing-imports .
"""


def generate_default_init_file():
    with open("p8.ini", "w") as f:
        f.write(DEFAULT_INIT_FILE)


def init():
    if os.path.exists("p8.ini"):
        sys.exit("p8.ini already exists, please remove it to generate new one")
    generate_default_init_file()
    print("Wrote p8.ini")
    sys.exit(0)


def run():
    # TODO: not run if no arg passed or no config file exits
    # because accidentally run black8 . on top level dir is dangerous

    Config = configparser.ConfigParser()
    found = Config.read("p8.ini")
    if not found and len(sys.argv) == 1:
        sys.exit(
            "No p8.ini file found in current directory,"
            " please create by `p8 init` or passing directory for black/flake8/mypy"
        )
        # TODO handle when passing directory/file

    commands = []
    for section in Config.sections():
        if section == "p8":
            continue
        if Config.has_option(section, "command"):
            command = Config.get(section, "command")
            commands.append(command)

    failfast = Config.getboolean("p8", "failfast")

    exitcodes = set()
    for cmd in commands:
        exitcode, output = subprocess.getstatusoutput(cmd)
        exitcodes.add(exitcode)
        print("Running: {!r}".format(cmd))
        print("Output: {}".format(output))
        print("Exit code: {}".format(exitcode))
        if failfast and exitcode != 0:
            sys.exit(exitcode)

    if exitcodes != {0}:
        sys.exit(1)
    else:
        sys.exit(0)


def main():

    if len(sys.argv) == 1:
        run()
    else:
        cmd = sys.argv[1]
        # TODO use argparse here to handle args
        if cmd == "init":
            init()


if __name__ == "__main__":
    main()

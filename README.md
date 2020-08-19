# P8 - The Python ultimate meta linter

## Why?
To easily ensuring modern Python code quality in multiple projects.

A new Python developer on Windows may not know:

- How to set PATH
- How to invoke command installed via pip: e.g flake8
- How to install make and write Makefile
- How to setup git precommit

This program helps ensuring code quality without above hassle, it runs commands
by default includes:

- `black`
- `flake8`
- `mypy` - it not only work when type annotation exists, it can detect type by
itself for some cases, and detect error like `print("%s %s", missing_one_arg)`.

## Install

`pip install p8`

## Usage
- `p8 init` creates a config file `p8.ini`
- `p8` runs all commands defined in `p8.ini`, order matters.
- Installing those commands are users responsibility.
- On Windows, use `py -m p8 init` and `py -m p8` instead.

## TODO
- Test and fully support Windows
- Add option to install default suite `flake8 black mypy`
- Generate Makefile

# Authors
- Viet Hung Nguyen <hvn@familug.org>

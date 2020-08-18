# P8 - The Python ultimate meta linter

## Why?
To ensuring modern Python code quality in multiple projects.

`mypy` not only work when type annotation exists, it can detect type by itself
for some cases, and detect error like `print("%s %s", missing_one_arg)`.

## Install

`pip install p8`

## Usage
- `p8 init` creates a config file `p8.ini`
- `p8` runs all commands defined in `p8.ini`, order matters.
- Install those command are users responsible

## TODO
- Add option to install default suite `flake8 black mypy`
- Generate Makefile

# Authors
- Viet Hung Nguyen <hvn@familug.org>

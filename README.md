# Advent Of Code

These are my solutions to [Advent of Code](https://adventofcode.com)

I started solving advent of code since 2024

## Project Setup

### Before usage

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

### Usage

#### First time

- `cp .env.example .env`
- Authenticate at [Advent of Code](https://adventofcode.com)
- Copy `session` cookie from browser to `.env`

#### Generally

- `./get-input.py -y <YEAR> -d <DAY>`
- If needed copy test input to `<YEAR>/<DAY>/test.txt`
- Write code in `<YEAR>/<DAY>/main.py`
- `./run-solution.py -y <YEAR> -d <DAY> [-t,--test]`

### After usage

- `deactivate`

## Note

- All commands in this file are unix based, convert if necessary
- `boilerplate.py` contains boilerplate for `<YEAR>/<DAY>/main.py`
- If `-t` flag is passed to `./run-solution.py`, test input will be used

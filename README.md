# Advent Of Code

These are my solutions to [Advent of Code](https://adventofcode.com)

I started solving advent of code since 2024

## Project Setup

### Pre-Usage

- `python -m venv .venv`
- Activate the `venv`
- `pip install -r requirements.txt`

### Usage

#### First time

- `cp .env.example .env`
- Authenticate at [Advent of Code](https://adventofcode.com)
- Copy `session` cookie from browser to `SESSION` in `.env`

#### Generally

- `python ./config/cli.py`
- Write code in `src/<YEAR>/<DAY>/main.py`

### After usage

- Deactivate the `venv`

## Note

- `template/python.py` contains boilerplate for `src/<YEAR>/<DAY>/main.py`
- Test input is not readily available for scrapping in AoC, hence be aware of wrong test case

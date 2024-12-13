#!.venv/bin/python3
#!.venv/bin/python3

from argparse import ArgumentParser

import os
import subprocess


parser = ArgumentParser(description="Execute a solution")
parser.add_argument("-y", "--year", type=int, required=True)
parser.add_argument("-d", "--day", type=int, required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument("-t", "--test", action="store_true")
group.add_argument("-b", "--both", action="store_true")
args = parser.parse_args()

basePath = os.getcwd()
dirPath = os.path.join(basePath, f"{args.year}", f"{args.day}")

testCommand = ["python3", "main.py", "-t"]
inputCommand = ["python3", "main.py"]

try:
    os.chdir(dirPath)
    if args.both or args.test:
        subprocess.run(testCommand, check=True)
    if args.both or not args.test:
        subprocess.run(inputCommand, check=True)
    os.chdir(basePath)
except subprocess.CalledProcessError as e:
    print("Something went wrong")
    print(e)

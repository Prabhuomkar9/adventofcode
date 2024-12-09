#!.venv/bin/python3
from argparse import ArgumentParser
from dotenv import load_dotenv

import requests
import os


load_dotenv()

session = os.getenv("SESSION")
if session is None:
    print("Please set SESSION in .env file")
    exit(1)

parser = ArgumentParser(description="Read input")
parser.add_argument("-y", "--year", type=int, required=True)
parser.add_argument("-d", "--day", type=int, required=True)
args = parser.parse_args()


try:
    url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
    response = requests.get(url, cookies={"session": session})

    if response.status_code == 200:
        dirPath = os.path.join(os.getcwd(), f"{args.year}", f"{args.day}")
        filePath = os.path.join(dirPath, "input.txt")

        os.makedirs(dirPath, exist_ok=True)
        with open(filePath, "w") as file:
            file.write(response.text)
    else:
        print("Failed to get input")
        print(response.text)
except Exception as e:
    print("Something went wrong")
    print(e)

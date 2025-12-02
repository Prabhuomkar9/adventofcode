from argparse import ArgumentParser
from dotenv import load_dotenv

import os
import requests
import shutil


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
        inputPath = os.path.join(dirPath, "input.txt")
        testPath = os.path.join(dirPath, "test.txt")

        os.makedirs(dirPath, exist_ok=True)
        with open(inputPath, "w") as file:
            file.write(response.text)
        with open(testPath, "x") as file:
            pass

        bolierPlatePath = os.path.join(os.getcwd(), "boilerplate.py")
        sourceCodePath = os.path.join(dirPath, "main.py")

        if not os.path.exists(sourceCodePath):
            shutil.copyfile(bolierPlatePath, sourceCodePath)
    else:
        print("Failed to get input")
        print(response.text)
except Exception as e:
    print("Something went wrong")
    print(e)

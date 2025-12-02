from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import subprocess
import os
import time

from utils import Utils
from webClient import WebClient


class Cli:
    def __init__(self) -> None:
        self.config = Utils.get_config()
        self.web_client = WebClient(self.config)

        action = inquirer.select(  # type: ignore
            message="Select Action:",
            choices=[
                Choice(
                    value="run_solution",
                    name="Run Solution",
                ),
                Choice(
                    value="get_puzzle",
                    name="Get Puzzle",
                ),
                Choice(
                    value="submit_solution",
                    name="Submit Solution",
                ),
                Choice(
                    value="seed_config",
                    name="Seed Config",
                ),
            ],
            default="run_solution",
        ).execute()

        match action:
            case "seed_config":
                self.__seed_config()
            case "run_solution":
                self.__run_solution()
            case "submit_solution":
                self.__submit_solution()
            case "get_puzzle":
                self.__get_puzzle()

    def __get_input_type(self):
        return inquirer.select(  # type: ignore
            message="Select Input Type:",
            choices=[
                Choice(value="actual", name="Actual Input"),
                Choice(value="test", name="Test Input"),
            ],
            default="actual",
        ).execute()

    def __get_year(self):
        years = self.config["puzzles"].keys()
        if not years:
            print("No years found in config. Please seed the config first.")
            exit(1)

        return inquirer.select(  # type: ignore
            message="Select Year:",
            choices=[Choice(value=year, name=year) for year in years],
        ).execute()

    def __get_day(self, year: int):
        days = self.config["puzzles"][f"{year}"]
        if not days:
            print(
                "No days found in config for the selected year. Please seed the config first."
            )
            exit(1)

        return inquirer.select(  # type: ignore
            message="Select Day:",
            choices=[Choice(value=f"{day}", name=f"{day}") for day in days],
        ).execute()

    def __get_part(self):
        return inquirer.select(  # type: ignore
            message="Select Part:",
            choices=[
                Choice(value="1", name="Part 1"),
                Choice(value="2", name="Part 2"),
            ],
            default="1",
        ).execute()

    def __seed_config(self):
        years = self.web_client.get_years()

        config = {"puzzles": {}}

        for year in years:
            days = self.web_client.get_days(int(year))
            config["puzzles"][year] = days

        Utils.save_config(config)

    def __run_solution(self):
        input_type = self.__get_input_type()
        year = self.__get_year()
        day = self.__get_day(year)

        puzzle_dir_path = Utils.get_puzzle_dir_path(year, day)

        testCommand = ["python", "main.py", "-t"]
        actualCommand = ["python", "main.py"]

        match input_type:
            case "test":
                a = subprocess.run(testCommand, check=True, cwd=puzzle_dir_path)
                print(a)
            case "actual":
                a = subprocess.run(actualCommand, check=True, cwd=puzzle_dir_path)
                print(a)

    def __submit_solution(self):
        part = self.__get_part()
        self.__run_solution()

    def __get_puzzle(self):
        year = self.__get_year()
        day = self.__get_day(year)

        for i in range(10):
            print(f"Getting puzzle in {10 - i}...")
            time.sleep(1)

        if self.web_client.check_day(year, day):
            actual_input = self.web_client.get_actual_input(year, day)
            test_input = self.web_client.get_test_input(year, day)

            Utils.create_test_input(year, day, test_input)
            Utils.create_actual_input(year, day, actual_input)
            source_code_path = Utils.create_boilerplate(year, day)

            self.config["puzzles"][f"{year}"].insert(0, f"{day}")

            Utils.save_config(self.config)

            print(f"New puzzle found: {source_code_path}")
        else:
            print("No new puzzle found.")


if __name__ == "__main__":
    cli = Cli()

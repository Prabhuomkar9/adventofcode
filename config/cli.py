from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import subprocess
import os
import time

from utils import Utils
from client import Client


class Cli:
    """
    Command Line Interface for Advent of Code interactions
    """

    def __init__(self) -> None:
        self.config = Utils.get_config()
        self.web_client = Client(self.config)

        action = inquirer.select(  # type: ignore
            message="Select Action:",
            choices=[
                Choice(
                    value="seed_config",
                    name="Seed Config",
                ),
                Choice(
                    value="get_puzzle",
                    name="Get Puzzle",
                ),
                Choice(
                    value="run_solution",
                    name="Run Solution",
                ),
                Choice(
                    value="submit_solution",
                    name="Submit Solution",
                ),
            ],
            default="run_solution",
        ).execute()

        match action:
            case "seed_config":
                self.__seed_config()
            case "get_puzzle":
                self.__get_puzzle()
            case "run_solution":
                self.__run_solution()
            case "submit_solution":
                self.__submit_solution()

    def __get_input_type(self):
        """
        Get the type of input to work with.
        """
        return inquirer.select(  # type: ignore
            message="Select Input Type:",
            choices=[
                Choice(value="actual", name="Actual Input"),
                Choice(value="test", name="Test Input"),
            ],
            default="actual",
        ).execute()

    def __get_year(self):
        """
        Get the year of the puzzle to work with.
        """
        years = self.config["puzzles"].keys()
        if not years:
            print("No years found in config. Please seed the config first.")
            exit(1)

        latest_year = max(int(year) for year in years)
        new_year = latest_year + 1

        return inquirer.select(  # type: ignore
            message="Select Year:",
            choices=[Choice(value=new_year, name=f"{new_year}(New)")]
            + [Choice(value=int(year), name=year) for year in years],
            default=latest_year,
        ).execute()

    def __get_day(self, year: int):
        """
        Get the day of the puzzle to work with.
        """
        days = self.config["puzzles"][f"{year}"]
        if not days:
            print(
                "No days found in config for the selected year. Please seed the config first."
            )
            exit(1)

        latest_day = max(days)
        new_day = latest_day + 1

        return inquirer.select(  # type: ignore
            message="Select Day:",
            choices=[Choice(value=new_day, name=f"{new_day}(New)")]
            + [Choice(value=day, name=f"{day}") for day in days],
            default=latest_day,
        ).execute()

    def __get_part(self):
        """
        Get the part of the puzzle to work with.
        """
        return inquirer.select(  # type: ignore
            message="Select Part:",
            choices=[
                Choice(value=1, name="Part 1"),
                Choice(value=2, name="Part 2"),
            ],
            default=1,
        ).execute()

    def __seed_config(self):
        """
        Seed the configuration file with available years and days.
        """
        years = self.web_client.get_years()

        config = {"puzzles": {}}

        for year in years:
            days = self.web_client.get_days(int(year))
            config["puzzles"][year] = days

        Utils.save_config(config)

    def __get_puzzle(self):
        """
        Get a new puzzle for a specific year and day.
        """
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

            if day not in self.config["puzzles"][f"{year}"]:
                self.config["puzzles"][f"{year}"].insert(0, day)

            Utils.save_config(self.config)

            print(f"New puzzle found: {source_code_path}")
        else:
            print("No new puzzle found.")

    def __code_runner(self, year: int, day: int, input_type: str):
        """
        Run the solution code for a specific year and day with selected input type.
        """
        puzzle_dir_path = Utils.get_puzzle_dir_path(year, day)

        testCommand = ["python", "main.py", "-t"]
        actualCommand = ["python", "main.py"]

        process = subprocess.run(
            testCommand if input_type == "test" else actualCommand,
            check=True,
            cwd=puzzle_dir_path,
            capture_output=True,
        )

        stdout = process.stdout.decode()
        if not stdout:
            raise Exception("No output from solution.")

        ans1, ans2 = stdout.splitlines()[0].split(" ")[3:5]

        return (ans1, ans2)

    def __run_solution(self):
        """
        Run the solution for a specific year and day with selected input type.
        """
        input_type = self.__get_input_type()
        year = self.__get_year()
        day = self.__get_day(year)

        return self.__code_runner(year, day, input_type)

    def __submit_solution(self):
        """
        Submit the solution for a specific year and day.
        """
        year = self.__get_year()
        day = self.__get_day(year)
        part = self.__get_part()

        ans1, ans2 = self.__code_runner(year, day, "actual")

        solved, text = self.web_client.submit_solution(
            year, day, part, ans1 if part == 1 else ans2
        )

        print(f"{'SUCCESS' if solved else 'FAILURE'}:\n {text}")


if __name__ == "__main__":
    cli = Cli()

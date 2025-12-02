import os
import json
from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel, ValidationError


class Config(BaseModel):
    puzzles: dict[str, list[int]]


class Utils:
    template_path = os.path.join(os.getcwd(), "template", "python.py")

    @staticmethod
    def get_session():
        load_dotenv()

        session = os.getenv("SESSION")
        if session is None:
            print("Please set SESSION in .env file")
            exit(1)

        return session

    @staticmethod
    def get_config():
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r") as file:
                    config = Config(**json.load(file))

                return config.model_dump()

            config = Config(
                **{
                    "puzzles": {},
                }
            )

            with open("config.json", "w") as file:
                json.dump(config.model_dump(), file, indent=4)

            return config.model_dump()
        except ValidationError as e:
            print("Invalid config:", e)
            exit(1)

    @staticmethod
    def save_config(config: dict):
        try:
            current_config = Utils.get_config()
            current_config.update(config)

            with open("config.json", "w") as file:
                json.dump(current_config, file, indent=4)
        except ValidationError as e:
            print("Invalid config:", e)
            exit(1)

    @staticmethod
    def reset_config() -> None:
        config = Utils.get_config()

        Utils.save_config(config)

    @staticmethod
    def get_puzzle_dir_path(year: int, day: int) -> str:
        return os.path.join(os.getcwd(), "src", f"{year}", f"{day}")

    @staticmethod
    def __create_puzzle_file(
        year: int,
        day: int,
        content: str,
        file_type: Literal["source_code", "actual_input", "test_input"],
    ):
        puzzle_dir_path = Utils.get_puzzle_dir_path(year, day)

        file_path = os.path.join(
            puzzle_dir_path,
            (
                "main.py"
                if file_type == "source_code"
                else "input.txt" if file_type == "actual_input" else "test.txt"
            ),
        )

        os.makedirs(puzzle_dir_path, exist_ok=True)

        if file_type == "source_code" and os.path.exists(file_path):
            return file_path

        with open(file_path, "w") as file:
            file.write(content)

        return file_path

    @staticmethod
    def create_boilerplate(year: int, day: int):
        with open(Utils.template_path, "r") as template_file:
            return Utils.__create_puzzle_file(
                year, day, template_file.read(), file_type="source_code"
            )

    @staticmethod
    def create_actual_input(year: int, day: int, content: str):
        return Utils.__create_puzzle_file(year, day, content, file_type="actual_input")

    @staticmethod
    def create_test_input(year: int, day: int, content: str):
        return Utils.__create_puzzle_file(year, day, content, file_type="test_input")


if __name__ == "__main__":
    pass

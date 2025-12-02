import requests
from bs4 import BeautifulSoup
import re

from utils import Utils


class WebClient:
    base_url = "https://adventofcode.com"

    def __init__(self, config: dict) -> None:
        self.session = Utils.get_session()
        self.config = config

    def get_years(self):
        """
        Get available years from Advent of Code
        """
        url = f"{self.base_url}/events"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        main_tag = soup.find("main")
        if not main_tag:
            raise Exception("Failed to get years: no main tag found")

        year_tags = main_tag.find_all("div", class_="eventlist-event")

        years: list[int] = []

        for year_tag in year_tags:
            anchor_tag = year_tag.find("a")
            if not anchor_tag:
                raise Exception("Failed to get years: no anchor tag found")

            text = anchor_tag.text

            years.append(int(text[1:-1]))

        years.sort(reverse=True)

        return years

    def get_days(self, year: int):
        """
        Get available days for a given year from Advent of Code"""
        url = f"{self.base_url}/{year}"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        main_tag = soup.find("main")
        if not main_tag:
            raise Exception("Failed to get days: no main tag found")

        day_tags = main_tag.find_all("a", class_=re.compile("calendar-day."))

        days: list[int] = []

        for day_tag in day_tags:
            span_tag = day_tag.find("span", class_="calendar-day")
            if not span_tag:
                raise Exception("Failed to get days: no span tag found")

            text = span_tag.text

            days.append(int(text))

        days.sort(reverse=True)

        return days

    def check_day(self, year: int, day: int):
        """
        Check if a given day exists for a given year"""
        url = f"{self.base_url}/{year}/day/{day}"
        response = requests.get(url)

        return response.status_code == 200

    def get_actual_input(self, year: int, day: int):
        """
        Get actual input for a given year and day
        """
        url = f"{self.base_url}/{year}/day/{day}/input"
        response = requests.get(url, cookies={"session": self.session})

        if response.status_code != 200:
            raise Exception("Failed to get input")

        return response.text

    def get_test_input(self, year: int, day: int):
        """
        Get test input for a given year and day
        Note: Prone to be wrong if AoC changes their HTML structure
        """
        url = f"{self.base_url}/{year}/day/{day}"
        response = requests.get(url, cookies={"session": self.session})

        if response.status_code != 200:
            raise Exception("Failed to get test input")

        soup = BeautifulSoup(response.text, "html.parser")

        main_tag = soup.find("main")
        if not main_tag:
            raise Exception("Failed to get test input: no main tag found")

        hopefully_test_pre_tag = main_tag.find("pre")
        if not hopefully_test_pre_tag:
            raise Exception("Failed to get test input: no pre tag found")

        code_tag = hopefully_test_pre_tag.find("code")
        if not code_tag:
            raise Exception("Failed to get test input: no code tag found")

        return code_tag.text

    def submit_solution(self, year: int, day: int, part: int, answer: str):
        """
        Submit solution for a given year, day, and part
        """
        url = f"{self.base_url}/{year}/day/{day}/answer"
        response = requests.post(
            url,
            data={"level": part, "answer": answer},
            cookies={"session": self.session},
        )

        if response.status_code != 200:
            raise Exception("Failed to submit solution")

        soup = BeautifulSoup(response.text, "html.parser")

        main_tag = soup.find("main")
        if not main_tag:
            raise Exception("Failed to submit solution: no main tag found")

        article_tag = main_tag.find("article")
        if not article_tag:
            raise Exception("Failed to submit solution: no article tag found")

        p_tag = article_tag.find("p")
        if not p_tag:
            raise Exception("Failed to submit solution: no p tag found")

        span_tag = p_tag.find("span")
        if not span_tag:
            raise Exception("Failed to submit solution: no span tag found")

        if span_tag.has_attr("class"):
            # TODO: remove the print
            print("here:", span_tag["class"])
            if "day-success" in span_tag["class"]:
                return (True, article_tag.text.strip())

        return (False, article_tag.text.strip())


if __name__ == "__main__":
    pass

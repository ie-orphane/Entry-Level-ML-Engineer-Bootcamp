import sys
import requests
from bs4 import BeautifulSoup
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrapper.py FILENAME")
        quit()

    response = requests.get("https://data.1337ai.org/")

    soup = BeautifulSoup(response.text, "html.parser")

    for row in soup.find_all("tr"):
        with open(Path(__file__).parent / sys.argv[1], "a") as f:
            print(",".join([element.text for element in row.contents]), file=f)

from io import BytesIO
from re import findall
from typing import Any

import requests
from django.core.files import File
from lxml.html import HtmlElement

DATE_REGEX = r"(\d{1,2})\.\s(\w+)\s(\d{4})\.\s*(\d{2}\.\d{2})*"
MONTHS = {
    "januara": 1,
    "februara": 2,
    "marta": 3,
    "aprila": 4,
    "maja": 5,
    "juna": 6,
    "jula": 7,
    "avgusta": 8,
    "septembra": 9,
    "oktobra": 10,
    "novembra": 11,
    "decembra": 12,
}


# TODO: Add UTC
def parse_date(text: str) -> str:
    grps = findall(DATE_REGEX, text)[0]
    day = str(grps[0]).rjust(2, "0")
    month = str(MONTHS[grps[1]]).rjust(2, "0")
    year = grps[2]
    time = grps[3].replace(".", ":")

    return f"{year}-{month}-{day} {time}"


def strip_list(x: list[str]) -> list[str]:
    if isinstance(x, str):
        return [x.strip()]
    return [i.strip() for i in x]


def save_image(x: str) -> File:
    resp = requests.get(x)
    # TODO: Check resp status
    return File(BytesIO(resp.content), name=str(hash(x)))


def scrape_page_data(
    doc: HtmlElement, xpaths: dict[str, tuple[str, Any]]
) -> dict[str, Any]:
    data = {}

    for k, v in xpaths.items():
        try:
            data[k] = doc.xpath(v[0])
            if len(data[k]) == 0:
                del data[k]
                continue
            if len(data[k]) == 1:
                data[k] = data[k][0]
            if len(v) == 2:
                data[k] = v[1](data[k])
        except Exception as e:
            # TODO: Log something
            pass

    return data

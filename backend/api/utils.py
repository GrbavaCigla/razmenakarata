from typing import List
from re import match

DATE_REGEX = r'(\d{1,2})\.\s(\w+)\s(\d{4})\.\s(\d{2}:\d{2})'
MONTHS = {
    'januara': 1,
    'februara': 2,
    'marta': 3,
    'aprila': 4,
    'maja': 5,
    'juna': 6,
    'jula': 7,
    'avgusta': 8,
    'septembra': 9,
    'oktobra': 10,
    'novembra': 11,
    'decembra': 12
}


def parse_date(text: str):
    grps = match(DATE_REGEX, text).groups()
    day = str(grps[0]).rjust(2, '0')
    month = str(MONTHS[grps[1]]).rjust(2, '0')
    year = grps[2]
    time = grps[3]

    return f'{year}-{month}-{day} {time}'
        
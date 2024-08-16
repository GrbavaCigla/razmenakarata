from .utils import parse_date, save_image, strip_list

GRID_XPATH = '//div[@class="gt-col"]'
LANDING_XPATHS = {
    "id": (".//div/@data-event-id", lambda x: int(x)),
    "name": ('.//div[@class="gt-title"]/a/text()',),
    "city": ('.//div[@class="gt-location"]//a/text()',),
    "thumbnail": ('.//div[@class="gt-image"]//img/@src', save_image),
    "start_date": ('.//div[@class="gt-date"]//span/text()', parse_date),
    "categories": ('.//div[@class="gt-category"]//a/text()', strip_list),
    "page": ('.//div[@class="gt-title"]/a/@href',),
}
PART_XPATHS = {
    "date": '//div[@class="gt-content"]//div[@class="gt-inner"]/text()',
    "details": '//div[@class="gt-content-detail-box"]/ul',
}
XPATHS = {
    "start_date": ('.//li[@class="gt-start-date"]' + PART_XPATHS["date"], parse_date),
    "end_date": ('.//li[@class="gt-end-date"]' + PART_XPATHS["date"], parse_date),
    "location": (
        './/li[@class="gt-venue"]//div[@class="gt-content"]//div[@class="gt-inner"]//a/text()',
    ),
    "description": (
        '//div[@class="gt-event-sections"]/div[1]//p/text()',
        lambda x: " ".join(x).replace("\n", " "),
    ),
    "packages": ('//div[@class="gt-tickets-title"]/text()', strip_list),
}

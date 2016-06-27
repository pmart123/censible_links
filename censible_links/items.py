from scrapy.item import Item, Field


class Page(Item):
    title = Field()
    h1 = Field()
    href = Field()
    meta = Field()

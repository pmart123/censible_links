from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from censible_links.items import Page


class CensibleCrawlSpider(CrawlSpider):
    name = 'censible_crawl'
    allowed_domains = ['censible.co']
    start_urls = ['https://censible.co/']

    rules = (
        Rule(LinkExtractor(allow=('.*')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('Response from %s ', response.url)
        # Scraping item (page) content
        item = Page()
        selector = Selector(response)
        item['title'] = selector.xpath('//title/text()').extract()
        item['h1'] = selector.xpath('//h1/text()').extract()
        item['href'] = selector.xpath('//a/@href').extract()
        item['meta'] = selector.xpath('//meta[@name=\'description\']/@content').extract()

        return item

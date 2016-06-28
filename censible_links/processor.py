from scrapy.crawler import CrawlerProcess

from censible_links.spiders import CensibleCrawlSpider


def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(CensibleCrawlSpider)
    process.start()


if __name__ == '__main__':
    main()

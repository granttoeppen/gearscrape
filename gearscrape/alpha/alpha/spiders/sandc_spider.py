from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector

from alpha.items import DealItem

class SAndCSpider(BaseSpider):
    name = "steepandcheap"
    allowed_domains = ["feedburner.com"]
    start_urls = [
        "http://feeds.feedburner.com/steepandcheap"
    ]

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        xxs.register_namespace('sac', 'http://www.steepandcheap.com/docs/steepcheap/rss.xml')
        deals = xxs.select('//item')
        items = []
        for deal in deals:
            item = DealItem()
            item['title'] = deal.select('title/text()').extract()
            item['link'] = deal.select('link/@href').extract()
            item['desc'] = deal.select('description/text()').extract()
            item['shortDesc'] = deal.select('sac:listDescription/text()').extract()
            item['curPrice'] = deal.select('sac:priceCurrent/text()').extract()
            item['regPrice'] = deal.select('sac:priceRegular/text()').extract()
            items.append(item)
            return items
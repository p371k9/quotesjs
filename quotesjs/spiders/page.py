import scrapy
import os
from ..items import QuotesjsItem
#from scrapy.shell import inspect_response

class PageSpider(scrapy.Spider):
    name = 'page'    
    start_urls = []
    
    def __init__(self, dir='pages', *args, **kwargs):        
        absPath = os.path.abspath(dir)
        htmls = os.listdir(dir)
        htmls.sort()
        for h in htmls:
            self.start_urls.append('file://' + absPath + '/' + h)                    
        
    def parse(self, response):        
        self.logger.debug("This is the parse page func")
        for sect in response.xpath('//div[@class="quote"]'):
            item = QuotesjsItem()
            item["text"] = sect.xpath('span[@class="text"]/text()').get()
            item["author"] = sect.xpath('span/small[@class="author"]/text()').get()
            tags = ''
            for t in sect.xpath('div[@class="tags"]/a/text()').extract():
                tags = tags + ' ' + t if len(tags) else t
            item['tags'] =  tags            
            item["url"] = response.url
            self.logger.info(item)
            yield item

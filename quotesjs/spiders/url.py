import scrapy
from .page import PageSpider
from urllib.parse import urljoin
#from scrapy.shell import inspect_response

from scrapy.exporters import CsvItemExporter
# Adding .lll file ext.  = headless .csv , see: settings.py! custom_settings problematic. Seems not working without predefinition in seettings.py
class HeadlessCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['include_headers_line'] = False
        super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)

class UrlSpider(PageSpider):
    name = 'url'
    base = 'http://quotes.toscrape.com'    
        
    def parse(self, response):        
        self.logger.debug("This is the parse page func")
        if response.url == self.start_urls[0]:
            u = urljoin(self.base, 'js/')
            yield {
                'url': u
            }
        n = response.xpath('//li[@class="next"]/a/@href').get()
        #inspect_response(response, self)  
        if type(n) is str:
            u = urljoin(self.base, n)
            yield {
                'url': u
            }


import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # identifies the spider, unique in a project

    def start_requests(self):
        """

        :return: an iterable of Requests, either a list or a generator
        """

        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parses the response:
        1. extract data as dicts
        2. find new URLs to follow
        3. create new requests

        :param response:
        :return:
        """
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

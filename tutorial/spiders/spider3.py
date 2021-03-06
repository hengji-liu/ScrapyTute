import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            # <div class="quote">
            #     <span class="text">“The world as we have created it is a process of our
            #     thinking. It cannot be changed without changing our thinking.”</span>
            #     <span>
            #         by <small class="author">Albert Einstein</small>
            #         <a href="/author/Albert-Einstein">(about)</a>
            #     </span>
            #     <div class="tags">
            #         Tags:
            #         <a class="tag" href="/tag/change/page/1/">change</a>
            #         <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
            #         <a class="tag" href="/tag/thinking/page/1/">thinking</a>
            #         <a class="tag" href="/tag/world/page/1/">world</a>
            #     </div>
            # </div>

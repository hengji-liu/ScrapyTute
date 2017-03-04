import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            # supports relative url, no need to urljoin
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parse)

            # for <a> element, there is also a shortcut
            # for a in response.css('li.next a'):
            #     yield response.follow(a, callback=self.parse)

            # <ul class ="pager">
            #   <li class ="next">
            #       <a href = "/page/2/"> Next <span aria-hidden="true">&rarr;</span></a>
            #   </li>
            # </ul>

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

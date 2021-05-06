import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ['https://bluelimelearning.github.io/my-fav-quotes/']

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),           # for multiple line
                'author':quote.css('p.author::text').extract_first(),    # for single line
            }



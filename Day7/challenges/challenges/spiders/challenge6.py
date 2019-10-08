### PURPOSE: Extract the product detail from https://scrapingclub.com/exercise/list_infinite_scroll/ such as title, description, and price from an infinite scrolling page. Try to crawl all product info.

import scrapy
import json

class InfiniteScrollScrape(scrapy.Spider):

    name = "infinite_scroll"
    test_urls = ["http://quotes.toscrape.com/api/quotes?page={}", "https://scrapingclub.com/exercise/list_infinite_scroll/"]
    start_urls = [test_urls[0].format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                "author": quote['author']['name'],
                "text": quote['text'],
                "tags": quote['tags'],
            }
        #check if there is another page to follow in the data
        if data['has_next']:
            next_page = data['page'] +1
            print("scraping page "+str(next_page))
            yield scrapy.Request(url = self.test_urls[0].format(next_page), callback = self.parse)

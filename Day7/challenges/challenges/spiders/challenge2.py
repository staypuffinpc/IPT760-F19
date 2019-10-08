### PURPOSE:  Extract the product detail from https://scrapingclub.com/exercise/detail_json/ such as title, description, and price from the json located at the bottom of the page.

import scrapy
import json #see https://stackoverflow.com/questions/18171835/scraping-a-json-response-with-scrapy
# from myproject.items import MyItem
#see https://docs.scrapy.org/en/latest/topics/developer-tools.html for a demo and explanation

class detail_json(scrapy.Spider):

    name ="detail_json"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data["quotes"]:
            yield {"quote": quote["text"]}

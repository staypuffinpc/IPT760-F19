### PURPOSE: To extract the product detail, such as title, description, and price, from https://scrapingclub.com/exercise/detail_basic/.  Extra points (up to 3) for using CSS, xPath, and regex extraction ###

import scrapy

class BasicDetail(scrapy.Spider):

    name = "basic_detail"
    start_urls = ["https://scrapingclub.com/exercise/detail_basic/"]

    def parse(self, response):

        # find the container for the info, then iterate through and yield the basic information
        card = response.css("div.card-body")
        yield {
            "name": response.css("div.card-body h3.card-title::text").get(),
            "price": response.xpath('//div[@class="card-body"]/h4/text()').get(),
            "description": response.css("div.card-body p::text").get(),
        }

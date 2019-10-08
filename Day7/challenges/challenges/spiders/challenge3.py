### PURPOSE: Extract all the product detail from https://scrapingclub.com/exercise/list_basic/ such as title, description, and price from the HTML by creating a spider. The spider should should go through every page and gather the information for each item on the page.

import scrapy

class AllProductDetail(scrapy.Spider):

    name = "all_product_detail"
    start_urls = ["https://scrapingclub.com/exercise/list_basic/"]

    def parse(self, response):
        #gets all data on a singl page
        for card in response.css("div.card"):
            yield { #should update so that I don't return null results
                "description": card.css("div.card-body h4 a::text").get(),
                "price" : card.css("div.card-body h5::text").get()
            }
        #get next button
        next_btn = response.xpath("//*[contains(text(), 'Next')]/@href").extract()[0]
        yield response.follow(next_btn,self.parse)

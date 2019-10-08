### PURPOSE: To extract the product detail, such as title, description, and price, from https://scrapingclub.com/exercise/detail_basic/.  Extra points (up to 3) for using CSS, xPath, and regex extraction ###

import scrapy
import re #needed for regex example (see https://www.accordbox.com/blog/scrapy-tutorial-11-how-to-extract-data-from-native-javascript-statement/)



class ProductDetails(scrapy.Spider):

    name = "product_details"
    start_urls = ['https://scrapingclub.com/exercise/detail_basic/']

    def parse(self, response):

        # get product name, price, and description
        card = response.css("div.card-body")
        yield {
            "product": card.css("h3.card-title::text").get(), #css demo
            "price" : re.findall("[$]\d+[.]\d*",response.body.decode("utf-8"))[0], #regex demo
            "description": card.xpath("//p[@class='card-text']//text()").extract(), #xpath demo
        }

### PURPOSE: show how to use scrapy using peterjrich.com ###

##import needed libraries
import scrapy

class PeterTitles(scrapy.Spider):

    #all spiders need names
    name = "titles"
    start_urls = [
        "http://peterjrich.com",
    ]

    def parse(self, response):
        # iterate over each header and get title and date info.  Export all info to .json file
        for header in response.css("header.entry-header"):

            #follow the link for each element
            url = response.css("h2.entry-title a::href")
            response.follow()

            # yield {
            #     "title": header.css("h2.entry-title a::text").get(),
            #     "updated": header.css("span.updated::text").get()
            # }

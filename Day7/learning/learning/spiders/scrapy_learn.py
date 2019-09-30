#### PURPOSE: To learn how to use scrapy to build a web spider ####

###IMPORTANT: make sure you have have done the following:
 ## pip install scrapy
    ## if you get an error installing the "wheel", you may need to grant permissions to xcode (even if you've done it previously).  Run this code first: sudo xcodebuild -license
## start a new scrapy project with the following scrapy command: scrapy startproject learning

## import needed libraries ##
import scrapy

# always need to create a class to scrape data
class QuotesSpider(scrapy.Spider):
    #must create a name for this spider
    name = "quotes"

    # if you want to use the built-in starter, use start_urls list, like so:
    # start_urls = [
    #     "http://quotes.toscrape.com/page/1/",
    #     "http://quotes.toscrape.com/page/2/",
    #     "http://quotes.toscrape.com/page/3/"
    # ]

    #get url data (like requests)
    def start_requests(self):
        urls = {
            "http://quotes.toscrape.com/page/1/"
            }

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            #NOTICE: yield is kind of like "return" but instead of recalculating the values each time, it adds to the generator.  Generators are like iterables, but instead of storing all the values in memory, it recalculates them each time.  These are useful for memory-intensive tasks.

    def parse(self, response): #code that handles the response
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # with open(filename, "wb") as file:
        #     file.write(response.body)
        # self.log("Saved file as {}".format(filename))
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall()
            }

        rel_next_page = response.css("li.next a::attr(href)").get()
        if rel_next_page is not None:
            abs_next_page = response.urljoin(rel_next_page)
            yield scrapy.Request(abs_next_page,callback=self.parse)

#to run this file, use the following command in your terminal: scrapy crawl quotes (where "quotes" is the name you gave the object)

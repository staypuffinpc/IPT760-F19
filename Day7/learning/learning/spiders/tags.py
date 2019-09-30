### PURPOSE: To demonstrate how to crawl and follow pages and return tag data ###

#import libraries
import scrapy

#base class
class TagSpider(scrapy.Spider):

    name = "tags"
    # start_urls = ["http://quotes.toscrape.com/page/1"]
    tags = [] # start an empty list of tags
    tag_counts = {} # count individual tag counts

    def start_requests(self):
        self.urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
            "http://quotes.toscrape.com/page/3/",
            "http://quotes.toscrape.com/page/4/",
            "http://quotes.toscrape.com/page/5/"
            # "http://quotes.toscrape.com/page/6/",
            ]

        for url in self.urls:
            yield scrapy.Request(url = url, callback = self.parse)
            #NOTICE: yield is kind of like "return" but instead of recalculating the values each time, it adds to the generator.  Generators are like iterables, but instead of storing all the values in memory, it recalculates them each time.  These are useful for memory-intensive tasks.


    def parse(self, response):
        #extract the tags of the quotes on the first 5 pages and provide a count of each tag.

        #get the tags for each div with tags (div.tags a::text)
        for tag in response.css("div.tags a::text").getall():
            if tag not in self.tags:
                self.tags.append(tag)
                self.tag_counts[tag] = 1
            else: #already in list, so increment count for that tag
                self.tag_counts[tag] += 1

        if response.url == self.urls[-1]:
            yield {
                    "count_all": len(self.tags),
                    "tags": self.tags,
                    "tag_counts": self.tag_counts,
                    }

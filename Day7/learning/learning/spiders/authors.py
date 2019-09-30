### PURPOSE: To show how to scrape author data from quotes.toscrape.com (follow a link and back)

## import needed libraries
import scrapy

class AuthorSpider(scrapy.Spider):
    name = "authors"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        # follow links to author pages
        for href in response.css(".author +a::attr(href)"):
            yield response.follow(href,callback = self.parse_author) #TODO: def parse_author()

        # follow page links
        for href in response.css("li.next a::href(href)"):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        # extract author data from second page
        def extract_with_css(query):
            return response.css(query).get(default = "").strip() #gets data usiing a css query and cleans it

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "year": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text")
        }

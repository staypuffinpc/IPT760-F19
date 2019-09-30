### To demonstrate how to scrape book data from books.toscrape.com ###

## import needed libraries
import scrapy

class BookSpider(scrapy.Spider):

    name = "books"
    count = 0
    count_max = 5
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        ## main page
        # title = response.css("article.product_pod a::attr(title)").get()
        # price = response.css("article.product_pod p.price_color::text").get()

        ## product page
        # title: response.css("div.product_main > h1::text").get()
        # price: response.css("p.price_color::text").get()
        # product description: response.css("#product_description +p::text").get()

        # follow links to author pages
        for href in response.css("h3 a::attr(href)"):
            yield response.follow(href, self.parse_books)

        # determine how many pages to scrape
        self.count += 1
        while self.count < self.count_max:
            for href in response.css("li.next a::attr(href)"):
                yield response.follow(href, self.parse)

    #get the data from each library page
    def parse_books(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "title": extract_with_css("div.product_main > h1::text"),
            "price": extract_with_css("p.price_color::text"),
            "description": extract_with_css("#product_description +p::text"),
        }

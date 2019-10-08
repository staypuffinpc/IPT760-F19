### PURPOSE: Create a spider that can handle the login form on https://scrapingclub.com/exercise/basic_login/. Use scrapingclub for both username and password.

import scrapy
from scrapy.http import FormRequest #to be able to process form data

class LoginChallenge(scrapy.Spider):

    name = "login"
    start_urls = ["https://scrapingclub.com/exercise/basic_login/"]

    def parse(self, response):
        #find the form elements
        csrf_token = response.css("form > input::attr(value)").get()
        # fill out each of the form elements and submit the form
        return FormRequest.from_response(response,
                                        formdata={
                                                "csrf_token": csrf_token,
                                                "name": "scrapingclub",
                                                "password": "scrapingclub",
                                                },
                                                callback = self.parse_login)
    def parse_login(self,response):
        proof = response.css("nav+div p::text").get()
        yield { "proof": proof}

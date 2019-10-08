### PURPOSE: Extract the product detail from https://scrapingclub.com/exercise/detail_ajax/ such as title, description, and price from the AJAX call. You should learn how to inspect network requests in the browser and filter them, after you figure out the URL of the ajax request, implement it in your spider.

import scrapy
from scrapy.http import FormRequest # to be able to handle AJAX data

class AjaxSpider(scrapy.Spider):

    name="ajax"
    start_urls= ["https://scrapingclub.com/exercise/detail_ajax/"]

    def parse(self,response):
        #get title, description, and price from the AJAX call
        #to see the AJAX page, inspect page, click on "Network", click on XHR, reload the page to see the AJAX request, choose it (ajaxdetail) from the list, then click on "Preview" to see what there is in AJAX.
        ## AJAX shows: desscription, img_path, price, title

        return None

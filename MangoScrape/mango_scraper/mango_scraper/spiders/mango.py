# import scrapy
# from scrapy_splash import SplashRequest
# import json

# class MangoSpider(scrapy.Spider):
#     name = 'mango'
#     start_urls = ['https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07']

#     def start_requests(self):
#         for url in self.start_urls:
#             yield SplashRequest(url, self.parse, args={'wait': 10})

#     def parse(self, response):
#         item = {}

#         # Extracting the product name from the title
#         title = response.xpath('//title/text()').get()
#         item['name'] = title.split(' - ')[0].strip()

#         # Extracting the JavaScript object containing the price and other details
#         script_content = response.xpath("//script[contains(., 'dataLayerV2Json')]/text()").get()
#         data_start = script_content.find('dataLayerV2Json = ') + len('dataLayerV2Json = ')
#         data_end = script_content.find('};', data_start) + 1
#         data_json_str = script_content[data_start:data_end]
#         data_json = json.loads(data_json_str)
        
#         product_details = data_json['ecommerce']['detail']['products'][0]

#         # Extracting the price
#         item['price'] = product_details['originalPrice']

#         # Extracting size availability
#         available_sizes = product_details['sizeAvailability']
#         unavailable_sizes = product_details['sizeNoAvailability']
#         item['size'] = {
#             'available': available_sizes.split(','),
#             'unavailable': unavailable_sizes.split(',')
#         }

#         # Request the AJAX endpoint for the color label
#         ajax_url = "https://shop.mango.com/services/garments/068/en/S/4709592307"
#         yield scrapy.Request(ajax_url, callback=self.parse_ajax, meta={'item': item})

#     def parse_ajax(self, response):
#         item = response.meta['item']
#         json_data = json.loads(response.text)
    
#         # Extract the color label
#         color_label = json_data['colors']['colors'][0]['label']
#         item['colour'] = color_label
    
#         yield item
import scrapy
from scrapy_splash import SplashRequest
import json

class MangoSpider(scrapy.Spider):
    name = 'mango'
    start_urls = ['https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 10})

    def parse(self, response):
        item = {
            'name': None,
            'price': None,
            'colour': None,
            'size': None
        }

        # Extracting the product name from the title
        title = response.xpath('//title/text()').get()
        item['name'] = title.split(' - ')[0].strip()

        # Extracting the JavaScript object containing the price and other details
        script_content = response.xpath("//script[contains(., 'dataLayerV2Json')]/text()").get()
        data_start = script_content.find('dataLayerV2Json = ') + len('dataLayerV2Json = ')
        data_end = script_content.find('};', data_start) + 1
        data_json_str = script_content[data_start:data_end]
        data_json = json.loads(data_json_str)
        
        product_details = data_json['ecommerce']['detail']['products'][0]

        # Extracting the price
        item['price'] = product_details['originalPrice']

        # Extracting size availability
        available_sizes = product_details['sizeAvailability']
        unavailable_sizes = product_details['sizeNoAvailability']
        item['size'] = {
            'available': available_sizes.split(','),
            'unavailable': unavailable_sizes.split(',')
        }

        # Request the AJAX endpoint for the color label
        ajax_url = "https://shop.mango.com/services/garments/068/en/S/4709592307"
        yield scrapy.Request(ajax_url, callback=self.parse_ajax, meta={'item': item})

    def parse_ajax(self, response):
        item = response.meta['item']
        json_data = json.loads(response.text)
    
        # Extract the color label
        color_label = json_data['colors']['colors'][0]['label']
        item['colour'] = color_label
    
        yield item

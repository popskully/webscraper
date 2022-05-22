from urllib.request import Request

import scrapy
from ..items import ShopinjascrapeItem
from scrapy.loader import ItemLoader


class ShopinjaSpiderSpider(scrapy.Spider):
    name = 'jco-cars'
    page_number = 1
    start_urls = ['https://jamaicaclassifiedonline.com/auto/cars/']

    def parse(self, response):
        text = 'Some text'
        for car in response.css('.col.l3.s12.m6'):
            items = ShopinjascrapeItem()

            product_title = car.css('.jco-card-title::text').extract()
            product_price = car.css('.ribbon span').css('::text').extract()
            # product_location = car.css('p::text').extract()
            product_imagelink = car.css('.card-image img::attr(data-src)').getall()
            urls = car.css('.card-image a::attr(href)').getall()
            #self.product_active = str(car.xpath('//*[@id="index-banner"]/div/div[4]/div[3]/div[28]/div/div[1]/div/text()').getall())
            # ad_type = car.css('.badge::text').getall()


            for url in urls:
                url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_details)

            if product_title and product_imagelink:
                if 'USD' not in product_price:
                    # if 'Sold' not in product_active:
                    items['product_title'] = product_title
                    items['urls'] = urls
                    # items['product_active'] = product_active

                    # yield product_active

    def parse_details(self, response):
        # for car in response.css('.col.l3.s12.m6'):
        # l = ItemLoader(item=ShopinjascrapeItem(), selector=response)
       # product_active = self.product_active
        #product_active.replace('\n','')

        # if 'Sold' in product_active:
        #     product_active = 'Expired'
        # if 'Sold' not in product_active:
        #     product_active = 'Active'

        product_title = str(response.css("h1#title::text").get())
        if 'For Sale' in product_title:
            ad_type = 'Sell'
        if 'For Rent' in product_title:
            ad_type = 'Rent'
        if 'Seeking' in product_title:
            ad_type = 'Buy'

        product_price = str(response.xpath('//*[@id="item-details"]/div/div[1]/div[2]/div[3]/text()').getall())
        product_imagelink = response.css(".item-images img::attr(src)").getall()
        product_author = response.xpath('//*[@id="item-details"]/div/div[1]/div[2]/div[1]/text()').get()
        product_phone = response.xpath('//*[@id="item-details"]/div/div[1]/div[2]/div[2]/a[2]/text()').get()
        product_location = str(response.xpath('//*[@id="item-details"]/div/div[1]/div[2]/div[5]/text()').getall())
        product_description = str(response.xpath('//*[@id="item-description"]/div/div[1]/div/text()').getall())
        view_count = str(response.xpath('//*[@id="item-details"]/div/div[1]/div[2]/div[7]/text()').getall())

        product_active = str(response.xpath('//*[@id="index-banner"]/div/div[2]/div/div/div[1]/span/text()').getall())
        if 'No Longer Available' in product_active:
            product_active = 'expired'
        else:
            product_active = 'active'

        # l.add_xpath('product_imagelink', '//*[@id="item-photos"]/div/div/div[2]/div[1]/a/@href')
        # ad_type = str(response.css("h1#title::text").get())

        # car specs

        year = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[2]/div/a/b').getall())
        make = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[3]/div/a/b').getall())
        model = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[4]/div/a/b').getall())
        fuel = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[5]/div/a/b').getall())
        door = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[6]/div/a/b').getall())
        transm = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[7]/div/a/b').getall())
        body = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[8]/div/a/b').getall())
        driver_side = str(response.xpath('//*[@id="item-details"]/div[1]/div[1]/ul/li[9]/div/a/b').getall())
        feature = str(response.xpath('//*[@id="item-details"]/div[1]/div[2]/div/div/div/div[1])').getall())


        # if '\n' in product_description:
        # // *[ @ id = "item-details"] / div / div[1] / div[2] / div[7] / text()
            # product_description = product_description.replace('\n','').replace('\xa0','').replace("'","").replace(":","|")





        # // *[ @ id = "item-photos"] / div / div / div[2] / div[1] / a / img
        # l.add_xpath('product_imagelink2', '//*[@id="item-photos"]/div/div/div[2]/div[2]/a/@href')
        # l.add_xpath('product_imagelink3', '//*[@id="item-photos"]/div/div/div[2]/div[3]/a/@href')
        # l.add_xpath('product_imagelink4', '//*[@id="item-photos"]/div/div/div[2]/div[4]/a/@href')
        # // *[ @ id = "item-photos"] / div / div / div[1] / div[2] / a

        yield {
        'product_title': product_title.replace('For Rent: ','').replace('For Sale: ','').replace("\n","").replace('â€','').strip(),
        'product_price': product_price.replace("USD","").replace("[","").replace("]","").replace("\n","").replace('$','').replace("'","").replace(",","").replace("\\n","").replace("\\,","").strip(),
        'product_imagelink': product_imagelink,
        'product_author': product_author,
        'product_phone': product_phone,
        'product_location': product_location.replace("[","").replace("]","").replace("\n","").replace('\xa0','').replace("'","").replace(":","|").replace("\\n","").replace("\\,","").replace(",","").strip(),
        'product_description': product_description.replace("[","").replace("]","").replace("\n","").replace('\xa0','').replace("'","").replace(":","|").replace("\\n","").replace("\\,","").replace(",","").strip(),
        'view_count': view_count.replace("[", "").replace("]", "").replace("\n", "").replace('times', '').replace("'", "").replace(",", "").replace("\\n", "").replace("\\,", "").strip(),
        'ad_type': ad_type,
        'product_active': product_active,

        # car specs
        'year' : year.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'make' : make.replace("[", "").replace("]", "").replace("<b>", "").replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'model' : model.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'fuel' : fuel.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'door' : door.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").strip(),
        'transm' : transm.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'body' : body.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").replace(" ", "").strip(),
        'driver_side' : driver_side.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").strip(),
        'feature': feature.replace("[", "").replace("]", "").replace("\n", "").replace('<b>', '').replace("'", "").replace("</b>", "").strip()
        }
        # scrapy crawl shopinja2 -t csv -o computers.csv
        next_page = 'https://jamaicaclassifiedonline.com/auto/cars/' + str(ShopinjaSpiderSpider.page_number) + ''
        if ShopinjaSpiderSpider.page_number <= 4:
            ShopinjaSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)

import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["zz.58.com"]
    start_urls = ["https://zz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]

    def parse(self, response):
        #字符串
        # content=response.text
        #二进制
        # content=response.body

        # print('====================')
        # print(content)

        span=response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print('====================')
        print(span.extract())
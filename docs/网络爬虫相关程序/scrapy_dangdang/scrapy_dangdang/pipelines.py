# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道的话 那么就必须在settings中开启管道
# ITEM_PIPELINES = {
# 管道可以有很多个  那么管道是有优先级的  优先级的范围是1到1000  值越小优先级越高
#    "scrapy_dangdang.pipelines.ScrapyDangdangPipeline": 300,
# }
class ScrapyDangdangPipeline:
    # 在爬虫文件开始之前就执行的一个方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # #以下这种模式不推荐  因为每传递过来一个对象  那么就打开一次文件 对文件操作过于频繁
        #
        #
        # # (1)write方法必须要写一个字符串  而不能是其他对象
        # # (2)w模式 会每一个对象都打开一次  覆盖之前的内容
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))

        self.fp.write(str(item))

        return item

    # 在爬虫文件执行玩之后  执行的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request


# 多条管道同时开启
# (1)定义管道类
# (2)在settings中开启管道
# "scrapy_dangdang.pipelines.DangdangPipeline": 301
class DangdangPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item

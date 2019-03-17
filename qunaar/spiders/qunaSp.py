# -*-coding:utf-8-*-
import scrapy
from qunaar.items import QunaarItem
import json


class TcopspSpider(scrapy.Spider):
    name = 'qunarPy'
    allowed_domains = ['http://travel.qunar.com']
    offset = 1
    url = "http://travel.qunar.com/p-oi712636-bayiqiyijinianguan-0-"
    # 这个是我们最想要的链接
    # http://travel.qunar.com/p-oi719780-tengwangge-1-99?rank=0#lydp
    # start_urls = [url+str(offset)]
    start_urls = [url + str(offset),
                  # "http://travel.qunar.com/p-oi703469-houtianshamo-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi703469-houtianshamo-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi703420-poyanghu-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi9017377-nanchangzhixingmotian-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi712942-qiushuiguangchang-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi9502951-nanchangwandazhutileyuan-1-2?rank=0#lydp",
                  # "http://travel.qunar.com/p-oi9208108-nanchangwandahaiyangle-1-2?rank=0#lydp",
                  ]

    def parse(self, response):
        # with open("123.html", "w") as f:
        #    f.write(response.body)
        # 把json格式的数据转换为python格式，data段是列表
        # data = response.xpath('//div[@class="e_comment_main"] | //div[@class="e_comment_usr"]')
        data = response.xpath('//li[@class="e_comment_item clrfix"]')
        # data = json.loads(response.text)["data"]
        # print data

        for each in data:
            item = QunaarItem()
            # 获取评论
            item["cat_user_comment"] = each.xpath(
                './div[@class="e_comment_main"]/div[@class="e_comment_main_inner"]/div[@class="e_comment_content"]/p/text()').extract()
            # 获取评论时间
            item["cat_comment_time"] = each.xpath(
                './div[@class="e_comment_main"]/div[@class="e_comment_main_inner"]/div[@class="e_comment_add_info"]/ul/li[1]/text()').extract()
            # 获取评论人姓名
            item["cat_user_name"] = each.xpath(
                './div[@class="e_comment_usr"]/div[@class="e_comment_usr_name"]/a/text()').extract()
            # 获取评论者发图片数(作业要求通过算法给景点评分推荐,个人认为游客发照片数量是一个重要特征)
            item["cat_user_pic"] = each.xpath(
                './div[@class="e_comment_main"]/div[@class="e_comment_main_inner"]/div[@class="e_comment_imgs_box"]/div[@class="e_comment_imgs clrfix"]/span[@class="img_count"]/a/text()').extract()

            # cat_jd_poi = scrapy.Field()
            yield item

        # 被限制了,慎用
        if self.offset < 50:
            self.offset += 1
            # print self.offset
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)

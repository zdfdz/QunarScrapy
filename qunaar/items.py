# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunaarItem(scrapy.Item):
    # 用户id
    cat_user_id = scrapy.Field()
    # 用户名字
    cat_user_name = scrapy.Field()
    # 用户评分
    cat_score = scrapy.Field()
    # 用户评论
    cat_user_comment = scrapy.Field()
    # 用户评论时间
    cat_comment_time = scrapy.Field()
    # 用户发图数
    cat_user_pic = scrapy.Field()

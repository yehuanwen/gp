# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 产品
class ProductItem(scrapy.Item):
    updated_at = scrapy.Field()  # 最后一次更新时间
    gp_icon = scrapy.Field()   # 图标
    gp_name = scrapy.Field()  # GP名称
    gp_tag = scrapy.Field()  # GP标签
    gp_url = scrapy.Field()  # GP链接
    gp_intro = scrapy.Field()  # GP介绍
    gp_developer = scrapy.Field()  # GP开发者
    gp_rating = scrapy.Field()  # GP评级
    gp_package = scrapy.Field()  # GP包名
    gp_picture = scrapy.Field()  # GP图片，英文逗号分割
    gp_version = scrapy.Field()  # GP最新版本
    gp_update = scrapy.Field()  # GP更新时间
    gp_news = scrapy.Field()  # GP更新内容
    gp_video_image = scrapy.Field()  # GP视频图片
    gp_video_url = scrapy.Field()  # GP视频链接
    gp_review = scrapy.Field()  # GP视频链接
    gp_downloads = scrapy.Field()  # GP下载人数


# 评论
class GPReviewItem(scrapy.Item):
    avatar_url = scrapy.Field()  # 头像链接
    user_name = scrapy.Field()  # 用户名称
    review_text = scrapy.Field()  # 评论
    rating_star = scrapy.Field()  # 评星个数，1~5

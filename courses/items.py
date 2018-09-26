# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class CoursesDetails(Item):
    course_title = Field()
    course_download_link = Field()
    course_tags = Field()
    course_link = Field()
    course_img = Field()
    course_views = Field()
    course_desc = Field()
    course_published = Field()
    course_updated = Field()
    course_size = Field()
    course_category = Field()
    related_posts = Field()
    udemy_link = Field()



# -*- coding: utf-8 -*-
import scrapy
from courses.items import CoursesDetails
from scrapy.loader import ItemLoader

class FreetutorialsSpider(scrapy.Spider):
    name = 'freetutorials'
    # allowed_domains = ['www.freetutorials.us']
    start_urls = ['http://www.freetutorials.us/']

    def parse_page(self, response):
        course_pg_links = response.xpath("//*[@class = 'entry-title post-title']")
        k = 1
        for i in course_pg_links:
            course_link = i.xpath("./a/@href").extract_first()
            yield scrapy.Request(course_link, callback=self.parse_course)
            print(course_link)
            # if k == 2: break
            # k = 2

    def parse_course(self, response):

        l = ItemLoader(item=CoursesDetails(), response = response)

        course_title = response.xpath("//*[@class = 'entry-header']/h1/text()").extract_first()
        course_views = response.xpath("//*[@class = 'post-views-count']/text()").extract_first()
        try :
            course_img = response.xpath("//*[contains(@src, 'https://udemy-images.udemy.com/')  ]")[0].xpath("./@src").extract_first()
            course_desc = response.xpath("//*[contains(@src , 'https://udemy-images')]//following::h1/text()").extract_first()
        except:
            course_img = response.xpath("//*[@class = 'wp-image-7501 aligncenter']/@src").extract_first()
            course_desc = response.xpath("//*[@class = 'wp-image-7501 aligncenter']//following::h1/text()").extract_first()

        course_tags = response.xpath("//*[@class = 'thetags']/a/text()").extract()

        course_published =  response.xpath("//*[@class = 'entry-date published']/@datetime").extract_first()      
        course_updated =response.xpath("//*[@class = 'updated']/@datetime").extract_first()
        # if response.xpath("//*[time/@datetime]").extract() == 2:
        #     course_published = response.xpath("//*[time/@datetime]/@datetime")[0].extract()
        #     course_updated = response.xpath("//*[time/@datetime]")[1].extract_first()
        # elif len(response.xpath("//*[@datetime]/@datetime")) == 1:
        #     course_published = response.xpath("//*[@datetime]/@datetime")[0].extract_first()
        #     if response.xpath("//*[contains(text(), 'Last updated')]/child::node()").extract_first():
        #         course_updated = response.xpath("//*[contains(text(), 'Last updated')]/child::node()").extract_first()
        #     elif response.xpath("//*[contains(text(), 'Last Updated')]/child::node()").extract_first():
        #         course_updated = response.xpath("//*[contains(text(), 'Last Updated')]/child::node()").extract_first()
        #     if course_updated:
        #         course_updated = course_updated.lower().replace("last updated", "").upper()
        #     else:
        #         course_updated = "NOT FOUND"

        course_size = response.xpath("//*[contains(text(), 'Size')]/child::node()").extract_first()
        # course_size = course_size.lower().replace("size: ", "").upper()
        # .replace("\xa","").replace("gb", "GB")
        course_link = response.url
        course_category = response.xpath("//*[@rel = 'category tag']/text()").extract_first()

        if response.xpath("//*[contains(@href, '.torrent')]/@href").extract_first():
            course_download_link = response.xpath("//*[contains(@href, '.torrent')]/@href").extract_first()
        elif response.xpath("//*[contains(@href, 'magnet')]/@href").extract_first():
            course_download_link = response.xpath("//*[contains(@href, 'magnet')]/@href").extract_first()
        elif response.xpath("//*[contains(@href, 'drive.google.com')]/@href").extract_first():
            course_download_link = response.xpath("//*[contains(@href, 'drive.google.com')]/@href").extract_first()
        else:
            course_download_link = "NOT PROVIDED"


        if response.xpath("//*[@class = 'related-posts']"):
            titles = response.xpath("//*[@class='related-posts']/ul/li//*[@class = 'post-title']//*[@title]/text()").extract()
            links = response.xpath("//*[@class='related-posts']/ul/li//*[@class = 'post-title']//*[@title]/@href").extract()
            related_posts = [ [i,j] for (i,j) in zip(titles, links) ]
        else:
            related_posts = "NA"

        if response.xpath("//*[@class = 'wpss_copy']"):
            udemy_link = response.xpath("//*[@class = 'wpss_copy']/text()").extract_first()
            try:
                udemy_link = (udemy_link[:-1] if udemy_link[-1] == '.' else udemy_link)
            except:
                udemy_link = "NOT FOUND"
        else:
            udemy_link = "Not Found"

        l.add_value('course_title', course_title)
        l.add_value('course_views', course_views)
        l.add_value('course_img', course_img)
        l.add_value('course_desc', course_desc)
        l.add_value('course_tags', course_tags)
        l.add_value('course_link', course_link)
        l.add_value('course_published', course_published)
        l.add_value('course_updated', course_updated)
        l.add_value('course_size', course_size)
        l.add_value('course_category', course_category)
        l.add_value('course_download_link', course_download_link)
        l.add_value('related_posts', related_posts)
        l.add_value('udemy_link', udemy_link)

        yield l.load_item()
        # yield {
            # "course_title" : course_title,
            # "course_views" : course_views,
            # "course_img" : course_img,
            # "course_desc" : course_desc,
            # "course_tags" : course_tags,
            # "course_published" : course_published,
            # "course_updated" : course_updated,
            # "course_size" : course_size,
            # "course_link" : course_link,
            # "course_category" : course_category,
            # "course_download_link" : course_download_link,
            # "related_posts" : related_posts,
            # "udemy_link" : udemy_link
        # }
        



    def parse(self, response):
        url = "https://www.freetutorials.us/page/"
        for i in range(1, 85):
            page_url = url + str(i)
            yield scrapy.Request(page_url, callback=self.parse_page)
            break

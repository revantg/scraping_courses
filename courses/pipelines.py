# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import dateutil.parser
import sys
# import libtorrent
from urllib.parse import urlencode

# def getDateTimeFromISO8601String(s):
#     d = dateutil.parser.parse(s)
#     return d

class CoursesPipeline(object):

    # def torrent2magnet(self, torrent):

    #     session = libtorrent.session()  # noqa
    #     info = libtorrent.torrent_info(sys.argv[1])

    #     params = [
    #         ("dn", info.name()),
    #     ]
    #     params.extend(("tr", tr.url) for tr in info.trackers())

    #     magnet = "magnet:?xt=urn:btih:{}&{}".format(
    #         info.info_hash(),
    #         urlencode(params),
    #     )
    #     return magnet

    def process_time(self, isostring):
        a = isostring
        iso_string = isostring
        datetime_obj = dateutil.parser.parse(a)
        formatted_date = datetime_obj.strftime("%d %B %Y")
        formatted_time = datetime_obj.strftime("%H:%M:%S")
        formatted_date_time = formatted_date + ' ' + formatted_time
        a_dict = {
            'datetime-object': datetime_obj,
            'formatted_date': formatted_date,
            'formatted_time': formatted_time,
            'formatted_date_time': formatted_date_time,
            'iso_string' : iso_string,
        }
        return a_dict

    def process_item(self, item, spider):
        if item["course_title"]         : item  ['course_title'] = item['course_title'][0]
        if item["course_views"]         : item['course_views'] = item['course_views'][0]
        if item["course_img"]           : item['course_img'] = item['course_img'][0]
        if item["course_desc"]          : item['course_desc'] = item['course_desc'][0]
        if item["course_tags"]          : item['course_tags'] = item['course_tags'][0]
        if item["course_link"]          : item['course_link'] = item['course_link'][0]
        if item["course_category"]      : item['course_category'] = item['course_category'][0]
        if item["course_download_link"] : item['course_download_link'] = item['course_download_link'][0]
        if item["udemy_link"]           : item['udemy_link'] = item['udemy_link'][0]
        # if item["related_posts"]        : item['related_posts'] = item['related_posts'][0]

        if item["course_size"] : 
            item['course_size'] = item['course_size'][0]    
            item['course_size'] = item['course_size'].upper().replace('SIZE: ', '').replace('G', 'GB').replace('M', 'MB')

        if item["course_published"]: 
            item['course_published'] = item['course_published'][0]
            item['course_published'] = self.process_time(item['course_published'])
       
        if item["course_updated"] : 
            item['course_updated'] = item['course_updated'][0]
            item['course_updated'] = self.process_time(item['course_updated'])

        return item


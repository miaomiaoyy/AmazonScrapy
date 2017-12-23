# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class PracticePipeline(object):
    def process_item(self, item, spider):
        return item


class HupuPipeline(object):

    def process_item(self, item, spider):

        host = "localhost"
        port = 3306
        user = "root"
        password = "yy19890224"
        charset = "utf8"
        db = "Hupu"


        connect = pymysql.connect(host=host, port=port, user=user, passwd=password, charset=charset, db=db)
        cursor = connect.cursor()
        #cursor.execute("insert post(title) values(\"{}\");".format(item["title"]))
        connect.commit()
        cursor.close()
        connect.close()
        return item

class ApplePipeline(object):

    def process_item(self, item, spider):

        host = "localhost"
        port = 3306
        user = "root"
        password = "yy19890224"
        charset = "utf8"
        db = "apple"

        connect = pymysql.connect(host=host, port=port, user=user, passwd=password, charset=charset, db=db)
        cursor = connect.cursor()
        cursor.callproc("insert_apple", [item["news"]])
        #cursor.execute("insert post(title) values(\"{}\");".format(item["title"]))
        connect.commit()
        cursor.close()
        connect.close()
        return item
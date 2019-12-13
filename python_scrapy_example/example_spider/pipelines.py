# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ExampleSpiderPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        print(item['serial_number'])
        # pic_name = " ".join([item["title"], item["name"]]) + ".jpg"
        # img_data = requests.get(item["img_src"])
        # with open(pic_name, "wb") as f:
        #     f.write(img_data.content)
        return item

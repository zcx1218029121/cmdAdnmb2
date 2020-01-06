# coding=utf-8
from src.template.ListTemplate import *


class ListPagerTemplate(Template, ABC):

    def generate_content(self, info):
        r = ""
        index = 0
        lt = ListTemplate()
        for item in info:
            if isinstance(item, tuple):
                # userid,img,ext,content
                item = {"index": item[0], "userid": item[1], "img": item[2], "ext": item[3], "content": item[4]}
            else:
                item["index"] = index
            r = r + lt.generate_all(item)
            index = index + 1
        return r

    def generate_header(self, info):
        return ""

    def generate_divider(self, info):
        return ""

    def generate_footer(self, info):
        return ""

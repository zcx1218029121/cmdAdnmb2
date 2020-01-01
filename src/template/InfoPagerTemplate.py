# coding=utf-8
from abc import ABC

from src.template.ListTemplate import ListTemplate
from src.template.Template import Template


class InfoPagerTemplate(Template, ABC):
    def generate_content(self, info):
        r = ""
        index = 0
        lt = ListTemplate()
        if len(info["replys"]) == 1:
            return "没有数据了"
        for item in info["replys"]:
            item["index"] = index
            if info["userid"] == item["userid"]:
                item["pou"] = True
            r = r + lt.generate_all(item)
            index = index + 1
        return r

    def generate_divider(self, info):
        return "------ "

    def generate_footer(self, info):
        return ""

    def generate_header(self, info):
        return """%s \n 时间:%s \n %s: \n %s
                """ % (self.generate_divider(info), info['now'], info["userid"], info["content"])

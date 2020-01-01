from src.template.ListTemplate import *


class ListPagerTemplate(Template, ABC):

    def generate_content(self, info):
        r = ""
        index = 0
        lt = ListTemplate()
        for item in info:
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

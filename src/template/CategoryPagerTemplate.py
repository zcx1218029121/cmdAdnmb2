from abc import ABC

from src.template.Template import Template


class CategoryPagerTemplate(Template, ABC):
    def generate_content(self, info):
        r = ""
        index = 0
        for item in info["forum"]:
            r = r + "【" + str(index) + "】:  " + item["name"] + "\n" + "-----------\n"
            index = index + 1
        return r

    def generate_header(self, info):
        return ""

    def generate_footer(self, info):
        return ""

    def generate_divider(self, info):
        return ""

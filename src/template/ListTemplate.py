from abc import ABC

from src.singleton import singleton
from src.template.Template import Template


@singleton()
class ListTemplate(Template, ABC):
    def generate_footer(self, info):
        return self.generate_divider(info)

    def generate_header(self, info):
        print(info)
        return self.generate_divider(info) + \
               self.generate_index(info["index"]) + info["userid"] + ":" + \
               self.generate_divider(info)

    def generate_divider(self, info):
        return "\n----\n"

    def generate_content(self, info):
        return info["content"] + "\n"

    def generate_index(self, index):
        return "【"+str(index)+"】"

from abc import ABC

from src.singleton import singleton
from src.template.Template import Template


@singleton()
class ListTemplate(Template, ABC):
    def generate_footer(self, info):
        return self.generate_divider(info)

    def generate_header(self, info):
        return self.generate_divider(info) + \
               info["userid"] + ":" + \
               self.generate_divider(info)

    def generate_divider(self, info):
        return "\n----\n"

    def generate_content(self, info):
        return info["content"] + "\n"

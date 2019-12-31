from abc import ABC

from src.singleton import singleton
from src.template.Template import Template

@singleton()
class ListPagerTemplate(Template, ABC):
    def generate_content(self, info):
        pass

    def generate_header(self, info):
        return ""

    def generate_divider(self, info):
        pass

    def generate_footer(self, info):
        return ""

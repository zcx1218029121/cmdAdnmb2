# coding=utf-8
from abc import ABC

from src.template.Template import Template


class ToastTemplate(Template, ABC):
    """
    吐司的模板
    """

    def generate_divider(self, info):
        pass

    def generate_header(self, info):
        return "---------------- info ---------------------\n"

    def generate_footer(self, info):
        return "--------------------------------------------\n"

    def generate_content(self, info):
        return info + "\n"

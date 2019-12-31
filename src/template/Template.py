from abc import abstractmethod
from abc import abstractmethod, ABCMeta


class Template(metaclass=ABCMeta):
    """
    应用模板
    """

    @abstractmethod
    def generate_header(self, info):
        pass

    @abstractmethod
    def generate_content(self, info):
        pass

    @abstractmethod
    def generate_footer(self, info):
        pass

    @abstractmethod
    def generate_divider(self, info):
        pass

    def generate_all(self, info):
        return self.generate_header(info) + self.generate_content(info) + self.generate_footer(info)

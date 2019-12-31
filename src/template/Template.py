from abc import abstractmethod


class Template:
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

    @abstractmethod
    def generate_index(self, index):
        pass

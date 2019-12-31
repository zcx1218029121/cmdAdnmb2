from abc import ABC

from src.pager.View import View


class Item(View, ABC):
    def init_data(self):
        """
        初始化数据
        :return:
        """
        pass

    def on_destroy(self):
        self.data = None

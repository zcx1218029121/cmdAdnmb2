from src.template.Template import *
from src.out.OutPutUtil import *
from abc import ABCMeta, abstractmethod


class Pager:
    #  请求数据
    data = None
    # 模板
    template = None

    @abstractmethod
    def init_data(self):
        """
        初始化数据
        :return:
        """
        pass

        # 显示回调

    @abstractmethod
    def on_show(self):
        pass

        # 销毁回调

    @abstractmethod
    def on_destroy(self):
        self.data = None

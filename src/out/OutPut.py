from abc import ABCMeta, abstractmethod

"""
 输出 抽象类
"""


class OutPut(metaclass=ABCMeta):
    @abstractmethod
    def out(self, text):
        pass

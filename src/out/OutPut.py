from abc import ABCMeta, abstractmethod

"""
 输出 抽象类
"""


class OutPut:
    @abstractmethod
    def out(self, text):
        pass

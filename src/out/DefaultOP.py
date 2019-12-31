from abc import ABC
from src.out.OutPut import *

"""
 默认输出
"""


class DefaultOP(OutPut, ABC):
    def out(self, text):
        print(text)

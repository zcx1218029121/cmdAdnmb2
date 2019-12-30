from src.out.OutPut import *
from src.out.DefaultOP import *

"""
输出 工具
"""


class OutPutUtil:
    def __init__(self, out_put):
        self.out_put = out_put

    def log(self, text):
        self.out_put.out(text)

    def logf(self, text):
        self.out_put.out(text+"\n")


singleton = OutPutUtil(DefaultOP())

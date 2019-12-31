from abc import ABC
from src.out.OutPut import *

"""
 默认输出
"""

import threading


class DefaultOP(OutPut, ABC):
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(DefaultOP, "_instance"):
            with DefaultOP._instance_lock:
                DefaultOP._instance = DefaultOP(*args, **kwargs)
        return DefaultOP._instance

    def out(self, text):
        print(text)

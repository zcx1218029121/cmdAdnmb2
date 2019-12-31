from src.pager.View import *
from abc import ABC
import json
from src.net.Api import *


class Pager(View, ABC):

    def init_data(self):
        """
        初始化数据
        :return:
        """
        return json.loads(get_plate_info(4, 1))

    def on_destroy(self):
        self.data = None

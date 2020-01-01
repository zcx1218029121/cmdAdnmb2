from src.pager.View import *
from abc import ABC
import json
from src.net.Api import *
import queue


class Pager(View, ABC):
    cache_size = 10
    # 默认 请求页数 1
    pager = 1
    # 缓存页面 默认为 3
    pager_queue = queue.Queue(cache_size)

    is_loading = False

    def __init__(self, template, string_id=4):
        super().__init__(template)
        self.id = string_id

    def on_destroy(self):
        self.data = None

    def next_pager(self):
        self.pager = self.pager + 1
        # 缓存上一页的数据
        if self.pager_queue.full():
            # 缓存页数据出队
            self.pager_queue.get()
        self.pager_queue.put(self.data)

        self.data = self.get_data()
        # 重新打印当前内
        self.print_pager()

    def up_pager(self):
        # 缓存队列
        self.pager = self.pager - 1
        # 如果前一页缓存 不为空
        if not self.pager_queue.empty():
            self.data = self.pager_queue.get()
        else:
            if self.pager < 2:
                self.pager = 1
            self.data = self.get_data()
        self.print_pager()

    def get_data(self):
        self.show_loading()
        return json.loads(get_plate_info(self.id, self.pager))

    def show_loading(self):
        self.print_text("加载中...")
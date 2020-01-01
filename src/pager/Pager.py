from src import Route
from src.pager.View import *
from abc import ABC
import json
from src.net.Api import *
import queue
from src.config.Config import prefix_re, pg_down, pg_up


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


class Pager(View, ABC):
    cache_size = 10
    # 默认 请求页数 1
    pager = 1
    # 缓存页面 默认为 3
    pager_queue = queue.Queue(cache_size)

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

    def up_pager(self):
        # 缓存队列
        self.pager = self.pager - 1
        # 如果前一页有缓存 不为空
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

    def handler_input(self, ip):
        """

        :param ip: 输入
        :return: 是否传递输入给 循环的下一页
        """
        if ip == pg_down:
            self.next_pager()
            return True
        if ip == pg_up:
            self.up_pager()
            return True
        if ip.startswith(prefix_re):
            self.do_reply(ip[len(prefix_re):])
            return True
        if is_number(ip):
            return self.index_type(ip)
        # 不消耗输入
        return False

    def do_reply(self, text):
        Route.instance.show_toast(post_data(self.id, text))

    def index_type(self, ip):
        Route.instance.push({"name": "info", "parm": self.data[int(ip)]["id"]})
        return True

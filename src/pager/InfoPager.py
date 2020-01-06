# coding=utf-8
import json
from src.dao.DbHelper import *
from src import Route
from src.net.Api import *
from src.pager.Pager import Pager


class InfoPager(Pager):
    def get_data(self):
        self.show_loading()
        return json.loads(get_string_info_url(self.id, self.pager))

    def do_reply(self, text):
        Route.instance.show_toast(post_data(self.id, text))

    def index_type(self, ip):
        Route.instance.show_toast("串引用还在开发中...")
        pass

    def on_creat(self):
        self.id = Route.instance.cur_intent["parm"]

    def handler_input(self, ip):
        super().handler_input(ip)
        if ip == "cs":
            add_string(userid=self.data["userid"], img=self.data["img"], ext=self.data["ext"], content=self.data
            ["content"],sid=self.data["id"])

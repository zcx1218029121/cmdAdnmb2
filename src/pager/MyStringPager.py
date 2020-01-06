from src import Route
from src.pager.Pager import Pager
from src.dao.DbHelper import *


class MyStringPager(Pager):
    def get_data(self):
        return get_strings()

    def on_creat(self):
        pass

    def do_reply(self, text):
        pass

    def index_type(self, ip):
        Route.instance.push({"name": "info", "parm": self.data[int(ip) - 1][5]})
        return True

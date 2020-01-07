import json

from src.dao import Route
from src.pager.Pager import Pager, get_category


class CategoryPager(Pager):
    def get_data(self):
        self.show_loading()
        return json.loads(get_category())

    def index_type(self, ip):
        Route.instance.push({"name": "main", "parm": self.data["forum"][int(ip)]["id"]})

    def do_reply(self, text):
        pass

    def on_creat(self):
        pass
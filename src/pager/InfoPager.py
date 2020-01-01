import json

from src import Route
from src.net.Api import *
from src.pager.Pager import Pager


class InfoPager(Pager):
    def get_data(self):
        self.show_loading()
        self.id = Route.instance.cur_intent["parm"]
        return json.loads(get_string_info_url(self.id, self.pager))

    def index_type(self, ip):
        Route.instance.show_toast("串引用还在开发中...")
        return True

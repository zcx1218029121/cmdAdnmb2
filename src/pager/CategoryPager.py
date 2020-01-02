from src import Route
from src.pager.Pager import Pager, get_category
import json

from src.template.CategoryPagerTemplate import CategoryPagerTemplate


class CategoryPager(Pager):
    def get_data(self):
        self.show_loading()
        return json.loads(get_category())

    def index_type(self, ip):
        Route.instance.push({"name": "main", "parm": self.data["forum"][int(ip)]["id"]})

    def do_reply(self, text):
        pass

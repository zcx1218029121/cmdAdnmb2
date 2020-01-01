import json

from src import Route
from src.config.Config import prefix_re
from src.net.Api import *
from src.pager.Pager import Pager


class InfoPager(Pager):
    def get_data(self):
        self.show_loading()
        self.id = Route.instance.cur_intent["parm"]
        return json.loads(get_string_info_url(self.id, self.pager))

    def handler_input(self, ip):
        if ip.startswith(prefix_re):
            self.do_reply(ip[len(prefix_re):])

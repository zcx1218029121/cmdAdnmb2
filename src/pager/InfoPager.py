import json

from src.net.Api import *
from src.pager.Pager import Pager


class InfoPager(Pager):
    def get_data(self):
        self.show_loading()
        return json.loads(get_string_info_url(self.id, self.pager))

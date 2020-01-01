from src.pager.InfoPager import InfoPager
from src.pager.Pager import Pager
from src.template.InfoPagerTemplate import InfoPagerTemplate
from src.template.ListPagerTemplate import ListPagerTemplate


class Route:
    # 路由列表
    route_list = {"info": {"pager": InfoPager, "template": InfoPagerTemplate},
                  "main": {"pager": Pager, "template": ListPagerTemplate}
                  }
    cur_intent = None
    app = None

    def push(self, intent):
        if not self.app:
            raise RuntimeError("app 未绑定")
        if "name" not in intent:
            raise RuntimeError("错误的意图")
        self.cur_intent = intent
        m_intent = self.route_list.get(intent["name"])
        pager = m_intent["pager"](m_intent["template"]())
        self.app.add_pager(pager)

    def bind_app(self, app):
        self.app = app


instance = Route()

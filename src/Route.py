# coding=utf-8
from src.pager.InfoPager import InfoPager
from src.pager.Pager import Pager
from src.pager.Toast import Toast
from src.template.InfoPagerTemplate import InfoPagerTemplate
from src.template.ListPagerTemplate import ListPagerTemplate
from src.template.ToastTemplate import ToastTemplate


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

    def show_toast(self, text):
        """
        显示 提示 Toast  重写了onshow 在onshow 调用后立即出栈
        :param text:
        :return:
        """
        if not self.app:
            raise RuntimeError("app 未绑定")

        self.app.add_pager(Toast(template=ToastTemplate(), app=self.app, text=text))


instance = Route()

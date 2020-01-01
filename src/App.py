# coding=utf-8
import sys
sys.path.append('/home/zcx/IdeaProjects/cmdAdnmb2')
from src import Route
from src.Stack import Stack
from src.config.Config import welcome, bye, pg_down, pg_up, back
from src.pager.InfoPager import InfoPager
from src.pager.Pager import *
from src.template.InfoPagerTemplate import InfoPagerTemplate
from src.template.ListPagerTemplate import *


class App:
    # 页面栈
    pager_task = Stack()
    run = True

    def on_creat(self):
        """
        应用启动
        :return:
        """
        OutPutUtil.singleton.log(welcome)
        # 绑定路由
        Route.instance.bind_app(self)

    def add_pager(self, pager):
        """
        添加页面方法
        :return:
        """
        # 压入元素
        self.pager_task.push(pager)

    def show_pager(self):
        """
        打印当前页码
        :return:
        """
        self.pager_task.peek().on_show()

    def on_exit(self):
        self.pager_task.clear()
        OutPutUtil.singleton.log(bye)
        # 结束循环
        self.run = False

    def back(self):
        if self.pager_task.size() > 1:
            # 回调 销毁方法
            self.pager_task.peek().on_destroy()
            self.pager_task.pop()
        else:
            self.on_exit()

    def start(self):
        self.on_creat()
        # 默认加载时间线页面
        self.add_pager(Pager(ListPagerTemplate(), string_id=4))
        # main loop
        while self.run:
            self.show_pager()
            ip = input()
            if self.pager_task.peek().handler_input(ip):
                continue
            if ip == back:
                self.back()
            if ip == "exit":
                self.on_exit()


if __name__ == '__main__':
    App().start()

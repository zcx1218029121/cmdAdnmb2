from src.Stack import Stack
from src.pager.InfoPager import InfoPager
from src.pager.Pager import *
from src.template.InfoPagerTemplate import InfoPagerTemplate
from src.template.ListPagerTemplate import *


class App:
    # 页面栈
    pager_task = Stack()

    def on_creat(self):
        """
        应用启动
        :return:
        """
        OutPutUtil.singleton.log(welcome)

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
        OutPutUtil.singleton.log(ConfigReader.get_config().bye)

    def back(self):
        if self.pager_task.size() >= 1:
            self.pager_task.pop()

    def start(self):
        self.on_creat()
        # 默认加载时间线页面
        self.add_pager(Pager(ListPagerTemplate(), string_id=4))
        # main loop
        while True:
            self.show_pager()
            ip = input()
            if ip == pg_down:
                self.pager_task.peek().next_pager()
            elif ip == pg_up:
                self.pager_task.peek().up_pager()
            elif ip == back:
                self.back()
            else:
                self.add_pager(InfoPager(InfoPagerTemplate(), string_id=self.pager_task.peek().data[int(ip)]["id"]))


if __name__ == '__main__':
    App().start()

from src.Stack import Stack
from src.config.ConfigReader import *
from src.pager.Pager import *
from src.template.ListPagerTemplate import *


@singleton()
class App:
    # 页面栈
    pager_task = Stack()

    def on_creat(self):
        """
        应用启动
        :return:
        """
        OutPutUtil.singleton.log(ConfigReader.get_config().welcome)

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

    def start(self):
        self.on_creat()
        # main loop
        while True:
            ip = input()
            self.add_pager(Pager(ListPagerTemplate()))
            self.show_pager()


if __name__ == '__main__':
    App().start()

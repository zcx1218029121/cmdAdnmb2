# coding=utf-8
import sys

sys.path.append('F:\cmdAdnmb2')
import os
from src.dao.DbHelper import *
from src.pager.CategoryPager import CategoryPager
from src.template.CategoryPagerTemplate import CategoryPagerTemplate
from src.pager.Pager import *


class App:
    # 页面栈
    pager_task = Stack()
    run = True

    def on_creat(self):
        """
        应用启动
        :return:
        """

        OutPutUtil.singleton.log(Config.instance.welcome)

        # 绑定路由
        self.read_config()
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
        OutPutUtil.singleton.log(Config.instance.bye)
        # 结束循环
        self.run = False

    def back(self):
        if self.pager_task.size() > 1:
            # 回调 销毁方法
            self.pager_task.peek().on_destroy()
            self.pager_task.pop()
        else:
            self.on_exit()

    def go_to(self, string_no):
        Route.instance.push({"name": "info", "parm": string_no[3:]})

    def start(self):
        self.on_creat()
        # 默认加载时间线页面
        self.add_pager(CategoryPager(CategoryPagerTemplate()))
        # main loop
        while self.run:
            self.show_pager()
            ip = input()
            if ip == "myString":
                Route.instance.push({"name": "myString"})
            if self.pager_task.peek().handler_input(ip):
                continue
            if ip == Config.instance.back:
                self.back()
            if ip == "exit":
                self.on_exit()
            if ip.startswith("go:"):
                self.go_to(ip)

    def read_config(self):
        # if not os.path.exists("./config.json"):
        #     userhash = input("userhash:")
        #     memberUserspapapa = input("memberUserspapapa:")
        #     PHPSESSID = input("PHPSESSID:")
        #     cookie_json = {"userhash": userhash, "memberUserspapapa": memberUserspapapa, "PHPSESSID": PHPSESSID}
        #     with open("./config.json", "w") as f:
        #         f.write(json.dumps(cookie_json))
        if os.path.exists("./config.json"):
            with open("./config.json", 'r') as f:
                config_json = json.loads(f.read())
                Config.instance.cookies = config_json["cookies"]
                OutPutUtil.singleton.log("已经登录")
        else:
            OutPutUtil.singleton.log("未登录")


if __name__ == '__main__':
    if not os.path.exists("./collect.db"):
        creat_table()
    App().start()

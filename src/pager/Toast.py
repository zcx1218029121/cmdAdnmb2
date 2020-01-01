from abc import ABC

from src.pager.View import View


# 弹出提示view 显示一次后立即退出页面栈
class Toast(View, ABC):

    def __init__(self, template, app, text):
        super().__init__(template)
        self.app = app
        self.data = text

    def get_data(self):
        pass

    def on_destroy(self):
        self.template = None
        self.data = None
        self.app = None

    def on_show(self):
        super().on_show()
        # show 调用后吐司 立刻弹出页面
        self.app.pager_task.pop()

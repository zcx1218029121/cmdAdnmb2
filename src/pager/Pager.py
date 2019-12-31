from abc import abstractmethod

from src.out import OutPutUtil


class Pager:
    #  请求的数据
    data = None
    # 模板
    template = None

    @abstractmethod
    def init_data(self):
        """
        初始化数据
        :return:
        """
        pass

        # 显示回调

    def on_show(self):
        if self.data:
            self.init_data()
        self.on_show()

        # 销毁回调

    @abstractmethod
    def on_destroy(self):
        self.data = None

    @abstractmethod
    def bind_template(self, template):
        """
        绑定模板
        :param template:
        :return:
        """
        self.template = template

    def print_pager(self):
        """
        打印页面
        :return:
        """
        if not self.template:
            raise RuntimeError('template is  Unbound')

        self.print_header()
        self.print_content()
        self.print_footer()

    def print_header(self):
        """
        打印头
        :return:
        """
        OutPutUtil.singleton.log(self.template.header)

    def print_footer(self):
        """
        打印脚
        :return:
        """
        OutPutUtil.singleton.log(self.template.footer)

    def print_content(self):
        OutPutUtil.singleton.log(self.template.content)

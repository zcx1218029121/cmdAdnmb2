from abc import abstractmethod, ABCMeta

from src.out import OutPutUtil


class View(metaclass=ABCMeta):
    #  请求的数据
    data = None
    # 模板
    template = None

    def __init__(self, template):
        self.template = template

    @abstractmethod
    def init_data(self):
        """
        初始化数据
        :return:
        """
        pass

    def on_show(self):
        """
        # 显示回调
        :return:
        """
        if not self.data:
            self.print_pager(self.init_data())
        else:
            self.print_pager(self.init_data())

    def refresh(self):
        """
        # 强制刷新
        :return:
        """
        self.init_data()
        self.print_pager(self.init_data())

    # 销毁回调
    @abstractmethod
    def on_destroy(self):
        self.data = None

    def bind_template(self, template):
        """
        绑定模板
        :param template:
        :return:
        """
        self.template = template

    def print_pager(self,data):
        """
        打印页面
        :return:
        """
        if not self.template:
            raise RuntimeError('template is  Unbound')
        print(self.template.generate_content(data))

    def print_header(self):
        """
        打印头
        :return:
        """
        OutPutUtil.singleton.log(self.template.generate_header(self.data))

    def print_footer(self):
        """
        打印脚
        :return:
        """
        OutPutUtil.singleton.log(self.template.generate_footer(self.data))

    def print_content(self):
        OutPutUtil.singleton.log(self.template.generate_content(self.data))

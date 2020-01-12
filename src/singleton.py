from functools import wraps
import threading


def singleton():
    """
    单例模式装饰器
    :return:
    """
    # 闭包绑定线程锁
    lock = threading.Lock()

    def decorator(cls):
        # 替换 __new__ 函数
        instance_attr = '_instance'
        # 获取原来的__new__函数 防止无限递归
        __origin_new__ = cls.__new__

        @wraps(__origin_new__)
        def __new__(cls_1, *args, **kwargs):
            if not hasattr(cls_1, instance_attr):
                with lock:
                    if not hasattr(cls_1, instance_attr):
                        setattr(cls_1, instance_attr, __origin_new__(cls_1, *args, **kwargs))
            return getattr(cls_1, instance_attr)

        cls.__new__ = __new__

        # 替换 __init__函数 原理同上
        init_flag = '_init_flag'
        __origin_init__ = cls.__init__

        @wraps(__origin_init__)
        def __init__(self, *args, **kwargs):
            if not hasattr(self, init_flag):
                with lock:
                    if not hasattr(self, init_flag):
                        __origin_init__(self, *args, **kwargs)
                        setattr(self, init_flag, True)

        cls.__init__ = __init__
        return cls

    return decorator

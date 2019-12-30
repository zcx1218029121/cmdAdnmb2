"""
命令行刷岛工具
"""
from src.StringInfo import *
from src.BaseItem import *
from src.out import OutPutUtil
import json
from src.net.Api import *

plate_pager = 1

details_pager = 1

state = 0

cur_id = 0

# 平台页 item 缓存
palte_item_cache = []

# 详情页 item 缓存
details_item_cache = []


def request_palte(pager):
    jsons = json.loads(get_plate_info(4, pager))
    index = 0
    for item in jsons:
        string = BaseItem(item)
        palte_item_cache.append(string)
        OutPutUtil.singleton.log("------------")
        OutPutUtil.singleton.log("【%d】" % index)
        OutPutUtil.singleton.log(string.content)
        index = index + 1


def show_info(info):
    OutPutUtil.singleton.log(creartHeader(info))
    for reply in info["replys"]:
        OutPutUtil.singleton.log(creat_item(reply))


def show_info_all(id, pager):
    """
    详情页全文展示
    """
    text = get_string_info_url(id, pager)
    info = json.loads(text)

    stinginfo = StringInfo(info)
    OutPutUtil.singleton.log(creartHeader(stinginfo))
    for reply in stinginfo.replys:
        details_item_cache.append(reply)
        OutPutUtil.singleton.log(creat_item(reply))
    return stinginfo.replys


def creartHeader(info):
    return "------- info ---------\n " + info.content + "\n"


def creat_item(reply):
    return "---\n" + reply.userid + ":\n" + reply.content + "\n"


def creat_welcome():
    return """  
    欢迎，A岛是一个前台匿名后台实名的论坛，旨在为大家提供一个理性客观中立的讨论环境，请不要发表涉政敏感信息，遵守相关法律法规。
    A岛核心精神：开放包容，理性客观，有事说事，就事论事
    有问题请转向值班室留言或联系help@adnmb.com              
    """


def creat_exit():
    return """  
    退出              
    """


if __name__ == '__main__':
    # main loop
    OutPutUtil.singleton.log(creat_welcome())
    request_palte(plate_pager)
    plate_pager = plate_pager + 1
    while True:
        ip = input()
        if ip == "exit":
            OutPutUtil.singleton.log(creat_exit())
            break
        if ip == "n":
            if state == 0:
                request_palte(plate_pager)
                plate_pager = plate_pager + 1
            else:
                show_info_all(palte_item_cache[cur_id].id, details_pager)
                details_pager = details_pager + 1
            continue
        if ip == "b":
            state = 0
            details_pager = 1
            continue
        try:
            cur_id = int(ip)
            details_pager = 1
            show_info_all(palte_item_cache[int(ip)].id, details_pager)
            details_pager = details_pager + 1
            state = 1
        except Exception:
            OutPutUtil.singleton.log("错误的输入")

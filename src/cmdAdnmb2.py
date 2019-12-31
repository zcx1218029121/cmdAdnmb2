"""
命令行刷岛工具
"""
from src.StringInfo import *
from src.BaseItem import *
from src.out import OutPutUtil
import json
from src.net.Api import *
from src.config.ConfigReader import *

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
    palte_item_cache.clear()
    for item in jsons:
        string = BaseItem(item)
        palte_item_cache.append(string)
        OutPutUtil.singleton.log("------------")
        OutPutUtil.singleton.log("【%d】" % index)
        OutPutUtil.singleton.log(string.content)
        index = index + 1


def show_info(info):
    """
    详情页部分展示 岛api 首页不知道为什么会有三个回复
    :param info:
    :return:
    """
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
    details_item_cache.clear()
    for reply in stinginfo.replys:
        details_item_cache.append(reply)
        OutPutUtil.singleton.log(creat_item(reply, reply.userid == stinginfo.userid))
    return stinginfo.replys


def creartHeader(info):
    return "------- info ---------\n " + info.content + "\n" + info.userid + "\n"


def creat_item(reply, is_pou):
    if is_pou:
        return "---\n" + "POU:" + reply.userid + ":\n" + reply.content + "\n"
    else:
        return "---\n" + reply.userid + ":\n" + reply.content + "\n"


def creat_welcome():
    return ConfigReader.get_config().welcome


def creat_exit():
    return ConfigReader.get_config().bye


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
        elif ip == "n":
            if state == 0:
                request_palte(plate_pager)
                plate_pager = plate_pager + 1
            else:
                show_info_all(palte_item_cache[cur_id].id, details_pager)
                details_pager = details_pager + 1
        elif ip == "b":
            state = 0
            details_pager = 1

        elif ip.startswith(ConfigReader.get_config().prefix_re):
            OutPutUtil.singleton.log(ip[3:])
            OutPutUtil.singleton.log(post_data(palte_item_cache[cur_id].id, ip[2:]))
        else:
            try:
                cur_id = int(ip)
                details_pager = 1
                show_info_all(palte_item_cache[int(ip)].id, details_pager)
                details_pager = details_pager + 1
                state = 1
            except Exception:
                OutPutUtil.singleton.log("错误的输入")

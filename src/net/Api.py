import requests
from src.config.ConfigReader import *

appid = "&appid=e31c86032f0d607c&__t=1571144068156"
plate_url = "https://adnmb2.com/Api/showf?id=%s&page=%s"
sting_info_url = "https://nmb.fastmirror.org/Api/thread?id=%s&page=%d"
re_url = "https://adnmb.com/Home/Forum/doReplyThread.html"


def get_plate_info(id, pager):
    """
    :param id: 板块 id
    :param pager:  当前页码
    :return:
    """
    url = plate_url % (id, pager) + appid
    text = requests.get(headers=ConfigReader.get_config().header, url=url).text
    return text


def get_string_info_url(id, pager):
    """
    :param id: 串 id
    :param pager: 分页
    :return:
    """
    url = sting_info_url % (id, pager) + appid
    text = requests.get(headers=ConfigReader.get_config().header, url=url).text
    return text


def post_data(resto, content, title="", name="", email=""):
    data = {
        "resto": resto,
        "content": content,
        "title": title,
        "name": name,
        "email": email,
        "water": "true"
    }
    text = requests.post(headers=ConfigReader.get_config().header, url=re_url, data=data,
                         cookies=ConfigReader.get_config().cookies).text
    if "回复成功" in text:
        return ConfigReader.get_config().send_ok
    elif "没有饼干" in text:
        return ConfigReader.get_config().no_cookies
    elif "冷却" in text:
        return "冷却中"

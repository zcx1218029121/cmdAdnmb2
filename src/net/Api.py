import requests

appid = "&appid=e31c86032f0d607c&__t=1571144068156"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}

plate_url = "https://adnmb2.com/Api/showf?id=%s&page=%s"

sting_info_url = "https://nmb.fastmirror.org/Api/thread?id=%s&page=%d"


def get_plate_info(id, pager):
    """
    :param id: 板块 id
    :param pager:  当前页码
    :return:
    """
    url = plate_url % (id, pager) + appid
    text = requests.get(headers=header, url=url).text
    return text


def get_string_info_url(id, pager):
    """
    :param id: 串 id
    :param pager: 分页
    :return:
    """
    url = sting_info_url % (id, pager) + appid
    text = requests.get(headers=header, url=url).text
    return text

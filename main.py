import time
import json
import requests
from win10toast import ToastNotifier

def _get_follower(url: str):
    return int(json.loads(requests.get(url).text)['data']['follower'])

def _get_top_artivle_view(url: str):
    return int(json.loads(requests.get(url).text)['data']['stat']['view'])

def _get_top_artivle_like(url: str):
    return int(json.loads(requests.get(url).text)['data']['stat']['like'])

_follower = _get_follower("https://api.bilibili.com/x/relation/stat?vmid=1865984682")
_top_artivle_view = _get_top_artivle_view("https://api.bilibili.com/x/space/top/arc?vmid=1865984682")
_top_artivle_like = _get_top_artivle_like("https://api.bilibili.com/x/space/top/arc?vmid=1865984682")

while True:
    print("刷新...")

    follower = _get_follower("https://api.bilibili.com/x/relation/stat?vmid=1865984682")
    top_artivle_view = _get_top_artivle_view("https://api.bilibili.com/x/space/top/arc?vmid=1865984682")
    top_artivle_like = _get_top_artivle_like("https://api.bilibili.com/x/space/top/arc?vmid=1865984682")

    if follower > _follower:
        _title = "恭喜你，你新增了 " + str(follower - _follower) + " 个粉丝！"
        _msg = "你现在的粉丝量为：" + str(follower)
        ToastNotifier.show_toast(title=_title, msg=_msg, duration=15)
        _follower = follower
    elif follower < _follower:
        _title = "啊哦，你掉了 " + str(_follower - follower) + " 个粉丝！ "
        _msg = "你现在的粉丝量为：" + str(follower)
        ToastNotifier.show_toast(title=_title, msg=_msg, duration=5)
        _follower = follower

    if top_artivle_view > _top_artivle_view:
        _title = "恭喜你，你最近一期视频的播放量新增了 " + str(top_artivle_view - _top_artivle_view)
        _msg = "现在的播放量为：" + str(top_artivle_view)
        ToastNotifier.show_toast(title=_title, msg=_msg, duration=15)
        _top_artivle_view = top_artivle_view

    if top_artivle_like > _top_artivle_like:
        _title = "恭喜你，你最近一期视频的点赞数新增了 " + str(top_artivle_like - _top_artivle_like)
        _msg = "现在的点赞数为：" + str(top_artivle_like)
        ToastNotifier.show_toast(title=_title, msg=_msg, duration=15)
        _top_artivle_like = top_artivle_like
            
    time.sleep(60)

    

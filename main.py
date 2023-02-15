import time
import json
import requests

from win10toast import ToastNotifier
t = ToastNotifier()

rp = requests.get("https://api.bilibili.com/x/relation/stat?vmid=1865984682")
jsd = json.loads(rp.text)
flr = jsd['data']['follower']
flrnw = int(flr)

rp1 = requests.get("https://api.bilibili.com/x/space/top/arc?vmid=1865984682&jsonp=jsonp")
jsd1 = json.loads(rp1.text)
flr1 = jsd1['data']['stat']['view']
like = jsd1['data']['stat']['like']
likecot = int(like)
cot = int(flr1)
ct = 0

haha = 0
while haha == 0:
        print("刷新..")
        ct += 1
        rp = requests.get("https://api.bilibili.com/x/relation/stat?vmid=1865984682")
        jsd = json.loads(rp.text)
        flr = jsd['data']['follower']

        rp1 = requests.get("https://api.bilibili.com/x/space/top/arc?vmid=1865984682&jsonp=jsonp")
        jsd1 = json.loads(rp1.text)
        flr1 = jsd1['data']['stat']['view']
        like = jsd1['data']['stat']['like']

        if int(flr) > int(flrnw):
                ti = "恭喜你，你新增了 " + str(int(flr) - int(flrnw)) + " 个粉丝！"
                rule = "你现在的粉丝量为：" + str(flr)
                t.show_toast(title=ti, msg=rule, duration=15)
                flrnw = int(flr)
        elif int(flr) < int(flrnw):
                ti = "啊哦，你掉了 " + str(int(flrnw) - int(flr)) + " 个粉丝！ "
                rule = "你现在的粉丝量为：" + str(flr)
                t.show_toast(title=ti, msg=rule,
                        duration=5)
                flrnw = int(flr)

        if int(flr1) > int(cot):
                ti = "恭喜你，你最近一期视频的播放量新增了 " + str(int(flr1) - int(cot))
                rule = "现在的播放量为：" + str(flr1)
                t.show_toast(title=ti, msg=rule, duration=15)
                cot = int(flr1)

        if int(like) > int(likecot):
                ti = "恭喜你，你最近一期视频的点赞数新增了 " + str(int(like) - int(likecot))
                rule = "现在的点赞数为：" + str(like)
                t.show_toast(title=ti, msg=rule, duration=15)
                likecot = int(like)
                
        time.sleep(60)

        

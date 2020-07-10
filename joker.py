"""
@program: jihuomaIDEA
@description: 
@author: gaigaibill@gamil.com
@create: 2020-06-30 01:00
"""

import mitmproxy.http
from mitmproxy import ctx, http
import os


class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):

        if flow.request.host == "www.damiwangxiao.com":
            flow.response = http.HTTPResponse.make(404)
        # print('请求状态码：'+flow.get_state())
        if flow.request.host == 'www.baidu.com':
            os.system("terminal-notifier -message 'Hello, this is my message' -title "+ flow.get_state() +"")
        # if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
        #     return
        #
        # if "wd" not in flow.request.query.keys():
        #     ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
        #     return
        #
        # ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        # flow.request.query.set_all("wd", ["哈哈哈哈"])

    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass

        # print('返回状态码：'+flow.get_state())
        # os.system("terminal-notifier -message 'Hello, this is my message' -title "+ flow.get_state() +"")

    # if flow.request.host == "www.damiwangxiao.com":
        #     flow.response = http.HTTPResponse.make(404)


            # text = flow.response.get_text()
            # text = text.replace("登录", "这是线上环境")
            # flow.response.set_text(text)

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "www.google.com":
            pass
            # flow.response = http.HTTPResponse.make(404)
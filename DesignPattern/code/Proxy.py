#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/25 14:50:27
# @Author  :   Gary
# @Email   :   None
# 该服务器接受如下格式数据，addr代表地址，content代表接收的信息内容
info_struct = dict()
info_struct["addr"] = 10000
info_struct["content"] = ""


class Server:
    # 抽象类
    content = ""

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class infoServer(Server):
    # 具体类
    def recv(self, info):
        self.content = info
        return "recv OK!"

    def send(self, info):
        pass

    def show(self):
        print("SHOW:%s" % self.content)


class serverProxy:
    pass


class infoServerProxy(serverProxy):
    server = ""

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class whiteInfoServerProxy(infoServerProxy):
    # 代理类
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info structure is not correct"
        addr = info.get("addr", 0)
        if not addr in self.white_list:
            return "Your address is not in the white list."
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def addWhite(self, addr):
        self.white_list.append(addr)

    def rmvWhite(self, addr):
        self.white_list.remove(addr)

    def clearWhite(self):
        self.white_list = []


if __name__ == "__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = infoServer()
    info_server_proxy = whiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()

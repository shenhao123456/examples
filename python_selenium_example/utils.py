import logging
import os

from browsermobproxy import Server

cur_dir_path = os.path.abspath('.')


# 重写server 解决程序关闭后server关闭问题
class ProxyServer(Server):

    def __init__(self, path='browsermob-proxy', options=None):
        options = options if options is not None else {}

        self.path = path
        self.host = 'localhost'
        self.port = options.get('port', 8080)
        self.process = None
        self.command = []

        self.command += ["java", "-Dapp.name=browsermob-proxy",
                         "-Dbasedir=%s/browsermob-proxy-2.1.4" % cur_dir_path, "-jar",
                         "%s/browsermob-proxy-2.1.4/lib/browsermob-dist-2.1.4.jar" % cur_dir_path,
                         '--port=%s' % self.port]

    def get_process_pid(self):
        return self.process.pid


# 获取当前服务器能生成的最大代理数
def max_count_of_proxy():
    server = ProxyServer(cur_dir_path + "/browsermob-proxy-2.1.4/bin/browsermob-proxy",
                         options={'port': 9090})
    server.start()
    num = 0
    while num < 200:
        try:
            proxy = server.create_proxy()
            # print(proxy.proxy)
            num += 1
        except Exception as e:
            # print(e)
            break
    server.stop()
    print(num)
    return num


class Page:
    def __init__(self, current_page, data_count, per_page_count=10):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count = per_page_count

    @property
    def start(self):
        if self.current_page > self.total_page and self.total_page != 0:
            self.current_page = self.total_page
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        return self.current_page * self.per_page_count

    @property
    def total_page(self):
        v, y = divmod(self.data_count, self.per_page_count)
        if y:
            v += 1
        return v


# 配置简单日志
def get_log():
    log = logging.getLogger('genhar')
    log.setLevel(logging.INFO)
    LOG_FORMAT = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    file_handler = logging.FileHandler(cur_dir_path + '/genhar.log')
    console_handler = logging.StreamHandler()
    file_handler.setFormatter(LOG_FORMAT)
    console_handler.setFormatter(LOG_FORMAT)
    log.addHandler(file_handler)
    return log

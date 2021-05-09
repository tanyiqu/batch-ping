import subprocess
import threading
import time
import re


class Ping(threading.Thread):
    def __init__(self, str_ip, sleep_time):
        threading.Thread.__init__(self)
        self.str_ip = str_ip
        self.sleep_time = sleep_time

    def run(self):
        print('run', self.str_ip)
        # time.sleep(self.sleep_time)
        ftp_ret = subprocess.Popen(
            'ping %s -n 3' % self.str_ip, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ret = ftp_ret.stdout.read()
        str_ret = ret.decode("gbk")
        ret_s = re.search("TTL", str_ret)

        if ret_s:
            print(self.str_ip, 'ok')
        else:
            print(self.str_ip, 'no')


def main():
    print('start')
    Ping('127.0.0.1', 1).run()
    Ping('192.168.0.100', 1).run()
    pass


main()

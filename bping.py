from core.Ping import Ping

if __name__ == '__main__':
    print('start batch ping...')

    fin = open('ip.txt')

    for ip in fin:
        Ping(ip.strip()).test_ping()

    fin.close()
    pass

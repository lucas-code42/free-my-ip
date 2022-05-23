from proxy import FreeMyIp


if __name__ == '__main__':
    proxys = FreeMyIp()

    test_1 = proxys.get_socks_proxies()
    test_2 = proxys.get_proxies()
    test_3 = proxys.get_us_proxies()
    test_4 = proxys.get_random_proxies()

    print(test_1)
    print(test_2)
    print(test_3)
    print(test_4)
    
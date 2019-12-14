

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print('cls:', cls)
        print(name)
        print(bases)
        print(attrs)

        count = 0
        attrs['__CrawelFunc__'] = []
        for k, v in attrs.items():
            if 'crawel_' in k:
                attrs['__CrawelFunc__'].append(k)
                count += 1

        attrs['__CrawelFuncCount__'] = count
        print(attrs)
        return type.__new__(cls, name, bases, attrs)


class Proxy(object, metaclass=ProxyMetaclass):
    def __init__(self):
        pass

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理 {}'.format(proxy))
            proxies.append(proxy)
        return proxies

    def crawel_51daili(self):
        print('crawel_51daili')

    def crawel_3366daili(self):
        print('crawel_3366daili')

    def crawel_sundaili(self):
        print('crawel_sundaili')

    def run(self):
        print('Proxy run')


if __name__ == '__main__':
    proxy = Proxy()
    # proxy.run()


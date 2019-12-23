import requests


@staticmethod
def get_http_session(pool_connections=1, pool_maxsize=10, max_retries=3):
    """
    http连接池
    pool_connections 要缓存的 urllib3 连接池的数量。
    pool_maxsize 要保存在池中的最大连接数。
    max_retries 每个连接的最大重试次数
    """
    session = requests.session()
    # 创建适配器
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=pool_connections,
        pool_maxsize=pool_maxsize,
        max_retries=max_retries
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


if __name__ == '__main__':
    get_http_session()

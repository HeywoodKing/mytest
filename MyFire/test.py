import fire


def add(a, b):
    count = a + b
    return count


def sub(a, b):
    result = a - b
    return result


def main():
    pass


class Calculator(object):
    def add(self, a, b):
        count = a + b
        return count

    def sub(self, a, b):
        result = a - b
        return result


if __name__ == '__main__':
    # main()
    # fire.Fire(add)
    fire.Fire()
    # 这里用类名Calculator或者类的实例化对象Calculator()结果都是一样的
    fire.Fire(Calculator)

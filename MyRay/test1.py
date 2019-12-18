
import ray


@ray.remote()
def func1():
    print(1)


@ray.remote()
def func2():
    print(2)


def main():
    ray.init()
    func1.remote()
    func2.remote()


if __name__ == '__main__':
    main()

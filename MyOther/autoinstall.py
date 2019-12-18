import sys
import os
from importlib import import_module


class AutoInstall(object):
    _loaded = set()

    @classmethod
    def find_lib(cls, name, path, target=None):
        if path is None and name not in cls._loaded:
            cls._loaded.add(name)
            print("Installing", name)
            try:
                pypi = 'https://pypi.tuna.tsinghua.edu.cn/simple'
                result = os.system('pip install {} -i {}'.format(name, pypi))
                # result = os.system('pipenv install {}'.format(name))
                if result == 0:
                    return import_module(name)
            except Exception as e:
                print("Failed", e)
        return None


sys.meta_path.append(AutoInstall)

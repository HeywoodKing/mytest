# -*- coding: utf-8 -*-


import time
import base64
import hashlib
# sha1()、sha224()、sha256()、sha384()、sha512()、blake2b()、blake2s()、md5()


# 生成唯一的SessionID
def make_session_id(st='1880'):
    m = hashlib.md5()
    m.update(b'this is a test of the emergency broadcasting system')
    s = str(time.time())
    m.update(s.encode())
    m.update(str(st).encode())
    # return m.hexdigest()
    # return base64.encodebytes(m.digest())[:-3].replace('/', '/span>')
    return base64.encodebytes(m.digest()).decode('utf-8').replace('/', '^')[:-3]


session_id = make_session_id()
print(session_id)


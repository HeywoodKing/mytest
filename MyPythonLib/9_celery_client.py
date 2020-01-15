# -*- coding: utf-8 -*-


from FastCelery.tasks import add, reduce, multi, divide, notice
from FastCelery.tasks import app

# res_add = add.delay(2, 2)
# print(res_add.ready(), res_add.result)
# print(res_add.ready(), res_add.result, res_add.revoke)

# res_red = minus.delay(2, 2)
# print(res_red.ready(), res_red.result)

# res_mul = multi.delay(2, 2)
# print(res_mul.ready())
# print(res_mul.result)

res_div = divide.delay(2, 3)
if res_div.ready():
    print(res_div.result)
else:
    # print('No', res_div.status)
    print(res_div.status)


# res_notice = notice.delay('22222')
# print(res_notice.result)

# result = divide.apply_async((2, 3), )
# result = app.send_task('tasks.add', [1, 2])
# print(result)

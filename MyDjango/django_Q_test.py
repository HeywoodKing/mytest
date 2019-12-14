

import operator
from django.db.models import *

# def test():
#     electrons = self.es_electron(model_name, factory)
#     # print('electrons: {}'.format(electrons))
#     print("before: {}".format(queryset))
#     if  len(electrons)  >  0:
#
#
#         q_list = []
#         for  i  in  range(0,  len(electrons)):
#             print(electrons[i])
#             q_list.append(Q(Q(model_name=electrons[i]["partnumber"]), Q(factory=electrons[i]["supplier"])))
#
#
#         Electron.objects.filter(
#             [reduce(operator.or_, [x for x in q_list])]
#             ~Q(id=electron.id),
#             isDelete=False,
#         )






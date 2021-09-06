# def work_on_product_list(product_list):
#
#     new_product_list = dict()
#     new_product_list['products'] = product_list['products']
#     new_product_list['total_price'] = 0
#     price = 'price'
#     cost = 'net_cost'
#
#     for index in range(len(new_product_list['products'])):
#         new_product_list['products'][index][price] = new_product_list['products'][index].pop(cost)
#         new_product_list['products'][index][price] *= (product_list['margin'] + 1) * (product_list['tax'] + 1)
#         new_product_list['total_price'] += new_product_list['products'][index][price]
#
#     print(new_product_list)
#
# import math
# print(math.floor(5.5))
# a = {}
# a[1] = 1
# print(a)
# a = {}
# print(len(a))
# print(0.1+0.2 == 0.3)
#
# a = 5
# a += 2
# print(a)
# t = (1,2,3,(1,2), None, {})
# print(len(t))
# name="SoftServe"
# print(name.title())

class A():
    def __init__(self, id):
        self.id = id
        id=666

a = [1]
a += [2]
print(a)